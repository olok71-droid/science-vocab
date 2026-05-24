// AMY Study App — 공통 모듈 (API 키 관리 + Claude API 호출)
// 브라우저에서 직접 Anthropic API 호출. 키는 localStorage에 저장.

const ANTHROPIC_API_URL = 'https://api.anthropic.com/v1/messages';
const MODEL = 'claude-sonnet-4-6';
const STORAGE_KEY = 'amy_anthropic_api_key';

function sanitizeKey(k) {
  if (!k) return '';
  // 공백 제거 + ASCII printable(0x20-0x7E)만 남김 (한글, zero-width, 보이지 않는 문자 제거)
  return k.trim().replace(/[^\x20-\x7E]/g, '').trim();
}

function getApiKey() {
  return sanitizeKey(localStorage.getItem(STORAGE_KEY) || '');
}

function setApiKey(k) {
  const clean = sanitizeKey(k);
  localStorage.setItem(STORAGE_KEY, clean);
  return clean;
}

function clearApiKey() {
  localStorage.removeItem(STORAGE_KEY);
}

function isLikelyValidKey(k) {
  // sk-ant-로 시작 + ASCII만 + 적당히 긴 길이
  return /^sk-ant-[A-Za-z0-9_\-]{20,}$/.test(k);
}

// ─── API 키 모달 ───
function ensureApiKey() {
  return new Promise((resolve, reject) => {
    if (getApiKey()) { resolve(getApiKey()); return; }
    showApiKeyModal((k) => {
      if (k) { setApiKey(k); resolve(k); }
      else reject(new Error('API 키 없음'));
    });
  });
}

