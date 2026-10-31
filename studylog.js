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
  ['pointerdown', 'keydown', 'scroll', 'touchstart', 'input', 'click'].forEach(function(ev){
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

  // ── 아래부터는 페이지의 기능을 덮어쓰지 않는다 ──
  // ★2026-10-31: 예전엔 speak·updateSpellStats 같은 페이지 기능을 같은 이름으로 다시 만들어 감쌌다(덧붙이기).
  //   지금은 버튼 누름(click)과 화면 변화를 옆에서 지켜보기만 한다. 페이지 기능은 한 벌 그대로다.

  function memSnapshot(){
    var o = {};
    try { for (var i = 0; i < localStorage.length; i++) { var k = localStorage.key(i); if (k && k.indexOf('memv_') === 0) o[k] = ls(k) || '[]'; } } catch(e){}
    return o;
  }
  function memDiff(before){
    var after = memSnapshot(), keys = {};
    for (var k in before) keys[k] = 1;
    for (var k2 in after) keys[k2] = 1;
    Object.keys(keys).forEach(function(k){
      if ((before[k] || '[]') === (after[k] || '[]')) return;
      var from = k === 'memv_opic' ? 'opic' : k === 'memv_jenny' ? 'jenny' : null;
      var b = [], a = [];
      try { b = JSON.parse(before[k] || '[]') || []; a = JSON.parse(after[k] || '[]') || []; } catch(e){ return; }
      var B = {}, A = {};
      b.forEach(function(x){ B[x] = 1; }); a.forEach(function(x){ A[x] = 1; });
      var plus = a.filter(function(x){ return !B[x]; }), minus = b.filter(function(x){ return !A[x]; });
      if (plus.length + minus.length <= 10) {
        plus.forEach(function(x){ add('mem', wordOf(x, from), 1); });
        minus.forEach(function(x){ add('unmem', wordOf(x, from), 1); });
      } else if (minus.length && !a.length) {
        add('unmem', '외움 표시 모두 지움', minus.length);
      }
    });
  }

  // ── 발음 들은 단어(손으로 단어 하나를 눌렀을 때만) ──
  var lastSay = {};
  function say(word){
    var w = (word || '').trim(); if (!w) return;
    var now = Date.now();
    if (lastSay[w] && now - lastSay[w] < 1500) return;
    lastSay[w] = now;
    add('say', w, 1);
  }
  function argOf(oc, fn){
    var m = oc.match(new RegExp(fn + "\\(\\s*(['\"]?)(.*?)\\1\\s*[,)]"));
    return m ? m[2] : null;
  }
  function qText(qi){
    var c = document.getElementById('q-card-' + qi);
    var t = c && c.querySelector('.q-text');
    return t ? t.textContent.replace(/\s+/g, ' ').trim() : ('문제 ' + (parseInt(qi, 10) + 1));
  }
  function spellName(){
    try { var c = (typeof spellState !== 'undefined' && spellState) ? spellState.current : null; return c ? c.en + (c.ko ? ' · ' + c.ko : '') : ''; } catch(e){ return ''; }
  }

  // 버튼을 누르는 순간(페이지 기능이 돌기 전)과 돈 뒤를 본다
  document.addEventListener('click', function(e){
    var el = e.target && e.target.closest ? e.target.closest('[onclick]') : null;
    var oc = el ? (el.getAttribute('onclick') || '') : '';
    var before = memSnapshot();
    var v;
    if ((v = argOf(oc, 'speak')) !== null) say(wordOf(slug(v)));
    else if ((v = oc.match(/new Audio\(['"]audio\/sci\/([^'"]+)\.mp3['"]\)/))) say(wordOf(v[1]));
    else if (/playClip\(\s*['"]w['"]/.test(oc) && (v = oc.match(/playClip\([^,]+,\s*(\d+)/))) say(wordOf(v[1], 'jenny'));
    else if ((v = argOf(oc, 'opPlay')) !== null) say(wordOf(v, 'opic'));
    else if ((v = argOf(oc, 'showModel')) !== null) {
      var c = document.getElementById('q-card-' + v), ta = c && c.querySelector('textarea');
      add('quiz', qText(v), ta ? ta.value.trim().length : null);
    }
    else if ((v = argOf(oc, 'rateSelf')) !== null) add('rate', qText(v) + ' ⇒ ' + (el.textContent || '').trim(), null);
    else if (/^\s*showAnswer\(/.test(oc)) {
      try { if (typeof spellState !== 'undefined' && spellState && spellState.current && !spellState.revealed) add('spell', spellName(), -1); } catch(err){}
    }
    else if (/^\s*answerQuiz\(/.test(oc)) {
      var q0 = null;
      try { if (typeof quiz !== 'undefined' && quiz && !quiz.answered && quiz.cur) q0 = { ok: quiz.ok, cur: quiz.cur }; } catch(err){}
      if (q0) setTimeout(function(){
        try { var d = q0.cur; add('pick', (d.hz || d.en || '') + (d.py ? ' (' + d.py + ')' : '') + (d.ko ? ' · ' + d.ko : ''), quiz.ok > q0.ok ? 1 : 0); } catch(err){}
      }, 0);
    }
    setTimeout(function(){ memDiff(before); }, 0);
  }, true);

  // ── 단어시험: 맞음·틀림 숫자 칸이 바뀌는 것을 본다 ──
  ['sp-correct', 'sp-wrong'].forEach(function(id){
    var box = document.getElementById(id);
    if (!box || !window.MutationObserver) return;
    var prev = parseInt(box.textContent, 10) || 0;
    new MutationObserver(function(){
      var now = parseInt(box.textContent, 10) || 0;
      if (now > prev) add('spell', spellName(), id === 'sp-correct' ? 1 : 0);
      prev = now;
    }).observe(box, { childList: true, characterData: true, subtree: true });
  });

  // ── 듣기 시간 ──
  // 합친 mp3(전체 _all · 부분 _pN)는 화면에 있는 재생기(allplay-audio)를 지켜본다(화면이 꺼져도 센다).
  var ap = document.getElementById('allplay-audio');
  if (ap) {
    var st = { t: null, label: null };
    var label = function(){
      var src = decodeURIComponent((ap.currentSrc || ap.src || '').split('?')[0]), m;
      if (/_all\.mp3$/.test(src)) return '전체 듣기';
      if ((m = src.match(/_p(\d+)\.mp3$/))) return '부분 듣기 ' + m[1];
      return null;
    };
    var stop = function(){
      if (st.t == null) return;
      var sec = (Date.now() - st.t) / 1000; st.t = null;
      if (sec >= 3) { add('listen', st.label, sec); flush(); }
    };
    ap.addEventListener('playing', function(){
      var l = label();
      if (st.t != null && l === st.label) return;   // 끊겼다 다시 나온 같은 소리는 이어서 센다
      stop(); st.label = l; st.t = l ? Date.now() : null;
    });
    ['pause', 'ended', 'emptied', 'abort', 'error'].forEach(function(ev){ ap.addEventListener(ev, stop); });
    window.addEventListener('pagehide', stop);
  }
  // 낱개 발음 이어 듣기(외운 단어가 있을 때)는 듣기를 맡은 listen.js 가 끝날 때 알려 준다.
  window.amyLogListen = function(label, sec){ if (sec >= 3) { add('listen', label, sec); flush(); } };

  flush();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
