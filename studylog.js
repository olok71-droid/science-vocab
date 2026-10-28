// 공부기록 — 서정이가 앱에서 한 공부를 Supabase amy_study_log 에 남긴다.
// 페이지 맨 끝에서 불러 온다(그래야 페이지의 함수들을 감쌀 수 있다).
// 남기는 것: 화면별 머문 시간(time) · 외운 단어(mem/unmem) · 발음 들은 단어(say)
//          · 전체/부분 듣기(listen) · 단어시험(spell) · 서술형 문제(quiz/rate) · 객관식 퀴즈(pick)
(function(){
  // 페이지의 다른 스크립트가 다 읽힌 뒤에 시작한다(그래야 함수를 감쌀 수 있다).
  function start(){
  if (window.__amyStudyLog) return;
  window.__amyStudyLog = true;

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
  // 인터넷이 끊겨 못 보낸 줄은 폰에 두었다가 다음에 같이 보낸다.
  var Q = [];
  try { Q = JSON.parse(ls('amy_log_q') || '[]') || []; } catch(e){ Q = []; }
  function saveQ(){ lsSet('amy_log_q', JSON.stringify(Q.slice(-500))); }
  function add(kind, detail, n){
    Q.push({ cid: DEV + '-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 7), ts: new Date().toISOString(), day: kstDay(), dev: DEV, page: PAGE, title: TITLE,
             kind: kind, detail: detail == null ? null : String(detail).slice(0, 300), n: n == null ? null : Math.round(n) });
    saveQ();
  }
  var sending = false;
  function flush(){
    if (sending || !Q.length || !navigator.onLine) return;
    var rows = Q.slice(0, 200);
    sending = true;
    fetch(URL + 'amy_study_log?on_conflict=cid', { method: 'POST', keepalive: true, headers: head({ Prefer: 'return=minimal,resolution=ignore-duplicates' }), body: JSON.stringify(rows) })
      .then(function(r){ if (r.ok) { Q = Q.slice(rows.length); saveQ(); } })
      .catch(function(){})
      .then(function(){ sending = false; });
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
  ['pointerdown', 'keydown', 'scroll', 'touchstart', 'input'].forEach(function(ev){
    window.addEventListener(ev, function(){ lastAct = Date.now(); }, { passive: true, capture: true });
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
    if (document.visibilityState === 'hidden') { dumpTime(); flush(); }
    else { last = Date.now(); lastAct = Date.now(); flush(); }
  });
  window.addEventListener('pagehide', function(){ dumpTime(); flush(); });

  // ── 단어 이름 찾기 ──
  function slug(t){ return (t || '').replace(/~/g, '').replace(/\//g, ' ').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, ''); }
  function wordOf(x){
    // 1) 단어 카드(slug)
    var cards = document.querySelectorAll('.vcard');
    for (var i = 0; i < cards.length; i++) {
      var en = cards[i].querySelector('.vcard-en');
      if (en && slug(en.textContent.trim()) === x) {
        var ko = cards[i].querySelector('.vcard-ko');
        return en.textContent.trim() + (ko ? ' · ' + ko.textContent.trim() : '');
      }
    }
    // 2) 제니 단어장(DATA) · OPIc 문장(OPIC)
    try {
      if (typeof DATA !== 'undefined' && DATA.find) {
        var d = DATA.find(function(o){ return String(o.id) === String(x); });
        if (d) return (d.en || d.hz || d.w || '') + (d.ko ? ' · ' + d.ko : '');
      }
    } catch(e){}
    try {
      if (typeof OPIC !== 'undefined') {
        for (var g = 0; g < OPIC.length; g++) {
          var it = (OPIC[g].items || []).find(function(o){ return String(o.n) === String(x); });
          if (it) return it.en + (it.ko ? ' · ' + it.ko : '');
        }
      }
    } catch(e){}
    return String(x).replace(/_/g, ' ');
  }

  // ── 외운 단어: memv_ 저장을 지켜본다 ──
  try {
    var origSet = Storage.prototype.setItem;
    Storage.prototype.setItem = function(k, v){
      if (this === window.localStorage && typeof k === 'string' && k.indexOf('memv_') === 0) {
        try {
          var before = JSON.parse(origSet && this.getItem(k) || '[]') || [];
          var after = JSON.parse(v || '[]') || [];
          var b = {}, a = {};
          before.forEach(function(x){ b[x] = 1; });
          after.forEach(function(x){ a[x] = 1; });
          var plus = after.filter(function(x){ return !b[x]; });
          var minus = before.filter(function(x){ return !a[x]; });
          if (plus.length + minus.length <= 10) {
            plus.forEach(function(x){ add('mem', wordOf(x), 1); });
            minus.forEach(function(x){ add('unmem', wordOf(x), 1); });
          } else if (minus.length && !after.length) {
            add('unmem', '외움 표시 모두 지움', minus.length);
          }
        } catch(e){}
      }
      return origSet.apply(this, arguments);
    };
  } catch(e){}

  // ── 발음 들은 단어 · 전체/부분 듣기 ──
  var lastSay = {}, noSay = false;
  function say(word){
    if (noSay) return;
    var w = (word || '').trim(); if (!w) return;
    var now = Date.now();
    if (lastSay[w] && now - lastSay[w] < 1500) return;   // 같은 단어가 두 길로 겹쳐 들어오는 것 한 번만
    lastSay[w] = now;
    add('say', w, 1);
  }
  if (typeof window.speak === 'function') {
    var origSpeak = window.speak;
    window.speak = function(text){ try { say(wordOf(slug(text)) || text); } catch(e){} return origSpeak.apply(this, arguments); };
  }
  try {
    var origPlay = HTMLMediaElement.prototype.play;
    HTMLMediaElement.prototype.play = function(){
      try {
        var src = decodeURIComponent((this.currentSrc || this.src || '').split('?')[0]);
        var f = src.split('/').pop() || '';
        var m;
        if (/_all\.mp3$/.test(f)) { listenStart(this, '전체 듣기'); }
        else if ((m = src.match(/\/audio\/[^\/]+_p(\d+)\.mp3$/))) { listenStart(this, '부분 듣기 ' + m[1]); }
        else if (/\/audio\/sci\//.test(src)) { say(wordOf(f.replace(/\.mp3$/, ''))); }
        else if (/\/audio\/jenny\/w(\d+)\.mp3$/.test(src)) { say(wordOf(src.match(/w(\d+)\.mp3$/)[1])); }
        else if (/\/audio\/opic\/e(\d+)\.mp3$/.test(src)) { say(wordOf(src.match(/e(\d+)\.mp3$/)[1])); }
      } catch(e){}
      return origPlay.apply(this, arguments);
    };
  } catch(e){}
  // 합친 mp3를 실제로 들은 시간(화면이 꺼져도 센다)
  function listenStart(el, label){
    if (el.__amyL) { el.__amyL.label = label; return; }
    var st = { label: label, t: null };
    el.__amyL = st;
    el.addEventListener('playing', function(){ st.t = Date.now(); });
    function stop(){
      if (st.t == null) return;
      var sec = (Date.now() - st.t) / 1000; st.t = null;
      if (sec >= 3) { add('listen', st.label, sec); flush(); }
    }
    el.addEventListener('pause', stop);
    el.addEventListener('ended', stop);
    window.addEventListener('pagehide', stop);
  }

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
        if (typeof spellState !== 'undefined' && spellState && spellState.current && !spellState.revealed && spellState.wrong === pw)
          add('spell', spellState.current.en + (spellState.current.ko ? ' · ' + spellState.current.ko : ''), -1);
      } catch(e){}
      noSay = true;
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
