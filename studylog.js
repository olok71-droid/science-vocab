// 공부기록 — 서정이가 앱에서 한 공부를 Supabase amy_study_log 에 남긴다.
// 페이지 맨 끝에서 불러 온다(그래야 페이지의 함수들을 감쌀 수 있다).
// 남기는 것: 화면별 머문 시간(time) · 외운 단어(mem/unmem) · 발음 들은 단어(say)
//          · 듣기 시간(listen: 전체/부분/이어 듣기) · 단어시험(spell) · 서술형 문제(quiz/rate) · 객관식 퀴즈(pick)
(function(){
  // 페이지의 다른 스크립트가 다 읽힌 뒤에 시작한다(그래야 함수를 감쌀 수 있다).
  function start(){
  if (window.__amyStudyLog) return;
  window.__amyStudyLog = true;
  // 맥 자동화(헤드리스 크롬·검사 도구)가 연 것은 기록하지 않는다
  if (navigator.webdriver || /HeadlessChrome/.test(navigator.userAgent)) return;

  var URL = 'https://pwbnbooyhujyzbmaydtp.supabase.co/rest/v1/';
  var KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB3Ym5ib295aHVqeXpibWF5ZHRwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA4MTU0NTQsImV4cCI6MjA5NjM5MTQ1NH0.BwKTVgnswWqPlAdclwMpso6kcEA2x0d502CXv2DvBIE';
  var PAGE = (location.pathname.split('/').pop() || 'index.html');
  var TITLE = (document.title || '').trim().slice(0, 120);
  var IN_FRAME = (window.top !== window.self);

  function ls(k){ try { return localStorage.getItem(k); } catch(e){ return null; } }
  function lsSet(k, v){ try { localStorage.setItem(k, v); } catch(e){} }

  var DEV = ls('amy_dev');
  if (!DEV) { DEV = 'd' + Date.now().toString(36) + Math.random().toString(36).slice(2, 8); lsSet('amy_dev', DEV); }

  function kstDay(){ var d = new Date(Date.now() + 9 * 3600e3); return d.toISOString().slice(0, 10); }
  function head(extra){
    var h = { apikey: KEY, Authorization: 'Bearer ' + KEY, 'Content-Type': 'application/json' };
    for (var k in (extra || {})) h[k] = extra[k];
    return h;
  }

  // 기기 등록(처음 한 번). 어느 기기가 서정이 것인지는 공부기록 화면에서 고른다.
  if (ls('amy_dev_reg') !== DEV) {
    fetch(URL + 'amy_study_dev', { method: 'POST', headers: head({ Prefer: 'resolution=ignore-duplicates' }),
      body: JSON.stringify({ dev: DEV, ua: navigator.userAgent.slice(0, 200) }) })
      .then(function(r){ if (r.ok) lsSet('amy_dev_reg', DEV); }).catch(function(){});
  }

  // ── 보낼 줄 모으기 ──
  // 줄은 바로 폰(localStorage)에 넣고, 보낸 줄만 cid로 골라 지운다. 탭이 여러 개여도 서로 덮어쓰지 않는다.
  // 인터넷이 끊겨 못 보낸 줄은 다음에 같이 보낸다. 같은 줄이 두 번 가도 cid 때문에 한 번만 들어간다.
  function loadQ(){ try { return JSON.parse(ls('amy_log_q') || '[]') || []; } catch(e){ return []; } }
  function saveQ(q){ lsSet('amy_log_q', JSON.stringify(q.slice(-1000))); }
  function add(kind, detail, n){
    var q = loadQ();
    q.push({ cid: DEV + '-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 7), ts: new Date().toISOString(), day: kstDay(), dev: DEV, page: PAGE, title: TITLE,
             kind: kind, detail: detail == null ? null : String(detail).slice(0, 300), n: n == null ? null : Math.round(n) });
    saveQ(q);
  }
  // keepalive 요청은 본문 64KB까지라 25줄씩 나눠 보낸다(한 줄 최대 약 1.5KB).
  var sending = false;
  function flush(){
    if (sending || !navigator.onLine) return;
    var rows = loadQ().slice(0, 25);
    if (!rows.length) return;
    sending = true;
    fetch(URL + 'amy_study_log?on_conflict=cid', { method: 'POST', keepalive: true, headers: head({ Prefer: 'return=minimal,resolution=ignore-duplicates' }), body: JSON.stringify(rows) })
      .then(function(r){
        if (!r.ok) return false;
        var sent = {}; rows.forEach(function(x){ sent[x.cid] = 1; });
        saveQ(loadQ().filter(function(x){ return !sent[x.cid]; }));
        return true;
      })
      .catch(function(){ return false; })
      .then(function(ok){ sending = false; if (ok && loadQ().length) setTimeout(flush, 300); });
  }

  // ── 화면별 머문 시간 ──
  // 화면이 보이고, 5분 안에 손을 댄 시간만 센다.
  function screenName(){
    var t = document.querySelector('.tab-btn.active');
    if (t) return t.textContent.replace(/\s+/g, ' ').trim();
    if (document.body && document.body.classList.contains('in-subject')) {
      var l = document.querySelector('.cat-pane.active .subject-label .name-en');
      if (l) return l.textContent.trim();
    }
    return '';
  }
  var acc = {}, last = Date.now(), lastAct = Date.now();
  var lastTap = 0, lastTapEl = null;   // 마지막으로 손가락으로 누른 때와 누른 것
  ['pointerdown', 'keydown', 'scroll', 'touchstart', 'input', 'click'].forEach(function(ev){
    window.addEventListener(ev, function(e){
      lastAct = Date.now();
      if (ev === 'pointerdown' || ev === 'click' || ev === 'touchstart' || ev === 'keydown') { lastTap = Date.now(); lastTapEl = e.target; }
    }, { passive: true, capture: true });
  });
  function tick(){
    var now = Date.now(), dt = now - last; last = now;
    if (IN_FRAME || document.visibilityState !== 'visible') return;
    if (now - lastAct > 5 * 60e3) return;
    if (dt > 5000) dt = 5000;
    var s = screenName();
    acc[s] = (acc[s] || 0) + dt;
  }
  function dumpTime(){
    tick();
    for (var s in acc) { var sec = acc[s] / 1000; if (sec >= 5) add('time', s, sec); }
    acc = {};
  }
  setInterval(tick, 1000);
  setInterval(function(){ dumpTime(); flush(); }, 60e3);
  document.addEventListener('visibilitychange', function(){
    if (document.visibilityState === 'hidden') { dumpTime(); seqDump(); flush(); }
    else { last = Date.now(); lastAct = Date.now(); flush(); }
  });
  window.addEventListener('pagehide', function(){ dumpTime(); seqDump(); flush(); });
  window.addEventListener('online', flush);

  // ── 단어 이름 찾기 ──
  // from: 'opic'(OPIc 문장 번호) · 'jenny'(제니 단어장 번호) · 없으면 단어 카드(slug)부터 찾는다.
  function slug(t){ return (t || '').replace(/~/g, '').replace(/\//g, ' ').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, ''); }
  function fromOpic(x){
    try {
      if (typeof OPIC === 'undefined') return null;
      for (var g = 0; g < OPIC.length; g++) {
        var it = (OPIC[g].items || []).find(function(o){ return String(o.n) === String(x); });
        if (it) return it.en + (it.ko ? ' · ' + it.ko : '');
      }
    } catch(e){}
    return null;
  }
  function fromData(x){
    try {
      if (typeof DATA === 'undefined' || !DATA.find) return null;
      var d = DATA.find(function(o){ return String(o.id) === String(x); });
      if (d) return (d.en || d.hz || d.w || '') + (d.ko ? ' · ' + d.ko : '');
    } catch(e){}
    return null;
  }
  function fromCard(x){
    var cards = document.querySelectorAll('.vcard');
    for (var i = 0; i < cards.length; i++) {
      var en = cards[i].querySelector('.vcard-en');
      if (en && slug(en.textContent.trim()) === x) {
        var ko = cards[i].querySelector('.vcard-ko');
        return en.textContent.trim() + (ko ? ' · ' + ko.textContent.trim() : '');
      }
    }
    return null;
  }
  function wordOf(x, from){
    var r = from === 'opic' ? fromOpic(x) : from === 'jenny' ? fromData(x) : (fromCard(x) || fromData(x));
    return r || String(x).replace(/_/g, ' ');
  }

  // ── 외운 단어: memv_ 저장을 지켜본다 ──
  try {
    var origSet = Storage.prototype.setItem;
    Storage.prototype.setItem = function(k, v){
      if (this === window.localStorage && typeof k === 'string' && k.indexOf('memv_') === 0) {
        try {
          var from = k === 'memv_opic' ? 'opic' : k === 'memv_jenny' ? 'jenny' : null;
          var before = JSON.parse(this.getItem(k) || '[]') || [];
          var after = JSON.parse(v || '[]') || [];
          var b = {}, a = {};
          before.forEach(function(x){ b[x] = 1; });
          after.forEach(function(x){ a[x] = 1; });
          var plus = after.filter(function(x){ return !b[x]; });
          var minus = before.filter(function(x){ return !a[x]; });
          if (plus.length + minus.length <= 10) {
            plus.forEach(function(x){ add('mem', wordOf(x, from), 1); });
            minus.forEach(function(x){ add('unmem', wordOf(x, from), 1); });
          } else if (minus.length && !after.length) {
            add('unmem', '외움 표시 모두 지움', minus.length);
          }
        } catch(e){}
      }
      return origSet.apply(this, arguments);
    };
  } catch(e){}

  // ── 발음 들은 단어 ──
  // 손으로 단어 하나를 눌러 들은 것만 '발음 들은 단어'로 남긴다.
  // 전체·부분 듣기 버튼으로 이어서 나오는 소리는 단어로 남기지 않고 듣기 시간으로 센다.
  function tappedOne(){
    if (Date.now() - lastTap > 1500 || !lastTapEl || !lastTapEl.closest) return false;
    var b = lastTapEl.closest('button,a,[onclick]');
    if (!b) return true;
    if (/듣기|▶/.test(b.textContent || '') || /chunkplay/.test(b.className || '')) return false;
    return !/^\s*(playAll|toggleAllPlay|togglePlayAll|playSection|playDay|opDrill|opPlayAll|playList)/.test(b.getAttribute('onclick') || '');
  }
  var lastSay = {}, noSay = false;
  function say(word){
    if (noSay || !tappedOne()) return;
    var w = (word || '').trim(); if (!w) return;
    var now = Date.now();
    if (lastSay[w] && now - lastSay[w] < 1500) return;   // 같은 단어가 두 길(speak·재생)로 겹쳐 들어오는 것 한 번만
    lastSay[w] = now;
    add('say', w, 1);
  }
  if (typeof window.speak === 'function') {
    var origSpeak = window.speak;
    window.speak = function(text){ try { say(wordOf(slug(text))); } catch(e){} return origSpeak.apply(this, arguments); };
  }

  // ── 듣기 시간 ──
  // 합친 mp3(전체 _all · 부분 _pN)는 실제로 소리가 난 시간을 그 이름으로 센다(화면이 꺼져도 센다).
  // 한 재생기에서 주소만 바꿔 다른 토막을 틀어도, 바뀌는 순간(emptied·abort) 앞 토막을 끊어 따로 센다.
  function chunkLabel(src){
    var f = src.split('/').pop() || '', m;
    if (/_all\.mp3$/.test(f)) return '전체 듣기';
    if ((m = src.match(/\/audio\/[^\/]+_p(\d+)\.mp3$/))) return '부분 듣기 ' + m[1];
    return null;
  }
  function clipWord(src){
    var m;
    if (/\/audio\/sci\//.test(src)) return wordOf((src.split('/').pop() || '').replace(/\.mp3$/, ''));
    if ((m = src.match(/\/audio\/jenny\/w(\d+)\.mp3$/))) return wordOf(m[1], 'jenny');
    if ((m = src.match(/\/audio\/opic\/e(\d+)\.mp3$/))) return wordOf(m[1], 'opic');
    return null;
  }
  function srcOf(el){ try { return decodeURIComponent((el.currentSrc || el.src || '').split('?')[0]); } catch(e){ return el.currentSrc || el.src || ''; } }

  // 낱개 소리를 이어서 튼 시간(외운 단어가 있을 때의 전체 듣기, 제니·OPIc 이어듣기)
  var seqSec = 0, seqTimer = null;
  function seqAdd(sec){
    seqSec += sec;
    clearTimeout(seqTimer);
    seqTimer = setTimeout(function(){ seqDump(); flush(); }, 20e3);
  }
  function seqDump(){ if (seqSec >= 3) add('listen', '이어 듣기', seqSec); seqSec = 0; }

  function track(el){
    if (el.__amyT) return;
    var st = el.__amyT = { t: null, label: null, seq: false };
    el.addEventListener('playing', function(){
      var label = chunkLabel(srcOf(el)), seq = !label && !el.__amyTap;
      if (st.t != null) {
        if (label === st.label && seq === st.seq) return;   // 끊겼다 다시 나온 같은 소리(버퍼링)는 이어서 센다
        stop();
      }
      st.label = label; st.seq = seq;
      st.t = (label || seq) ? Date.now() : null;
    });
    function stop(){
      if (st.t == null) return;
      var sec = (Date.now() - st.t) / 1000; st.t = null;
      if (st.label) { if (sec >= 3) { add('listen', st.label, sec); flush(); } }
      else if (st.seq) seqAdd(sec);
    }
    ['pause', 'ended', 'emptied', 'abort', 'error'].forEach(function(ev){ el.addEventListener(ev, stop); });
    window.addEventListener('pagehide', stop);
  }
  try {
    var origPlay = HTMLMediaElement.prototype.play;
    HTMLMediaElement.prototype.play = function(){
      try {
        this.__amyTap = tappedOne();
        track(this);
        var w = clipWord(srcOf(this));
        if (w && this.__amyTap) say(w);
      } catch(e){}
      return origPlay.apply(this, arguments);
    };
  } catch(e){}

  // ── 단어시험(스펠링) ──
  if (typeof window.updateSpellStats === 'function') {
    var origUSS = window.updateSpellStats, pc = null, pw = null;
    window.updateSpellStats = function(){
      try {
        if (typeof spellState !== 'undefined' && spellState) {
          var c = spellState.correct || 0, w = spellState.wrong || 0;
          var cur = spellState.current;
          var name = cur ? (cur.en + (cur.ko ? ' · ' + cur.ko : '')) : '';
          if (pc != null && c > pc) add('spell', name, 1);
          if (pw != null && w > pw) add('spell', name, 0);
          pc = c; pw = w;
        }
      } catch(e){}
      return origUSS.apply(this, arguments);
    };
  }
  if (typeof window.showAnswer === 'function' && typeof window.updateSpellStats === 'function') {
    var origSA = window.showAnswer;
    window.showAnswer = function(){
      try {
        // 틀려서 정답이 저절로 나온 경우(wrong이 이미 늘었음)는 '틀림' 하나로만 남긴다.
        if (typeof spellState !== 'undefined' && spellState && spellState.current && !spellState.revealed && spellState.wrong === pw)
          add('spell', spellState.current.en + (spellState.current.ko ? ' · ' + spellState.current.ko : ''), -1);
      } catch(e){}
      noSay = true;   // 정답 보기의 자동 발음은 '발음 들은 단어'가 아니다
      try { return origSA.apply(this, arguments); } finally { noSay = false; }
    };
  }

  // ── 서술형 문제(모범답안 보기 · 스스로 채점) ──
  function qText(qi){
    var c = document.getElementById('q-card-' + qi);
    var t = c && c.querySelector('.q-text');
    return t ? t.textContent.replace(/\s+/g, ' ').trim() : ('문제 ' + (qi + 1));
  }
  if (typeof window.showModel === 'function') {
    var origSM = window.showModel;
    window.showModel = function(qi){
      try {
        var c = document.getElementById('q-card-' + qi);
        var ta = c && c.querySelector('textarea');
        add('quiz', qText(qi), ta ? ta.value.trim().length : null);
      } catch(e){}
      return origSM.apply(this, arguments);
    };
  }
  if (typeof window.rateSelf === 'function') {
    var origRS = window.rateSelf;
    window.rateSelf = function(qi, level){
      try {
        var c = document.getElementById('q-card-' + qi);
        var b = c && c.querySelector('.q-self-rate .rate-' + level);
        add('rate', qText(qi) + ' ⇒ ' + (b ? b.textContent.trim() : level), null);
      } catch(e){}
      return origRS.apply(this, arguments);
    };
  }

  // ── 객관식 퀴즈(중국어 등) ──
  if (typeof window.answerQuiz === 'function') {
    var origAQ = window.answerQuiz;
    window.answerQuiz = function(){
      var ok0 = null, cur = null, done = true;
      try { if (typeof quiz !== 'undefined') { ok0 = quiz.ok; cur = quiz.cur; done = quiz.answered; } } catch(e){}
      var r = origAQ.apply(this, arguments);
      try {
        if (!done && cur) {
          var name = (cur.hz || cur.en || '') + (cur.py ? ' (' + cur.py + ')' : '') + (cur.ko ? ' · ' + cur.ko : '');
          add('pick', name, quiz.ok > ok0 ? 1 : 0);
        }
      } catch(e){}
      return r;
    };
  }

  flush();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
