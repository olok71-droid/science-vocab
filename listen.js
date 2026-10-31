/* 단어장 '전체 듣기' + '20개씩 끊어 듣기' — 단원 페이지가 모두 이 파일 하나를 쓴다.
   ★2026-10-31: 예전엔 페이지마다 같은 이름의 코드가 두 벌(합친 mp3 재생 / 외운 단어 빼기) 있었고,
     뒤에 놓인 쪽이 앞의 것을 덮어써서 순서가 바뀐 페이지(수학 5~8단원)는 외운 단어까지 들렸다.
     두 벌을 지우고 이 한 곳으로 합쳤다. 고칠 때는 이 파일을 고친다(페이지에 코드를 더 붙이지 않는다).

   - 외운 단어가 없으면: 미리 합쳐 둔 mp3(audio/<단원>_all.mp3, _pN.mp3)를 튼다.
     JS로 곡을 넘기는 방식은 아이폰 화면이 꺼지면 멈춘다(애플 확인) → 합친 파일이라 화면을 꺼도 계속 나온다.
   - ★2026-09-26 대표님 지시: '외운 단어'로 체크한 것은 전체 듣기·부분 듣기에서 들리지 않는다.
     합친 mp3는 통짜라 중간을 건너뛸 수 없다 → 외운 단어가 하나라도 있으면 그 단원(또는 그 토막)은
     낱개 발음(한국어 → 영어)을 이어서 들려준다(이때는 화면을 끄면 멈춘다).
   - ★2026-09-17 대표님 지시: 한 번에 60몇 개는 안 외워진다 → 20개 토막 버튼.
     전체와 토막이 audio 요소 하나를 같이 쓴다 → 두 소리가 겹칠 수 없다. */
