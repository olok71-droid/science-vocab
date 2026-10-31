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


# 전체듣기·토막듣기·외운단어 빼기 코드는 listen.js 한 곳에 있다(2026-10-31, 페이지마다 두 벌이던 것을 합침).
LISTEN_TAG = '<script src="listen.js"></script>'
OLD_ALL = re.compile(r"<script>\s*/\* 단원 전체 듣기 \+ 20개씩.*?</script>\n?", re.S)
OLD_MEM = re.compile(r"<script>\s*/\* ★2026-09-26 대표님 지시: '외운 단어'.*?</script>\n?", re.S)

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

    # ① 토막 버튼 — 이 페이지 단어 수로 늘 다시 만든다(다른 페이지 틀에서 복사된 버튼이 남지 않게)
    s = re.sub(r'<button class="blind-btn chunkplay"[^>]*>[^<]*</button>', '', s)
    btns = ''
    for k, (a1, b1) in enumerate(rs):
        lab = '▶ %d~%d' % (a1, b1)
        btns += ('<button class="blind-btn chunkplay" data-part="%d" data-label="%s" '
                 'title="%d~%d번 단어만 듣기" onclick="playAllFrom(%d)">%s</button>'
                 % (k + 1, lab, a1, b1, k + 1, lab))
    if btns:
        s = re.sub(r'(<audio id="allplay-audio"[^>]*></audio>)', lambda m: m.group(1) + btns, s, count=1)
    notes.append('토막버튼 %d개' % nchunk)

    # 단어 수를 버튼에 심어 둔다(잠금화면 제목용)
    if 'data-total=' not in s:
        s = s.replace('id="allplay-btn"', 'id="allplay-btn" data-total="%d"' % n, 1)
    else:
        s = re.sub(r'data-total="\d+"', 'data-total="%d"' % n, s, count=1)

    # ② 듣기 코드는 listen.js 하나 — 페이지 안의 옛 두 벌이 있으면 지우고 그 자리에 태그 하나
    if LISTEN_TAG not in s:
        m = OLD_ALL.search(s) or OLD_MEM.search(s)
        pos = m.start() if m else s.rfind('<script src="studylog.js"></script>')
        if pos < 0: pos = s.rfind('</body>')
        s = s[:pos] + LISTEN_TAG + '\n' + s[pos:]
    s = OLD_ALL.sub('', s); s = OLD_MEM.sub('', s)
    if s.count('window.toggleAllPlay = function'):
        raise RuntimeError(os.path.basename(page) + ': 듣기 코드가 페이지 안에 남아 있다(두 벌 금지)')

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