function showApiKeyModal(onSave) {
  // 이미 떠 있으면 재사용
  let modal = document.getElementById('api-key-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'api-key-modal';
    modal.className = 'amy-modal-overlay';
    const saved = getApiKey();
    const savedHint = saved ? `<small style="color:var(--green)">✅ 현재 키 저장됨: ${saved.slice(0,10)}...${saved.slice(-4)} (다시 입력하면 교체)</small>` : '';
    modal.innerHTML = `
      <div class="amy-modal">
        <h2>🔑 Claude API 키 입력</h2>
        <p class="amy-modal-desc">
          채점·튜터 기능은 Anthropic의 Claude AI를 사용해요.<br>
          <a href="https://console.anthropic.com/settings/keys" target="_blank" rel="noopener" style="color: var(--accent)">console.anthropic.com</a>에서 API 키를 만들어 붙여넣어 주세요. (sk-ant-...로 시작)<br><br>
          <small style="color:var(--muted)">• 키는 <b>이 기기 브라우저에만</b> 저장돼요 (서버로 안 보냄)<br>• 한 번 입력하면 다음부터 자동 사용<br>• 복붙할 때 한국어 자판 OFF로 두면 안전해요</small><br>
          ${savedHint}
        </p>
        <input type="password" id="amy-key-input" class="amy-modal-input" placeholder="sk-ant-..." autocomplete="off" spellcheck="false">
        <div id="amy-key-status" style="font-size:12px;font-weight:700;min-height:18px;margin-bottom:10px"></div>
        <div class="amy-modal-buttons">
          <button class="amy-btn amy-btn-secondary" onclick="closeApiKeyModal()">취소</button>
          <button class="amy-btn amy-btn-primary" onclick="saveApiKeyFromModal()">저장</button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);
  }
  modal.style.display = 'flex';
  setTimeout(() => document.getElementById('amy-key-input').focus(), 100);
  window._amyKeyCallback = onSave;
  // Enter로 저장
  const input = document.getElementById('amy-key-input');
  input.value = getApiKey();
  input.onkeydown = (e) => { if (e.key === 'Enter') saveApiKeyFromModal(); };
}

function saveApiKeyFromModal() {
  const raw = document.getElementById('amy-key-input').value;
  const clean = sanitizeKey(raw);
  const status = document.getElementById('amy-key-status');
  if (!clean) {
    if (status) { status.textContent = '⚠️ 키가 비어있어요'; status.style.color = '#fca5a5'; }
    return;
  }
  if (raw.length !== clean.length) {
    // 비-ASCII 문자가 제거됨 — 사용자에게 알림
    if (status) { status.textContent = '⚠️ 키에 잘못된 문자가 있어 ' + (raw.length - clean.length) + '자 제거됨. 다시 정확히 복사해주세요.'; status.style.color = '#fbbf24'; }
    document.getElementById('amy-key-input').value = clean;
    return;
  }
  if (!isLikelyValidKey(clean)) {
    if (status) { status.textContent = '⚠️ 키 형식이 이상해요 (sk-ant-... 형식이어야 함)'; status.style.color = '#fbbf24'; }
    return;
  }
  setApiKey(clean);
  if (status) { status.textContent = '✅ 저장됨! 이 기기에서 다시 입력 안 해도 돼요'; status.style.color = '#4ade80'; }
  setTimeout(() => {
    closeApiKeyModal();
    if (window._amyKeyCallback) window._amyKeyCallback(clean);
  }, 700);
}

function closeApiKeyModal() {
  const m = document.getElementById('api-key-modal');
  if (m) m.style.display = 'none';
  if (window._amyKeyCallback) window._amyKeyCallback(null);
  window._amyKeyCallback = null;
}

// ─── Claude API 호출 ───
async function callClaude({ system, messages, maxTokens = 2048, temperature = 0.7 }) {
  let apiKey = await ensureApiKey();
  apiKey = sanitizeKey(apiKey);  // 안전성: 헤더로 보내기 전에 한 번 더 정화
  if (!apiKey) {
    throw new Error('API 키가 비어있어요. 🔑 버튼을 눌러 입력해주세요.');
  }
  if (!isLikelyValidKey(apiKey)) {
    throw new Error('API 키 형식이 이상해요 (sk-ant-... 형식이어야 함). 🔑 버튼을 눌러 다시 입력해주세요.\n현재 길이: ' + apiKey.length);
  }
  const body = {
    model: MODEL,
    max_tokens: maxTokens,
    temperature: temperature,
    messages: messages,
  };
  if (system) body.system = system;

  const res = await fetch(ANTHROPIC_API_URL, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
      'anthropic-dangerous-direct-browser-access': 'true',
    },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    let errText = `HTTP ${res.status}`;
    try {
      const errJson = await res.json();
      errText = errJson?.error?.message || errText;
    } catch (e) { /* ignore */ }
    if (res.status === 401) {
      // 키는 지우지 않음 (사용자가 직접 🔑 버튼으로 확인/수정).
      // 자동 삭제하면 사용자가 매번 다시 입력해야 함.
      throw new Error('API 키가 거부됐어요. 상단 🔑 버튼으로 키를 확인해주세요.\n(' + errText + ')');
    }
    if (res.status === 429) {
      throw new Error('요청이 너무 많아요. 잠시 후 다시 시도해주세요.\n(' + errText + ')');
    }
    throw new Error(errText);
  }
  return await res.json();
}

// 응답에서 텍스트 추출
function extractText(response) {
  if (!response?.content) return '';
  return response.content
    .filter(b => b.type === 'text')
    .map(b => b.text)
    .join('\n');
}

// 이미지 file → base64 (Claude 호환)
async function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const r = new FileReader();
    r.onload = () => {
      const result = r.result;
      // "data:image/png;base64,..." → base64만 추출
      const idx = result.indexOf(',');
      resolve({
        media_type: file.type || 'image/jpeg',
        data: result.slice(idx + 1),
      });
    };
    r.onerror = reject;
    r.readAsDataURL(file);
  });
}

// markdown 간단 렌더 (안전)
function renderMarkdown(md) {
  // HTML escape
  let html = md.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  // 코드 블록
  html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
  // 인라인 코드
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
  // 굵게
  html = html.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
  // 기울임
  html = html.replace(/(^|[^*])\*([^*\n]+)\*/g, '$1<i>$2</i>');
  // 헤딩 ##
  html = html.replace(/^### (.+)$/gm, '<h4>$1</h4>');
  html = html.replace(/^## (.+)$/gm, '<h3>$1</h3>');
  html = html.replace(/^# (.+)$/gm, '<h2>$1</h2>');
  // 리스트
  html = html.replace(/^[-*] (.+)$/gm, '<li>$1</li>');
  html = html.replace(/(<li>.*<\/li>\n?)+/g, m => '<ul>' + m + '</ul>');
  // 줄바꿈
  html = html.replace(/\n\n/g, '</p><p>');
  html = '<p>' + html + '</p>';
  html = html.replace(/<p><\/p>/g, '');
  html = html.replace(/<p>(<h\d|<ul|<pre)/g, '$1');
  html = html.replace(/(<\/h\d>|<\/ul>|<\/pre>)<\/p>/g, '$1');
  return html;
}