(function(){
  var a = document.getElementById('allplay-audio');
  var btn = document.getElementById('allplay-btn');
  if (!a || !btn) return;
  var FULL = a.getAttribute('src');
  var TOTAL = btn.getAttribute('data-total') || '';
  var TITLE = (typeof UNIT_TITLE !== 'undefined') ? UNIT_TITLE : (document.title || '');
  var cur = 0;   // 합친 mp3: 0 = 전체, 1.. = 몇 번째 토막

  function parts(){ return Array.prototype.slice.call(document.querySelectorAll('.chunkplay')); }
  function chunkBtn(n){ return document.querySelector('.chunkplay[data-part="' + n + '"]'); }
  function labelOf(b){ return b === btn ? '▶ 전체 듣기' : (b.getAttribute('data-label') || '▶'); }
  function resetLabels(){
    btn.textContent = '▶ 전체 듣기'; btn.classList.remove('active');
    parts().forEach(function(b){ b.textContent = b.getAttribute('data-label'); b.classList.remove('active'); });
  }
  function activeBtn(){ return cur === 0 ? btn : chunkBtn(cur); }
  function mmss(s){ s = Math.max(0, Math.floor(s||0)); return Math.floor(s/60)+':'+String(s%60).padStart(2,'0'); }

  /* ── 낱개 발음 이어 듣기(외운 단어가 있을 때) ── */
  var seq = null, seqAudio = null, seqBtn = null, seqStart = 0;
  function slug(t){ return (t||'').replace(/~/g,'').replace(/\//g,' ').toLowerCase().replace(/[^a-z0-9]+/g,'_').replace(/^_+|_+$/g,''); }
  function stopList(){
    if (seqAudio) { try { seqAudio.pause(); } catch(e){} seqAudio = null; }
    if (seq && typeof window.amyLogListen === 'function') window.amyLogListen('이어 듣기', (Date.now() - seqStart) / 1000);   // 공부기록
    seq = null;
    if (seqBtn) { seqBtn.textContent = labelOf(seqBtn); seqBtn.classList.remove('active'); seqBtn = null; }
  }
  window.stopVisibleSeq = stopList;
  function playList(words, b){
    var i = 0, token = {};
    seq = token; seqBtn = b; seqStart = Date.now();
    b.textContent = '⏸ 멈춤'; b.classList.add('active');
    (function next(){
      if (seq !== token) return;
      if (i >= words.length) { stopList(); return; }   // 끝나면 멈춘다
      var sl = slug(words[i]);
      var koDone = false, enDone = false;
      var ko = new Audio('audio/sci_ko/' + sl + '.mp3');
      seqAudio = ko;
      var afterEn = function(){
        if (enDone) return; enDone = true;
        if (seq === token) { i++; next(); }
      };
      var afterKo = function(){
        if (koDone) return; koDone = true;
        if (seq !== token) return;
        var en = new Audio('audio/sci/' + sl + '.mp3');
        seqAudio = en;
        en.onended = afterEn; en.onerror = afterEn;
        en.play().catch(afterEn);
      };
      ko.onended = afterKo; ko.onerror = afterKo;
      ko.play().catch(afterKo);
    })();
  }
  /* 토막 버튼 라벨('1~20')에서 몇 번째~몇 번째 단어인지 읽는다 */
  function rangeOf(b){
    var m = (b && b.getAttribute('data-label') || '').match(/(\d+)\s*~\s*(\d+)/);
    return m ? [parseInt(m[1],10), parseInt(m[2],10)] : null;
  }
  /* 그 범위에서 외운 단어를 뺀 영어 단어 목록과 외운 단어 수 (1-based, 범위 없으면 전체) */
  function pick(rg){
    var all = Array.prototype.slice.call(document.querySelectorAll('#tab-vocab .vcard'));
    var part = rg ? all.slice(rg[0] - 1, rg[1]) : all;
    var out = [], mem = 0;
    part.forEach(function(c){
      if (c.classList.contains('hidden')) return;
      if (c.classList.contains('memorized')) { mem++; return; }
      var e = c.querySelector('.vcard-en'), en = e ? (e.textContent||'').trim() : '';
      if (en) out.push(en);
    });
    return { words: out, mem: mem };
  }

  /* ── 합친 mp3 재생 ── */
  function playSrc(src, which, title){
    if (typeof stopSeq === 'function') stopSeq();
    stopList();
    if (a.getAttribute('src') !== src) { a.pause(); a.setAttribute('src', src); a.load(); }
    cur = which;
    try { a.currentTime = 0; } catch (e) {}   // 끝까지 들은 뒤 다시 눌러도 처음부터
    a._title = title;
    a.play();
  }

  /* 버튼 하나(전체 = 0, 토막 = n)를 눌렀을 때 */
  function press(n){
    var b = n === 0 ? btn : chunkBtn(n);
    if (seq && seqBtn === b) { stopList(); return; }           // 이어 듣기 중 같은 버튼 → 멈춤
    if (cur === n && !a.paused && !seq) { a.pause(); return; } // 합친 mp3 재생 중 같은 버튼 → 멈춤
    stopList();
    var r = pick(n === 0 ? null : rangeOf(b));
    if (r.mem) {                                                // 외운 단어가 있다 → 낱개로 빼고 듣기
      if (!a.paused) a.pause();
      if (r.words.length && b) playList(r.words, b);
      return;
    }
    if (n === 0) playSrc(FULL, 0, '단원 전체 듣기' + (TOTAL ? ' — ' + TOTAL + ' 단어' : ''));
    else playSrc(FULL.replace('_all.mp3', '_p' + n + '.mp3'), n, (b ? b.getAttribute('data-label').replace('▶ ','') : n + '번째') + ' 듣기');
  }
  window.toggleAllPlay = function(){ press(0); };
  window.playAllFrom = function(n){ press(n); };

  a.addEventListener('play', function(){
    resetLabels();
    var b = activeBtn(); if (b) { b.textContent = '⏸ 멈춤'; b.classList.add('active'); }
    if ('mediaSession' in navigator) {
      try {
        navigator.mediaSession.metadata = new MediaMetadata({ title: a._title || '단원 전체 듣기', artist: TITLE, album: 'AMY Study App' });
        navigator.mediaSession.setActionHandler('play',  function(){ a.play(); });
        navigator.mediaSession.setActionHandler('pause', function(){ a.pause(); });
      } catch (e) {}
    }
  });
  a.addEventListener('pause', resetLabels);
  a.addEventListener('ended', resetLabels);
  a.addEventListener('timeupdate', function(){
    if (a.paused) return;
    var b = activeBtn(); if (b) b.textContent = '⏸ ' + mmss(a.currentTime);
  });
  a.addEventListener('error', function(){ resetLabels(); });
})();
