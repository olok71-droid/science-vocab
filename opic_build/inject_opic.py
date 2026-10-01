# jenny.html 에 🎤 OPIc 탭을 넣는다(단어장 왼쪽). 다시 돌리면 표시 사이만 바꿔 끼운다.
import json, os, re
from sentences import TOPICS
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
P = os.path.join(ROOT, 'jenny.html')
s = open(P, encoding='utf-8').read()
durs = json.load(open(os.path.join(ROOT, 'audio/opic/durations.json')))
data, n = [], 0
for ti, (title, sents) in enumerate(TOPICS):
    rows = []
    for en, ko in sents:
        n += 1; rows.append({'n': n, 'en': en, 'ko': ko, 'd': durs[str(n)]})
    data.append({'title': title, 'items': rows})

CSS = r'''
  /* ==OPIC CSS== */
  .op-guide { background:#fff; border-radius:16px; box-shadow:0 2px 12px var(--shadow); margin-bottom:14px; }
  .op-guide summary { padding:13px 16px; font-weight:900; font-size:15px; cursor:pointer; list-style:none; }
  .op-guide summary::-webkit-details-marker { display:none; }
  .op-guide summary::after { content:'펼치기 ▾'; float:right; font-size:12px; color:var(--muted); }
  .op-guide[open] summary::after { content:'접기 ▴'; }
  .op-guide .g-body { padding:0 16px 14px; font-size:13.5px; line-height:1.65; }
  .op-guide h4 { font-size:14px; color:var(--accent); margin:12px 0 4px; }
  .op-guide table { width:100%; border-collapse:collapse; font-size:13px; margin:4px 0; }
  .op-guide td { border-bottom:1px solid rgba(246,166,35,0.18); padding:5px 4px; vertical-align:top; }
  .op-guide td:first-child { font-weight:800; white-space:nowrap; width:78px; }
  .op-topic { margin:18px 0 8px; display:flex; flex-wrap:wrap; align-items:center; gap:6px; }
  .op-topic .t { font-size:16px; font-weight:900; flex:1 1 100%; }
  .op-topic .t .cnt { font-size:12px; color:var(--muted); font-weight:700; }
  .op-card { background:#fff; border-radius:14px; box-shadow:0 2px 10px var(--shadow); padding:11px 12px; margin-bottom:8px;
             display:flex; gap:8px; align-items:flex-start; }
  .op-card.memorized { opacity:.45; }
  .op-card .num { font-size:11px; color:var(--muted); font-weight:800; min-width:24px; padding-top:3px; }
  .op-card .txt { flex:1; min-width:0; }
  .op-card .en { font-size:16px; font-weight:800; line-height:1.35; }
  .op-card .ko { font-size:13.5px; color:var(--accent); font-weight:700; line-height:1.35; margin-top:3px; }
  .op-card .blinded span { visibility:hidden; }
  .op-card .blinded { background:rgba(246,166,35,0.12); border-radius:6px; cursor:pointer; min-height:1.3em; }
  .op-card .btns { display:flex; flex-direction:column; gap:5px; }
  /* ==OPIC CSS END== */
'''

