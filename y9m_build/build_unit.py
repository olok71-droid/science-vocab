# -*- coding: utf-8 -*-
"""y9m_unitN.html 의 빈 단어장·핵심노트를 채운다. 사용: python3 build_unit.py 3"""
import sys, re, os, html, time, urllib.parse, urllib.request
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
HERE = os.path.expanduser('~/science-vocab-fresh')
N = sys.argv[1]
VOCAB = __import__('vocab%s' % N).VOCAB
CATS  = __import__('vocab%s' % N).CATS
NOTES = __import__('notes%s' % N).NOTES
UNIT = 'y9m_unit%s' % N
PAGE = os.path.join(HERE, UNIT + '.html')

def slug(t):
    t = re.sub(r'<[^>]+>', '', t).strip().replace('~', '').replace('/', ' ').lower()
    return re.sub(r'[^a-z0-9]+', '_', t).strip('_')
def esc(s): return html.escape(s, quote=False)
def ranges(n):
    if n <= 25: return []
    out, i = [], 0
    while i < n:
        j = min(i + 20, n)
        if n - j <= 5: j = n
        out.append((i + 1, j)); i = j
    return out

# 1) 발음 mp3
def fetch(text, lang, out):
    url = 'https://translate.google.com/translate_tts?ie=UTF-8&tl=%s&client=tw-ob&q=%s' % (lang, urllib.parse.quote(text))
    req = urllib.request.Request(url, headers={'Referer': 'https://translate.google.com/', 'User-Agent': 'Mozilla/5.0'})
    d = urllib.request.urlopen(req, timeout=20).read()
    if len(d) < 800: raise RuntimeError('too small %d' % len(d))
    open(out, 'wb').write(d)
got = 0
for en, ko, de, dk, c in VOCAB:
    s = slug(en)
    for d, txt, lang in (('sci', en, 'en-GB'), ('sci_ko', ko, 'ko')):
        p = os.path.join(HERE, 'audio', d, s + '.mp3')
        if os.path.exists(p): continue
        fetch(txt, lang, p); got += 1; time.sleep(0.35)
print('발음 새로 받음 %d개' % got)

# 2) 단어장 pane
n = len(VOCAB); rs = ranges(n)
chunks = ''.join('<button class="blind-btn chunkplay" data-part="%d" data-label="▶ %d~%d" title="%d~%d번 단어만 듣기" onclick="playAllFrom(%d)">▶ %d~%d</button>'
                 % (i+1, a, b, a, b, i+1, a, b) for i, (a, b) in enumerate(rs))
vtool = ('<div class="vtool">'
 '<input class="search-input" id="vocab-search" type="search" placeholder="🔍 검색 (영어 또는 한국어)" autocomplete="off">'
 '<button class="blind-btn" id="mem-hide-btn" onclick="toggleHideMem()">외운 단어 숨기기</button>'
 '<span class="mem-info">총 <b id="total-count">0</b>단어 · 외운 단어 <b id="mem-count">0</b>개</span>'
 '<button class="blind-btn allplay-mini" id="allplay-btn" data-total="%d" onclick="toggleAllPlay()" title="%d개 단어 한 번에 듣기 — 화면을 꺼도 계속 재생">▶ 전체 듣기</button>'
 '<audio id="allplay-audio" preload="none" src="audio/%s_all.mp3"></audio>%s'
 '<button class="blind-btn" data-b="en" onclick="toggleBlind(\'en\')">🇬🇧 영어가림</button>'
 '<button class="blind-btn" data-b="ko" onclick="toggleBlind(\'ko\')">🇰🇷 한글가림</button>'
 '<button class="mem-toggle-btn" onclick="resetMem()">↺ 외움 초기화</button></div>') % (n, n, UNIT, chunks)
fb = '<button class="filter-btn active" data-cat="all" onclick=\'filterCards("all")\'>전체 All</button>' + \
     ''.join('<button class="filter-btn" data-cat="%s" onclick=\'filterCards("%s")\'>%s</button>' % (c, c, l) for c, l in CATS)
body = ''
for cat, lbl in CATS:
    body += '<div class="section-header" data-cat="%s"><h2>%s</h2><div class="section-line"></div></div>\n<div class="cards-wrap">\n' % (cat, lbl)
    for en, ko, de, dk, c in VOCAB:
        if c != cat: continue
        body += ('<div class="vcard" data-cat="%s">\n  <div class="vcard-left">\n'
                 '    <div class="vcard-en">%s</div>\n    <div class="vcard-ko">%s</div>\n'
                 '    <div class="vcard-def">%s</div>\n    <div class="vcard-def-ko">%s</div>\n  </div>\n'
                 '  <div class="vcard-right">\n    <button class="btn-speak" onclick=\'speak("%s")\'>🔊</button>\n'
                 '    <button class="btn-mem" onclick="toggleMem(this)" title="외웠으면 체크 (전체듣기에서 빠짐)">🧠</button>\n'
                 '  </div>\n</div>\n') % (cat, esc(en), esc(ko), esc(de), dk, en.replace('"', ''))
    body += '</div>\n'
