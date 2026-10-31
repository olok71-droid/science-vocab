# -*- coding: utf-8 -*-
"""버튼이 부르는 함수가 실제로 있는지, JS가 찾는 id가 실제로 있는지 검사한다.
★2026-10-31: 같은 기능(window.X = function / function X)이 한 페이지에 두 벌 있으면 '두 벌'로 잡는다.
  고칠 때 원래 코드를 고치지 않고 새 코드를 덧붙이면 여기서 걸린다(대표님 규칙: 덧붙이지 말고 원래 것을 고친다).
  듣기 버튼이 트는 mp3(전체·토막)가 실제로 있는지도 본다.
사용: check_app.py           — 모든 문제를 보여 준다
      check_app.py --block   — '두 벌'·'없는 mp3'·'JS 문법 오류'가 하나라도 있으면 종료코드 1 (깃 커밋 전 검사가 쓴다)"""
import re, glob, os, sys, subprocess, tempfile, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BUILTIN={'window','document','alert','confirm','console','event'}
BLOCK={'두 벌','없는 mp3','JS 문법 오류'}
bad=[]
_js_cache={}
def local_js(s):
    """페이지가 불러 쓰는 맥 안의 .js 파일 내용(listen.js·studylog.js 등)"""
    out=[]
    for src in re.findall(r'<script[^>]*\bsrc="([^"]+\.js)"', s):
        if src.startswith('http') or not os.path.exists(src): continue
        if src not in _js_cache: _js_cache[src]=open(src,encoding='utf-8').read()
        out.append(_js_cache[src])
    return out
for f in sorted(glob.glob('*.html')):
    s=open(f,encoding='utf-8').read()
    inline='\n;\n'.join(re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', s, re.S))
    code_all=s+'\n'+'\n'.join(local_js(s))
    ids=set(re.findall(r'\bid="([^"]+)"', s))
    # 1) onclick / oninput 이 부르는 함수
    for m in re.finditer(r'on(?:click|input|change)="([^"]+)"', s):
        code=m.group(1)
        for fn in re.findall(r'(?<![.\w$])([A-Za-z_$][\w$]*)\s*\(', code):
            if fn in BUILTIN or fn in ('function','if','for','return','setTimeout','Audio'): continue
            if re.search(r'\bfunction\s+'+re.escape(fn)+r'\s*\(', code_all): continue
            if re.search(r'(?:window\.)?'+re.escape(fn)+r'\s*=\s*function', code_all): continue
            if re.search(r'\b(?:const|let|var)\s+'+re.escape(fn)+r'\s*=', code_all): continue
            bad.append((f,'없는 함수 호출',fn))
    # 2) getElementById 가 찾는 id
    for m in re.finditer(r"getElementById\(['\"]([^'\"]+)['\"]\)", s):
        if m.group(1) not in ids: bad.append((f,'없는 id',m.group(1)))
    # 3) JS 문법 검사 (인라인 스크립트 합쳐서 node --check)
    if inline.strip():
        with tempfile.NamedTemporaryFile('w',suffix='.js',delete=False,encoding='utf-8') as t:
            t.write(inline); path=t.name
        r=subprocess.run(['node','--check',path],capture_output=True,text=True)
        if r.returncode: bad.append((f,'JS 문법 오류',r.stderr.strip().splitlines()[0][:90]))
        os.unlink(path)
    # 4) 같은 기능 두 벌 — 페이지 안 인라인 + 불러 쓰는 .js 를 합쳐서 센다
    defs=collections.Counter(re.findall(r'\bwindow\.([A-Za-z_$][\w$]*)\s*=\s*function', inline+'\n'+'\n'.join(local_js(s))))
    defs.update(re.findall(r'^function\s+([A-Za-z_$][\w$]*)\s*\(', inline, re.M))
    for fn,c in defs.items():
        if c>1: bad.append((f,'두 벌',fn+' %d번'%c))
    # 5) 듣기 버튼이 트는 mp3
    m=re.search(r'<audio id="allplay-audio"[^>]*src="([^"]+)"', s)
    if m:
        full=m.group(1)
        if not os.path.exists(full): bad.append((f,'없는 mp3',full))
        for n in sorted(set(re.findall(r'class="blind-btn chunkplay" data-part="(\d+)"', s))):
            p=full.replace('_all.mp3','_p%s.mp3'%n)
            if not os.path.exists(p): bad.append((f,'없는 mp3',p))
print('검사 파일', len(glob.glob('*.html')))
if bad:
    print('문제', len(bad))
    for b in bad[:40]: print('  ', b)
else:
    print('문제 없음')
if '--block' in sys.argv:
    blk=[b for b in bad if b[1] in BLOCK]
    if blk:
        print('★올리지 않음: 같은 기능 두 벌·없는 mp3·JS 문법 오류 %d건 — 덧붙이지 말고 원래 코드를 고쳐라' % len(blk))
        sys.exit(1)
