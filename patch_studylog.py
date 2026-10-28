#!/usr/bin/env python3
"""공부기록(studylog.js)을 앱 페이지 맨 끝에 붙인다. 다시 돌려도 안전(이미 붙은 페이지는 건너뜀).
새 페이지가 생기면 이것을 다시 돌린다."""
import glob, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TAG = '<script src="studylog.js"></script>'
SKIP = {'study_log.html', 'soundtest.html'}
done = 0
for f in sorted(glob.glob('*.html')):
    if f in SKIP:
        continue
    s = open(f, encoding='utf-8').read()
    if 'studylog.js' in s or '</body>' not in s:
        continue
    i = s.rfind('</body>')
    s = s[:i] + TAG + '\n' + s[i:]
    open(f, 'w', encoding='utf-8').write(s)
    done += 1
print('붙인 페이지', done)
missing = [f for f in glob.glob('*.html') if f not in SKIP and 'studylog.js' not in open(f, encoding='utf-8').read()]
print('안 붙은 페이지', missing)
sys.exit(1 if missing else 0)
