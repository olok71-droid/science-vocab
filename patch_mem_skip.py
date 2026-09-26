# -*- coding: utf-8 -*-
"""외운 단어로 체크한 것은 전체 듣기·부분(토막) 듣기에서 들리지 않게 한다 — 전 과목.
2026-09-26 대표님 지시. 합친 mp3는 통짜라 중간을 못 건너뛰므로, 외운 단어가 하나라도 있으면
그 단원(또는 그 토막)만 낱개 발음을 이어서 들려준다. 외운 단어가 없으면 예전처럼 합친 mp3."""
import io, glob, re, sys

MARK = "/* 외운 단어를 숨긴 상태면"
NEW = r"""/* ★2026-09-26 대표님 지시: '외운 단어'로 체크한 것은 전체 듣기·부분 듣기에서 들리지 않는다.
   합쳐 둔 mp3 는 통짜라 중간을 건너뛸 수 없다 → 외운 단어가 하나라도 있으면 그 단원(또는 그 토막)은
   낱개 발음을 이어서 들려준다. 외운 단어가 없으면 예전처럼 합친 mp3 를 튼다(화면을 꺼도 계속 나온다). */
(function(){
  var btn = document.getElementById('allplay-btn');
  var a   = document.getElementById('allplay-audio');
  if (!btn) return;
  var seq = null, cur = null, curBtn = null;
  function slug(t){ return (t||'').replace(/~/g,'').replace(/\//g,' ').toLowerCase().replace(/[^a-z0-9]+/g,'_').replace(/^_+|_+$/g,''); }
  function cards(){ return Array.prototype.slice.call(document.querySelectorAll('#tab-vocab .vcard')); }
  function isMem(c){ return c.classList.contains('memorized'); }
  function enOf(c){ var e = c.querySelector('.vcard-en'); return e ? (e.textContent||'').trim() : ''; }
  function labelOf(b){ return b === btn ? '▶ 전체 듣기' : (b.getAttribute('data-label') || '▶'); }
  function stop(){
    if (cur) { try { cur.pause(); } catch(e){} cur = null; }
    seq = null;
    if (curBtn) { curBtn.textContent = labelOf(curBtn); curBtn.classList.remove('active'); curBtn = null; }
  }
  window.stopVisibleSeq = stop;
  function playList(words, b){
    var i = 0, token = {};
    seq = token; curBtn = b;
    b.textContent = '⏸ 멈춤'; b.classList.add('active');
    (function next(){
      if (seq !== token) return;
      if (i >= words.length) { stop(); return; }   // 끝나면 멈춘다
      var sl = slug(words[i]);
      var koDone = false, enDone = false;
      var ko = new Audio('audio/sci_ko/' + sl + '.mp3');
      cur = ko;
      var afterEn = function(){
        if (enDone) return; enDone = true;
        if (seq === token) { i++; next(); }
      };
      var afterKo = function(){
        if (koDone) return; koDone = true;
        if (seq !== token) return;
        var en = new Audio('audio/sci/' + sl + '.mp3');
        cur = en;
        en.onended = afterEn; en.onerror = afterEn;
        en.play().catch(afterEn);
      };
      ko.onended = afterKo; ko.onerror = afterKo;
      ko.play().catch(afterKo);
    })();
  }
  /* 토막 버튼 라벨('1~20')에서 몇 번째~몇 번째 단어인지 읽는다 */
  function rangeOf(b){
    var m = (b.getAttribute('data-label') || '').match(/(\d+)\s*~\s*(\d+)/);
    return m ? [parseInt(m[1],10), parseInt(m[2],10)] : null;
  }
  function pick(from, to){            // 1-based, 없으면 전체
    var all = cards();
    var part = (from && to) ? all.slice(from - 1, to) : all;
    var out = [], memCount = 0;
    part.forEach(function(c){
      if (c.classList.contains('hidden')) return;
      if (isMem(c)) { memCount++; return; }
      var en = enOf(c); if (en) out.push(en);
    });
    return { words: out, mem: memCount };
  }
  var origToggle = window.toggleAllPlay;
  var origFrom   = window.playAllFrom;
  window.toggleAllPlay = function(){
    if (seq && curBtn === btn) { stop(); return; }
    stop();
    var r = pick(null, null);
    if (!r.mem) { if (origToggle) origToggle(); return; }   // 외운 단어 없음 → 합친 mp3
    if (a && !a.paused) a.pause();
    if (!r.words.length) return;
    playList(r.words, btn);
  };
  window.playAllFrom = function(n, label){
    var b = document.querySelector('.chunkplay[data-part="' + n + '"]');
    if (seq && curBtn === b) { stop(); return; }
    stop();
    var rg = b ? rangeOf(b) : null;
    var r = pick(rg ? rg[0] : null, rg ? rg[1] : null);
    if (!r.mem) { if (origFrom) origFrom(n, label); return; }
    if (a && !a.paused) a.pause();
    if (!r.words.length || !b) return;
    playList(r.words, b);
  };
})();"""

def patch(path):
    s = io.open(path, encoding="utf-8").read()
    i = s.find(MARK)
    if i < 0:
        return "블록없음"
    j = s.find("</script>", i)
    if j < 0:
        return "끝못찾음"
    if "2026-09-26 대표님 지시" in s[i:j]:
        return "이미적용"
    io.open(path, "w", encoding="utf-8").write(s[:i] + NEW + "\n" + s[j:])
    return "적용"

if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob("*.html"))
    done = {}
    for f in files:
        r = patch(f)
        done.setdefault(r, []).append(f)
    for k, v in done.items():
        print(f"{k}: {len(v)}개")
        if k == "적용":
            print("   ", ", ".join(v))