HTML = r'''<!-- ==OPIC HTML== -->
  <div class="tab-panel active" id="tab-opic">
    <details class="op-guide">
      <summary>📋 서베이·난이도 고르는 법</summary>
      <div class="g-body">
        <h4>1. 서베이(Background Survey)는 이렇게 고르세요</h4>
        서베이는 채점에 들어가지 않아요. 사실과 달라도 괜찮으니 <b>영어로 말하기 쉬운 것</b>, <b>서로 겹치는 것</b>을 고릅니다.
        <table>
          <tr><td>직업</td><td>일 경험 없음 (업무·상사 질문이 안 나와요)</td></tr>
          <tr><td>학생</td><td>아니오 → 수강 후 5년 이상 지남</td></tr>
          <tr><td>거주</td><td>개인 주택이나 아파트에 홀로 거주 (가족 질문이 줄어요)</td></tr>
          <tr><td>여가 6개</td><td>영화 보기 · 공연 보기 · 콘서트 보기 · 공원 가기 · 해변 가기 · 카페 가기</td></tr>
          <tr><td>취미 1개</td><td>음악 감상하기</td></tr>
          <tr><td>운동 3개</td><td>걷기 · 조깅 · 자전거</td></tr>
          <tr><td>휴가 2개</td><td>국내 여행 · 집에서 보내는 휴가</td></tr>
        </table>
        여가·취미·운동·휴가를 합쳐 <b>12개</b>예요. 12개 아래로는 다음 화면으로 넘어가지 않아요.<br>
        공원 산책 이야기 하나로 공원·걷기·조깅·자전거를, 영화관 이야기 하나로 영화·공연·콘서트를 돌려 쓸 수 있어요.

        <h4>2. 난이도(Self-Assessment)</h4>
        IM3 목표면 <b>4</b>를 고르세요. 3과 4는 같은 문제가 나오고, 4에서 과거 경험 질문이 조금 더 많을 뿐이에요.<br>
        7번 문제 뒤에 "쉬운 / 비슷한 / 더 어려운 질문" 중 하나를 고르는 화면이 나와요. 앞부분이 할 만했으면 <b>비슷한 질문</b>을 고르세요.

        <h4>3. 시험 순서 (난이도 3~4, 15문제)</h4>
        <table>
          <tr><td>1번</td><td>자기소개 (채점 안 됨)</td></tr>
          <tr><td>2~4번</td><td>서베이 주제: 묘사 → 습관 → 과거 경험</td></tr>
          <tr><td>5~7번</td><td>서베이 또는 돌발 주제: 묘사 → 습관 → 경험</td></tr>
          <tr><td>8~10번</td><td>돌발 주제 (은행·재활용·날씨 같은 것): 묘사 → 습관 → 경험·비교</td></tr>
          <tr><td>11~13번</td><td>롤플레이: 질문하기 → 문제 해결(대안 제시) → 관련 경험</td></tr>
          <tr><td>14~15번</td><td>일반 주제: 비교 → 의견</td></tr>
        </table>

        <h4>4. 답변 뼈대 (한 문제에 1~2분)</h4>
        ① 시작: 만능 문장으로 시간 벌기 (That's a good question…)<br>
        ② 묘사: 어디·무엇이 있나 (There is… / There are…)<br>
        ③ 습관: 보통 언제·어떻게 (I usually…)<br>
        ④ 경험: 한번은 무슨 일이 있었나 (Once… / One day…) — 과거형으로<br>
        ⑤ 마무리: Anyway, that's pretty much it.

        <h4>5. 이 탭으로 연습하는 법</h4>
        <b>▶ 듣기</b> = 한국어 → 3초 생각 → 영어 → 따라 말할 시간 → 영어 한 번 더. 한국어를 듣고 영어를 먼저 입으로 말해 보세요. 화면을 꺼도 계속 나와요.<br>
        <b>▶ 이어듣기</b> = 그 주제 영어 문장만 쭉 이어서. 1분 답변이 어떻게 들리는지 익혀요.<br>
        외운 문장은 🧠를 눌러 ✅로 바꾸면 듣기에서 빠져요.
      </div>
    </details>
    <div class="mem-bar"><span class="mem-info">총 <b>__TOTAL__</b>문장 · 외운 문장 <b id="op-mem-count">0</b>개</span>
      <button class="blind-btn" id="op-blind-en" onclick="opBlind('en')">🇺🇸 영어가림</button>
      <button class="blind-btn" id="op-blind-ko" onclick="opBlind('ko')">🇰🇷 한글가림</button>
      <button class="mem-toggle-btn" onclick="opResetMem()">↺ 외움 초기화</button></div>
    <div id="opic-list"></div>
  </div>
<!-- ==OPIC HTML END== -->
'''.replace('__TOTAL__', str(n))

