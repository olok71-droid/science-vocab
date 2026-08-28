# -*- coding: utf-8 -*-
"""버튼이 부르는 함수가 실제로 있는지, JS가 찾는 id가 실제로 있는지 검사한다."""
import re, glob, os, subprocess, tempfile
os.chdir(os.path.expanduser('~/science-vocab-fresh'))
BUILTIN={'window','document','alert','confirm','console','event'}
bad=[]
for f in sorted(glob.glob('*.html')):
    s=open(f,encoding='utf-8').read()
    ids=set(re.findall(r'\bid="([^"]+)"', s))
    # 1) onclick / oninput 이 부르는 함수
    for m in re.finditer(r'on(?:click|input|change)="([^"]+)"', s):
        code=m.group(1)
        for fn in re.findall(r'(?<![.\w$])([A-Za-z_$][\w$]*)\s*\(', code):
            if fn in BUILTIN or fn in ('function','if','for','return','setTimeout','Audio'): continue
            if re.search(r'\bfunction\s+'+re.escape(fn)+r'\s*\(', s): continue
            if re.search(r'(?:window\.)?'+re.escape(fn)+r'\s*=\s*function', s): continue
            if re.search(r'\b(?:const|let|var)\s+'+re.escape(fn)+r'\s*=', s): continue
            bad.append((f,'없는 함수 호출',fn))
    # 2) getElementById 가 찾는 id
    for m in re.finditer(r"getElementById\(['\"]([^'\"]+)['\"]\)", s):
        if m.group(1) not in ids: bad.append((f,'없는 id',m.group(1)))
    # 3) JS 문법 검사 (인라인 스크립트 합쳐서 node --check)
    js='\n;\n'.join(re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', s, re.S))
    if js.strip():
        with tempfile.NamedTemporaryFile('w',suffix='.js',delete=False,encoding='utf-8') as t:
            t.write(js); path=t.name
        r=subprocess.run(['node','--check',path],capture_output=True,text=True)
        if r.returncode: bad.append((f,'JS 문법 오류',r.stderr.strip().splitlines()[0][:90]))
        os.unlink(path)
print('검사 파일', len(glob.glob('*.html')))
if bad:
    print('문제', len(bad))
    for b in bad[:25]: print('  ', b)
else:
    print('문제 없음')