vocab_pane = ('<div class="tab-pane active" id="tab-vocab">\n%s\n  <div class="filter-wrap">\n    <div class="filter-tabs">\n      %s\n    </div>\n  </div>\n%s</div>' % (vtool, fb, body))

notes = '<div class="tab-pane" id="tab-notes">\n'
for icon, title, sub, cards in NOTES:
    notes += ('<div class="chapter-block">\n  <div class="chapter-head">\n    <span class="ch-icon">%s</span>\n'
              '    <div class="ch-text">\n      <h2>%s</h2>\n      <span class="ch-sub">%s</span>\n    </div>\n  </div>\n  <div class="notes-list">' % (icon, esc(title), esc(sub)))
    for h3, bd in cards:
        notes += '<div class="note-card">\n  <div class="note-head">\n    <h3>%s</h3>\n  </div>\n  <div class="note-body">%s</div>\n</div>\n' % (esc(h3), bd)
    notes += '</div>\n</div>\n'
notes += '</div>'

src = open(PAGE, encoding='utf-8').read()
assert '<div class="tab-pane" id="tab-vocab"></div>' in src, '이미 채워져 있다'
src = src.replace('<div class="tab-pane" id="tab-vocab"></div>', vocab_pane)
src = src.replace('<div class="tab-pane" id="tab-notes"></div>', notes)
src = src.replace('<button class="tab-btn active" data-tab="teacher">', '<button class="tab-btn" data-tab="teacher">')
src = src.replace('<button class="tab-btn" data-tab="vocab">', '<button class="tab-btn active" data-tab="vocab">')
src = src.replace('<div class="tab-pane active" id="tab-teacher">', '<div class="tab-pane" id="tab-teacher">')
CSS = """.vtool { max-width: 720px; margin: 0 auto 10px; padding: 0 16px; display: flex; flex-wrap: wrap;
  align-items: center; gap: 6px; }
.vtool .search-input { flex: 0 1 48%; max-width: 48%; min-width: 0; padding: 8px 12px; font-size: 13px; }
.vtool .mem-info { font-size: 12px; font-weight: 800; color: var(--strong, #16223f); white-space: nowrap; }
.vtool .mem-info b { color: #0b4f45; font-weight: 900; }
.vtool .blind-btn, .vtool .mem-toggle-btn { padding: 5px 10px; color: #0d5c50; border-color: rgba(13,92,80,0.55); background: rgba(255,255,255,0.85); font-weight: 900; }
.vtool .blind-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }
.vtool .allplay-mini { background: var(--accent); border-color: var(--accent); color: #fff; }
</style>"""
i = src.rindex('</style>'); src = src[:i] + CSS + src[i+len('</style>'):]
src = src.replace("    window.scrollTo({top:0, behavior:'smooth'});\n",
                  "    window.scrollTo({top:0, behavior:'smooth'});\n    if (typeof stopSeq === 'function') stopSeq();\n")
js = '<script>\nconst UNIT_ID = "%s";\n%s\n</script>\n<script>\n%s\n</script>\n' % (
    UNIT, open(os.path.join(SP,'vocabjs.txt'),encoding='utf-8').read(), open(os.path.join(SP,'chunkjs.txt'),encoding='utf-8').read())
src = src.replace('</body>', js + '</body>')
open(PAGE, 'w', encoding='utf-8').write(src)

# 3) 합본 + 토막 mp3
ws = [slug(e) for e in re.findall(r'class="vcard-en"[^>]*>(.*?)<', src, re.S)]
buf = b''
for s in ws:
    for d in ('sci_ko', 'sci'):
        buf += open(os.path.join(HERE,'audio',d,s+'.mp3'),'rb').read()
open(os.path.join(HERE,'audio',UNIT+'_all.mp3'),'wb').write(buf)
tot = 0
for ci,(a,b) in enumerate(rs):
    pb = b''
    for s in ws[a-1:b]:
        for d in ('sci_ko','sci'):
            pb += open(os.path.join(HERE,'audio',d,s+'.mp3'),'rb').read()
    open(os.path.join(HERE,'audio','%s_p%d.mp3'%(UNIT,ci+1)),'wb').write(pb); tot += len(pb)
print('단어 %d개 · 노트 %d블록 %d카드 · 토막 %d개' % (n, len(NOTES), sum(len(x[3]) for x in NOTES), len(rs)))
print('무결성: 전체 %d == 토막합계 %d → %s' % (len(buf), tot, '통과' if len(buf)==tot else '★불일치'))
