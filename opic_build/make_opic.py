# OPIc 음성 만들기: 문장별 en/ko mp3 + 주제별 합친 mp3(드릴·이어듣기). 다시 돌려도 안전(있는 파일은 건너뜀).
import asyncio, os, subprocess, json, sys
import edge_tts
from sentences import TOPICS
FF = os.path.expanduser('~/bin/ffmpeg'); FP = FF + 'probe' if os.path.exists(FF+'probe') else None
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audio', 'opic')
os.makedirs(OUT, exist_ok=True)
EN_VOICE, KO_VOICE = 'en-US-JennyNeural', 'ko-KR-SunHiNeural'
items = []
for ti, (title, sents) in enumerate(TOPICS):
    for en, ko in sents:
        items.append((len(items) + 1, ti, en, ko))

async def tts(text, voice, path):
    if os.path.exists(path) and os.path.getsize(path) > 1000: return
    for _ in range(3):
        try:
            await edge_tts.Communicate(text, voice).save(path)
            if os.path.getsize(path) > 1000: return
        except Exception as e: err = e
    raise SystemExit(f'TTS 실패: {path}')

async def main():
    for n, ti, en, ko in items:
        await tts(en, EN_VOICE, f'{OUT}/e{n}.mp3')
        await tts(ko, KO_VOICE, f'{OUT}/k{n}.mp3')
asyncio.run(main())

def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = r.split('Duration: ')[1].split(',')[0].split(':'); return int(h)*3600+int(m)*60+float(s)

def build(parts, out):
    # parts: [('f', path) | ('s', seconds)] → 24kHz mono mp3 하나로 다시 인코딩
    args, filt, k = [FF, '-y', '-loglevel', 'error'], '', 0
    for kind, v in parts:
        if kind == 'f': args += ['-i', v]
        else: args += ['-f', 'lavfi', '-t', f'{v:.2f}', '-i', 'anullsrc=r=24000:cl=mono']
        filt += f'[{k}:a]aresample=24000,aformat=channel_layouts=mono[a{k}];'; k += 1
    filt += ''.join(f'[a{i}]' for i in range(k)) + f'concat=n={k}:v=0:a=1[o]'
    subprocess.run(args + ['-filter_complex', filt, '-map', '[o]', '-b:a', '48k', out], check=True)

durs = {}
for ti, (title, _) in enumerate(TOPICS):
    its = [x for x in items if x[1] == ti]
    drill, story = [], []
    for n, _, en, ko in its:
        e = f'{OUT}/e{n}.mp3'; d = dur(e); durs[n] = round(d, 2)
        # 한국어 → 3초 생각 → 영어 → 따라 말할 시간 → 영어 한 번 더
        drill += [('f', f'{OUT}/k{n}.mp3'), ('s', 3.0), ('f', e), ('s', d + 1.0), ('f', e), ('s', 1.2)]
        story += [('f', e), ('s', 0.6)]
    build(drill, f'{OUT}/t{ti}_drill.mp3'); build(story, f'{OUT}/t{ti}_story.mp3')
    print('주제', ti, title, len(its), '문장')
json.dump(durs, open(os.path.join(OUT, 'durations.json'), 'w'))
