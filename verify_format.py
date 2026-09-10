#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""과목 페이지가 유전 단원과 같은 형식인지 검사한다. 형식 정의 = 과목페이지_형식.md

'자료 몇 개 들어갔나'만 세다가 2026-09-09에 반쪽짜리 페이지를 두 주 동안 못 봤다. 그래서
탭 4개·단어장·퀴즈·단어시험이 실제로 있는지 과목마다 본다. 화면에 '자료 없다'고 적어 놓고
자료가 들어와 있는 거짓말도 여기서 잡는다.
"""
import os, re, sys, glob

APP = os.path.dirname(os.path.abspath(__file__))
TABS = ["vocab", "files", "quiz", "spelling"]
bad = 0

pages = sorted(glob.glob(os.path.join(APP, "y9c_*.html"))) + [os.path.join(APP, "y9_genes.html")]
for p in pages:
    s = open(p, encoding="utf-8").read()
    name = os.path.basename(p)
    problems = []
    for t in TABS:
        if f'id="tab-{t}"' not in s:
            problems.append(f"{t} 탭 없음")
    n_vocab = len(re.findall(r'class="vcard"', s))
    n_quiz = len(re.findall(r'class="q-card"', s))
    n_files = len(re.findall(r'class="mat-title"', s))
    if n_files and not n_quiz:
        problems.append("자료는 있는데 퀴즈가 없다")
    if not n_files:
        # 아직 클래스룸에서 자료를 못 받은 과목 (로그인 만료 등). 형식 미달로 세지 않는다.
        print(f"⏳ {name}: 아직 자료가 없다 (클래스룸에서 못 받음)")
        continue
    if not n_vocab:
        print(f"⚠️ {name}: 자료 {n_files} · 단어 0 (자료에 단어로 뽑을 내용이 없다) · 퀴즈 {n_quiz}")
        continue
    if problems:
        bad += 1
        print(f"❌ {name}: " + " · ".join(problems))
    else:
        print(f"✅ {name}: 자료 {n_files} · 단어 {n_vocab} · 퀴즈 {n_quiz}")

# 홈에 박아 둔 '자료 없다' 문구가 거짓말인지 본다
idx = open(os.path.join(APP, "index.html"), encoding="utf-8").read()
if "자료는 아직 없다" in idx or "자료가 아직 없다" in idx:
    print("❌ index.html: '자료 없다' 문구가 글자로 박혀 있다. 자료가 들어오면 거짓말이 된다.")
    bad += 1

print(("\n문제 없음" if not bad else f"\n문제 {bad}건"))
sys.exit(1 if bad else 0)