JS = r'''// ==OPIC JS==
// ─── 🎤 OPIc 문장 (만드는 곳: opic_build/sentences.py → make_opic.py → inject_opic.py) ───
const OPIC = __DATA__;
let opMem = new Set();
try { opMem = new Set(JSON.parse(localStorage.getItem('memv_opic') || '[]')); } catch(e){}
let opBlindEn = false, opBlindKo = false;
function opSaveMem(){ try { localStorage.setItem('memv_opic', JSON.stringify([...opMem])); } catch(e){} }
function opToggleMem(n){ opMem.has(n) ? opMem.delete(n) : opMem.add(n); opSaveMem(); renderOpic(); }
function opResetMem(){ opMem.clear(); opSaveMem(); renderOpic(); }
function opBlind(side){ if (side==='en') opBlindEn=!opBlindEn; else opBlindKo=!opBlindKo; renderOpic(); }
function opPeek(el){ el.classList.toggle('blinded'); }
function opPlay(n){ stopSeq(); _audio = new Audio('audio/opic/e' + n + '.mp3'); _audio.play().catch(()=>{}); }

// 듣기: 외운 문장이 없으면 미리 합친 mp3(화면 꺼도 계속), 있으면 남은 문장만 낱개로 이어서
function opDrill(ti, btn, mode){
  const was = btn.classList.contains('active');
  stopSeq();
  if (was) return;
  const items = OPIC[ti].items.filter(x => !opMem.has(x.n));
  if (!items.length) return;
  btn.classList.add('active', 'play-all-btn'); btn.textContent = '⏹ 멈춤';
  const token = ++_seqToken;
  _seq = { token, btn };
  const label = mode === 'story' ? '▶ 이어듣기' : '▶ 듣기';
  btn.dataset.label = label;
  if (items.length === OPIC[ti].items.length) {
    // 끝나면 처음부터 다시. 파일이 안 열려 곧바로 끝나면(2초 안) 거기서 멈춘다 — 무한 재시도 방지
    const loop = () => { const t0 = Date.now();
      playFile('audio/opic/t' + ti + '_' + mode + '.mp3', token, () => { if (Date.now() - t0 < 2000) stopSeq(); else loop(); }); };
    loop(); return;
  }
  let i = 0;
  const wait = (ms, next) => { _thinkTimer = setTimeout(() => { if (_seq && _seq.token === token) next(); }, ms); };
  const one = () => {
    if (!_seq || _seq.token !== token) return;
    if (i >= items.length) i = 0;
    const x = items[i++], e = 'audio/opic/e' + x.n + '.mp3';
    if (mode === 'story') { playFile(e, token, () => wait(600, one)); return; }
    playFile('audio/opic/k' + x.n + '.mp3', token, () => wait(3000, () =>
      playFile(e, token, () => wait(x.d * 1000 + 1000, () =>
        playFile(e, token, () => wait(1200, one))))));
  };
  one();
}

function renderOpic(){
  const wrap = document.getElementById('opic-list');
  if (!wrap) return;
  let html = '';
  OPIC.forEach((t, ti) => {
    html += `<div class="op-topic"><span class="t">${esc(t.title)} <span class="cnt">· ${t.items.length}문장</span></span>
      <button class="blind-btn" onclick="opDrill(${ti}, this, 'drill')">▶ 듣기</button>
      <button class="blind-btn" onclick="opDrill(${ti}, this, 'story')">▶ 이어듣기</button></div>`;
    t.items.forEach(x => {
      const mem = opMem.has(x.n);
      html += `<div class="op-card${mem ? ' memorized' : ''}">
        <span class="num">${x.n}</span>
        <div class="txt">
          <div class="en${opBlindEn ? ' blinded' : ''}" onclick="opPeek(this)"><span>${esc(x.en)}</span></div>
          <div class="ko${opBlindKo ? ' blinded' : ''}" onclick="opPeek(this)"><span>${esc(x.ko)}</span></div>
        </div>
        <div class="btns">
          <button class="spk" onclick="opPlay(${x.n})" aria-label="원어민 발음">🔊</button>
          <button class="btn-mem${mem ? ' on' : ''}" onclick="opToggleMem(${x.n})" title="외웠으면 체크 (듣기에서 빠짐)">${mem ? '✅' : '🧠'}</button>
        </div></div>`;
    });
  });
  wrap.innerHTML = html;
  document.getElementById('op-mem-count').textContent = opMem.size;
  document.getElementById('op-blind-en').classList.toggle('active', opBlindEn);
  document.getElementById('op-blind-ko').classList.toggle('active', opBlindKo);
}
renderOpic();
// ==OPIC JS END==
'''.replace('__DATA__', json.dumps(data, ensure_ascii=False))

def put(s, start, end, block, anchor, before=True):
    if start in s:
        return re.sub(re.escape(start) + '.*?' + re.escape(end) + r'\n?', lambda m: block, s, count=1, flags=re.S)
    i = s.index(anchor)
    return s[:i] + block + s[i:] if before else s[:i+len(anchor)] + block + s[i+len(anchor):]

s = put(s, '  /* ==OPIC CSS== */', '  /* ==OPIC CSS END== */', CSS.lstrip('\n'), '</style>')
s = put(s, '<!-- ==OPIC HTML== -->', '<!-- ==OPIC HTML END== -->', HTML, '  <!-- 단어장 -->')
s = put(s, '// ==OPIC JS==', '// ==OPIC JS END==', JS, '// ─── 📷 새 학습자료(사진) 올리기 ───')
# 탭 버튼: OPIc 을 단어장 왼쪽에, 처음 열면 OPIc
if 'data-tab="opic"' not in s:
    s = s.replace('<button class="tab-btn active" data-tab="vocab">📖 단어장</button>',
                  '<button class="tab-btn active" data-tab="opic">🎤 OPIc</button>\n    <button class="tab-btn" data-tab="vocab">📖 단어장</button>', 1)
    s = s.replace('<div class="tab-panel active" id="tab-vocab">', '<div class="tab-panel" id="tab-vocab">', 1)
open(P, 'w', encoding='utf-8').write(s)
print('OK', n)
