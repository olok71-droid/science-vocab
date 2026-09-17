#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""단어 20개씩 끊어 듣기 버튼 + 음성 겹침 버그 수정 (대표님 지시 2026-09-17).

고치는 것 셋:
 1) '전체 듣기' 옆에 1~20 / 21~40 … 토막 버튼을 넣는다. 토막도 미리 합쳐 둔 mp3라
    화면을 꺼도 계속 나온다(JS 순차재생은 아이폰에서 멈춘다 — 2026-08-28 확인).
 2) 전체·토막이 오디오 요소 하나(allplay-audio)를 같이 쓴다 → 소리가 겹칠 수 없다.
 3) 순차재생(playList·playFileSeq)의 '두 번 진행' 버그를 막는다.
    onended / onerror / play().catch() 가 같은 함수를 가리켜, 파일이 없으면
    두 갈래가 동시에 흘러 목소리가 겹쳤다. done 플래그로 한 번만 넘어가게 한다.
"""
import re, os, sys, glob, math

HERE = os.path.dirname(os.path.abspath(__file__))
CHUNK = 20

def ranges(n):
    """단어 n개를 20개씩 끊은 구간 [(시작,끝)...]. 1-based, 끝 포함.
       ★자투리가 5개 이하로 남으면 앞 토막에 붙인다(1개짜리 토막 방지).
       ★25개 이하 단원은 쪼갤 이유가 없어 빈 목록을 돌려준다(전체 듣기만 둔다)."""
    if n <= 25:
        return []
    out, i = [], 0
    while i < n:
        j = min(i + CHUNK, n)
        if n - j <= 5:
            j = n
        out.append((i + 1, j))
        i = j
    return out


NEW_ALL = r'''/* 단원 전체 듣기 + 20개씩 끊어 듣기 — 미리 합쳐 둔 mp3를 재생한다.
   ★JS로 곡을 넘기는 방식은 아이폰 화면이 꺼지면 멈춘다(애플 확인). 그래서 파일로 합쳤다.
   ★2026-09-17 대표님 지시: 한 번에 60몇 개는 안 외워진다 → 20개 토막 버튼 추가.
     전체와 토막이 audio 요소 하나를 같이 쓴다 → 두 소리가 겹칠 수 없다. */
(function(){
  var a = document.getElementById('allplay-audio');
  var btn = document.getElementById('allplay-btn');
  if (!a || !btn) return;
  var FULL = a.getAttribute('src');
  var TOTAL = btn.getAttribute('data-total') || '';
  var cur = 0;   // 0 = 전체, 1.. = 몇 번째 토막
  function parts(){ return Array.prototype.slice.call(document.querySelectorAll('.chunkplay')); }
  function resetLabels(){
    btn.textContent = '▶ 전체 듣기'; btn.classList.remove('active');
    parts().forEach(function(b){ b.textContent = b.getAttribute('data-label'); b.classList.remove('active'); });
  }
  function activeBtn(){
    return cur === 0 ? btn : document.querySelector('.chunkplay[data-part="' + cur + '"]');
  }
  function mmss(s){ s = Math.max(0, Math.floor(s||0)); return Math.floor(s/60)+':'+String(s%60).padStart(2,'0'); }
  function playSrc(src, which, title){
    if (typeof stopSeq === 'function') stopSeq();
    if (typeof window.stopVisibleSeq === 'function') window.stopVisibleSeq();
    if (a.getAttribute('src') !== src) { a.pause(); a.setAttribute('src', src); a.load(); }
    cur = which;
    try { a.currentTime = 0; } catch (e) {}   // 끝까지 들은 뒤 다시 눌러도 처음부터
    a._title = title;
    a.play();
  }
  window.playAllFrom = function(n, label){
    var b = document.querySelector('.chunkplay[data-part="' + n + '"]');
    if (cur === n && !a.paused) { a.pause(); return; }
    playSrc(FULL.replace('_all.mp3', '_p' + n + '.mp3'), n, (b ? b.getAttribute('data-label').replace('▶ ','') : n + '번째') + ' 듣기');
  };
  window.toggleAllPlay = function(){
    if (cur === 0 && !a.paused) { a.pause(); return; }
    playSrc(FULL, 0, '단원 전체 듣기' + (TOTAL ? ' — ' + TOTAL + ' 단어' : ''));
  };
  a.addEventListener('play', function(){
    resetLabels();
    var b = activeBtn(); if (b) { b.textContent = '⏸ 멈춤'; b.classList.add('active'); }
    if ('mediaSession' in navigator) {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: a._title || '단원 전체 듣기', artist: UNIT_TITLE, album: 'AMY Study App'
      });
      navigator.mediaSession.setActionHandler('play',  function(){ a.play(); });
      navigator.mediaSession.setActionHandler('pause', function(){ a.pause(); });
    }
  });
  a.addEventListener('pause', resetLabels);
  a.addEventListener('ended', resetLabels);
  a.addEventListener('timeupdate', function(){
    if (a.paused) return;
    var b = activeBtn(); if (b) b.textContent = '⏸ ' + mmss(a.currentTime);
  });
  a.addEventListener('error', function(){ resetLabels(); });
})();'''

# playFileSeq: onended·onerror·catch 가 done()을 여러 번 부르던 것을 한 번으로
OLD_SEQ = re.compile(r"function playFileSeq\(src, token, done\)\{.*?\n\}", re.S)
NEW_SEQ = r'''function playFileSeq(src, token, done){
  if (!_seq || _seq.token !== token) return;
  // ★2026-09-17: onended·onerror·play().catch() 가 모두 done()을 불러서 한 소리가
  //   두 갈래로 갈라져 재생되던 것(목소리 겹침)을 막는다. 무슨 일이 나도 딱 한 번만 넘어간다.
  var fired = false;
  var go = function(){ if (fired) return; fired = true; if (_seq && _seq.token === token) done(); };
  try {
    if (_audio) { _audio.pause(); _audio = null; }
    const a = new Audio(src);
    _audio = a;
    a.onended = go;
    a.onerror = go;                       // 파일 없으면 건너뜀
    const p = a.play();
    if (p && p.catch) p.catch(go);
  } catch (e) { go(); }
}'''

# 낱개 순차(외운단어 숨김 모드) 이중진행 수정
OLD_LIST = """      var ko = new Audio('audio/sci_ko/' + sl + '.mp3');
      cur = ko;
      ko.onended = ko.onerror = function(){
        if (seq !== token) return;
        var en = new Audio('audio/sci/' + sl + '.mp3');
        cur = en;
        en.onended = en.onerror = function(){ if (seq === token) { i++; setTimeout(next, 300); } };
        en.play().catch(function(){ if (seq === token) { i++; setTimeout(next, 300); } });
      };
      ko.play().catch(function(){ if (seq === token) ko.onended(); });"""
NEW_LIST = """      // ★2026-09-17: onended·onerror·play().catch() 가 같은 함수를 가리켜, 파일이 없으면
      //   한 단어에서 두 갈래가 동시에 흘러 목소리가 겹쳤다. 단계마다 딱 한 번만 넘어가게 막는다.
      var koDone = false, enDone = false;
      var ko = new Audio('audio/sci_ko/' + sl + '.mp3');
      cur = ko;
      var afterEn = function(){
        if (enDone) return; enDone = true;
        if (seq === token) { i++; setTimeout(next, 300); }
      };
      var afterKo = function(){
        if (koDone) return; koDone = true;
        if (seq !== token) return;
        var en = new Audio('audio/sci/' + sl + '.mp3');
        cur = en;
        en.onended = afterEn;
        en.onerror = afterEn;
        en.play().catch(afterEn);
      };
      ko.onended = afterKo;
      ko.onerror = afterKo;
      ko.play().catch(afterKo);"""

# stopSeq 가 낱개 순차까지 멈추게 (섹션 듣기 ↔ 전체 듣기 겹침 방지)
OLD_STOP = """function stopSeq(){
  if (_seq) _seq.token = -1;
  if (_audio) { _audio.pause(); _audio = null; }"""
NEW_STOP = """function stopSeq(){
  if (_seq) _seq.token = -1;
  if (_audio) { _audio.pause(); _audio = null; }
  // ★2026-09-17: 낱개 순차재생(외운단어 숨김 모드 전체듣기)은 _audio 를 안 쓴다.
  //   여기서 같이 멈추지 않으면 섹션 듣기와 두 소리가 겹친다."""

# 카드 🔊 를 누르면 돌던 재생을 멈춘다(겹침 방지)
OLD_SPEAK = """function speak(text) {
  try {
    if (_audio) { _audio.pause(); _audio = null; }"""
NEW_SPEAK = """function speak(text) {
  try {
    // ★2026-09-17: 전체듣기·토막듣기·낱개순차가 돌고 있으면 먼저 멈춘다. 안 그러면 소리가 겹친다.
    var _ap = document.getElementById('allplay-audio');
    if (_ap && !_ap.paused) _ap.pause();
    if (typeof window.stopVisibleSeq === 'function') window.stopVisibleSeq();
    if (_audio) { _audio.pause(); _audio = null; }"""


def slug(t):
    t = re.sub(r'<[^>]+>', '', t).strip().replace('~', '').replace('/', ' ').lower()
    return re.sub(r'[^a-z0-9]+', '_', t).strip('_')


def patch(page):
    s0 = open(page, encoding='utf-8').read()
    if 'allplay-audio' not in s0:
        return None
    s = s0
    notes = []

    n = len(re.findall(r'class="vcard-en"', s))
    rs = ranges(n)            # make_chunk_audio.py 와 똑같은 규칙이어야 한다
    nchunk = len(rs)

    # ① 토막 버튼 — audio 태그 바로 뒤에
    if nchunk and 'chunkplay' not in s:
        btns = ''
        for k, (a1, b1) in enumerate(rs):
            lab = '▶ %d~%d' % (a1, b1)
            btns += ('<button class="blind-btn chunkplay" data-part="%d" data-label="%s" '
                     'title="%d~%d번 단어만 듣기" onclick="playAllFrom(%d)">%s</button>'
                     % (k + 1, lab, a1, b1, k + 1, lab))
        s, c = re.subn(r'(<audio id="allplay-audio"[^>]*></audio>)', r'\1' + btns, s, count=1)
        if c: notes.append('토막버튼 %d개' % nchunk)

    # 단어 수를 버튼에 심어 둔다(잠금화면 제목용)
    if 'data-total=' not in s:
        s = s.replace('id="allplay-btn"', 'id="allplay-btn" data-total="%d"' % n, 1)

    # ② 전체듣기 블록 교체
    s2, c = re.subn(r"/\* 단원 전체 듣기.*?\n\}\)\(\);", lambda m: NEW_ALL, s, count=1, flags=re.S)
    if c: s, _ = s2, notes.append('전체듣기 교체')

    # ③ 버그 수정 셋
    s2, c = OLD_SEQ.subn(lambda m: NEW_SEQ, s, count=1)
    if c: s, _ = s2, notes.append('playFileSeq')
    if OLD_LIST in s: s = s.replace(OLD_LIST, NEW_LIST, 1); notes.append('낱개순차')
    if OLD_STOP in s: s = s.replace(OLD_STOP, NEW_STOP, 1); notes.append('stopSeq')
    if OLD_SPEAK in s: s = s.replace(OLD_SPEAK, NEW_SPEAK, 1); notes.append('speak')

    if s != s0:
        open(page, 'w', encoding='utf-8').write(s)
    return (n, nchunk, notes)


if __name__ == '__main__':
    for page in (sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, '*.html')))):
        r = patch(page)
        if r:
            print('%-26s 단어 %-4d 토막 %d  |  %s' % (os.path.basename(page), r[0], r[1], ', '.join(r[2]) or '변경없음'))
