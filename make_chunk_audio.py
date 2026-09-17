#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""단어 20개씩 끊어 듣기용 mp3 만들기 (대표님 지시 2026-09-17).
   서정이가 "한 번에 60몇 개는 안 외워진다"고 해서 20개 단위로 쪼갠다.

   ★기존 <단원>_all.mp3 는 audio/sci_ko/<slug>.mp3 + audio/sci/<slug>.mp3 를
     카드 순서대로 '그냥 이어붙인' 파일이다(2026-09-17 바이트 단위로 확인, 차이 0).
     여기서도 같은 방식으로 20단어씩 묶어 <단원>_p1.mp3, _p2.mp3 ... 를 만든다.
   ★JS로 곡을 넘기면 아이폰 화면이 꺼질 때 멈춘다(2026-08-28 확인) → 파일로 합치는 방식 유지.
"""
import re, os, sys, glob

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



def slug(t):
    t = re.sub(r'<[^>]+>', '', t).strip()
    t = t.replace('~', '').replace('/', ' ').lower()
    return re.sub(r'[^a-z0-9]+', '_', t).strip('_')


def words_of(html):
    return [slug(e) for e in re.findall(r'class="vcard-en"[^>]*>(.*?)<', html, re.S)]


def unit_of(html):
    m = re.search(r'id="allplay-audio"[^>]*src="audio/([A-Za-z0-9_]+)_all\.mp3"', html)
    return m.group(1) if m else None


def build(page, write=True):
    html = open(page, encoding='utf-8').read()
    unit = unit_of(html)
    if not unit:
        return None
    ws = words_of(html)
    rs = ranges(len(ws))
    if not rs:
        return (unit, len(ws), 0, [], [])
    made, missing = [], []
    for ci, (a1, b1) in enumerate(rs):
        part = ws[a1 - 1:b1]
        buf = b''
        for s in part:
            for d in ('sci_ko', 'sci'):
                p = os.path.join(HERE, 'audio', d, s + '.mp3')
                if os.path.exists(p):
                    buf += open(p, 'rb').read()
                else:
                    missing.append(d + '/' + s)
        out = os.path.join(HERE, 'audio', '%s_p%d.mp3' % (unit, ci + 1))
        if write:
            open(out, 'wb').write(buf)
        made.append((os.path.basename(out), a1, b1, len(buf)))
    return (unit, len(ws), len(made), made, missing)


if __name__ == '__main__':
    targets = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, '*.html')))
    for page in targets:
        r = build(page)
        if not r:
            continue
        if r[2] == 0:
            print('%-26s %s 단어 %d개 — 25개 이하라 안 쪼갬' % (os.path.basename(page), r[0], r[1]))
            continue
        unit, n, k, made, missing = r
        print('%-26s %s 단어 %d개 → %d토막' % (os.path.basename(page), unit, n, k))
        for nm, a, b, sz in made:
            print('   %-22s %d~%d번  %s' % (nm, a, b, '{:,}'.format(sz) + ' bytes'))
        if missing:
            print('   ⚠️ 없는 클립 %d개: %s' % (len(missing), missing[:4]))
