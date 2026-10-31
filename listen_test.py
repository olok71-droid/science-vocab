#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""단원 페이지 '전체 듣기·20개씩 듣기'를 실제로 눌러 보는 시험(2026-10-31).
 - 외운 단어 없음 → 합친 mp3(_all, _p2)가 나오고 다시 누르면 멈추는지
 - 두 번째 단어를 외움 체크 → 전체 듣기·토막 1에서 그 단어가 안 나오고 나머지는 다 나오는지
매일 19:30 점검(~/classroom-sync/healthcheck.py)이 돌린다. 종료코드 0 = 전부 통과."""
import asyncio, glob, os, sys, subprocess, socket, time
from playwright.async_api import async_playwright
EXE='/Users/jenny/Library/Caches/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-mac-arm64/chrome-headless-shell'
INIT = """
window.__played=[];
const _p=HTMLMediaElement.prototype.play;
HTMLMediaElement.prototype.play=function(){ const el=this;
  if (el.id==='allplay-audio') return _p.apply(el, arguments);
  window.__played.push(decodeURIComponent((el.currentSrc||el.src||'').split('/').slice(-2).join('/')));
  setTimeout(()=>{ if(el.onended) el.onended(); }, 3); return Promise.resolve(); };
"""
SLUG="t=>t.replace(/~/g,'').replace(/\\//g,' ').toLowerCase().replace(/[^a-z0-9]+/g,'_').replace(/^_+|_+$/g,'')"
HERE=os.path.dirname(os.path.abspath(__file__))
def free_port():
    s=socket.socket(); s.bind(('127.0.0.1',0)); p=s.getsockname()[1]; s.close(); return p
PORT=free_port()
async def main():
    os.chdir(HERE)
    pages=[f for f in sorted(glob.glob('*.html')) if 'src="listen.js"' in open(f).read()]
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path=EXE, args=['--autoplay-policy=no-user-gesture-required'])
        bad=[]; ok=0
        for f in pages:
            ctx=await br.new_context(); await ctx.add_init_script(INIT); pg=await ctx.new_page()
            errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto('http://127.0.0.1:%d/'%PORT+f); await pg.wait_for_timeout(500)
            await pg.evaluate("document.querySelectorAll('#tab-vocab .vcard.memorized').forEach(c=>c.querySelector('button[onclick^=\"toggleMem\"]').click())")
            prob=[]
            # A) 외운 단어 없음 → 합친 mp3
            await pg.evaluate("toggleAllPlay()"); await pg.wait_for_timeout(700)
            st=await pg.evaluate("(()=>{const a=document.getElementById('allplay-audio');return [a.getAttribute('src'),a.paused,document.getElementById('allplay-btn').textContent]})()")
            if not st[0].endswith('_all.mp3') or st[1]: prob.append(('전체 mp3 안 나옴',st))
            await pg.evaluate("toggleAllPlay()"); await pg.wait_for_timeout(300)
            if not await pg.evaluate("document.getElementById('allplay-audio').paused"): prob.append('두번 눌러도 안 멈춤')
            nch=await pg.evaluate("document.querySelectorAll('.chunkplay').length")
            if nch:
                await pg.evaluate("playAllFrom(2)"); await pg.wait_for_timeout(700)
                st=await pg.evaluate("(()=>{const a=document.getElementById('allplay-audio');return [a.getAttribute('src'),a.paused]})()")
                if not st[0].endswith('_p2.mp3') or st[1]: prob.append(('토막2 mp3 안 나옴',st))
                await pg.evaluate("playAllFrom(2)"); await pg.wait_for_timeout(200)
            # B) 두 번째 단어 외움 → 전체 듣기에서 빠짐
            mem=await pg.evaluate("""(()=>{const c=document.querySelectorAll('#tab-vocab .vcard')[1]; c.querySelector('button[onclick^="toggleMem"]').click(); return c.querySelector('.vcard-en').textContent.trim();})()""")
            sl=await pg.evaluate(SLUG, mem)
            total=await pg.evaluate("document.querySelectorAll('#tab-vocab .vcard:not(.hidden)').length")
            await pg.evaluate("window.__played=[]; toggleAllPlay()"); await pg.wait_for_timeout(min(9000, 120+total*40))
            sci=[x for x in await pg.evaluate("window.__played") if x.startswith('sci/')]
            if ('sci/'+sl+'.mp3') in sci: prob.append('외운 단어가 들림')
            if len(sci) < total-1: prob.append(('단어 수 모자람',len(sci),total-1))
            if not await pg.evaluate("document.getElementById('allplay-audio').paused"): prob.append('이어듣기 중 합친 mp3도 나옴')
            if nch:
                await pg.evaluate("window.__played=[]; playAllFrom(1)"); await pg.wait_for_timeout(1500)
                sci=[x for x in await pg.evaluate("window.__played") if x.startswith('sci/')]
                if ('sci/'+sl+'.mp3') in sci: prob.append('토막1에서 외운 단어가 들림')
                if not sci: prob.append('토막1 이어듣기 안 나옴')
            if errs: prob.append(('페이지 오류',errs[:2]))
            if prob: bad.append((f,prob))
            else: ok+=1
            await ctx.close()
        print('듣기 시험',len(pages),'페이지 · 통과',ok); [print(b) for b in bad]
        await br.close()
        return 0 if ok==len(pages) else 1
srv=subprocess.Popen([sys.executable,'-m','http.server',str(PORT),'--bind','127.0.0.1'],cwd=HERE,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
try:
    time.sleep(1); rc=asyncio.run(main())
finally:
    srv.terminate()
sys.exit(rc)
