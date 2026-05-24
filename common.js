// AMY Study App — 공통 모듈 (API 키 관리 + Claude API 호출)
// 브라우저에서 직접 Anthropic API 호출. 키는 localStorage에 저장.

const ANTHROPIC_API_URL = 'https://api.anthropic.com/v1/messages';
const MODEL = 'claude-sonnet-4-6';
const STORAGE_KEY = 'amy_anthropic_api_key';

function getApiKey() {
  return localStorage.getItem(STORAGE_KEY) || '';
}

function setApiKey(k) {
  localStorage.setItem(STORAGE_KEY, k.trim());
}

function clearApiKey() {
  localStorage.removeItem(STORAGE_KEY);
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
    modal.innerHTML = `
      <div class="amy-modal">
        <h2>🔑 Claude API 키 입력</h2>
        <p class="amy-modal-desc">
          채점·튜터 기능은 Anthropic의 Claude AI를 사용해요.<br>
          <a href="https://console.anthropic.com/settings/keys" target="_blank" rel="noopener" style="color: var(--accent)">console.anthropic.com</a>에서 API 키를 만들어 붙여넣어 주세요. (sk-ant-...로 시작)<br><br>
          <small style="color:var(--muted)">키는 이 기기 브라우저에만 저장됩니다. 서버로 보내지 않아요.</small>
        </p>
        <input type="password" id="amy-key-input" class="amy-modal-input" placeholder="sk-ant-..." autocomplete="off">
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
  const v = document.getElementById('amy-key-input').value.trim();
  if (!v) return;
  setApiKey(v);
  closeApiKeyModal();
  if (window._amyKeyCallback) window._amyKeyCallback(v);
}

function closeApiKeyModal() {
  const m = document.getElementById('api-key-modal');
  if (m) m.style.display = 'none';
  if (window._amyKeyCallback) window._amyKeyCallback(null);
  window._amyKeyCallback = null;
}

// ─── Claude API 호출 ───
async function callClaude({ system, messages, maxTokens = 2048, temperature = 0.7 }) {
  const apiKey = await ensureApiKey();
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
      if (res.status === 401) {
        clearApiKey();
        throw new Error('API 키가 잘못됐어요. 다시 입력해 주세요.\n(' + errText + ')');
      }
    } catch (e) {
      if (e.message && e.message.includes('API 키')) throw e;
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
