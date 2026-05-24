// 단원 페이지 검색
function setupUnitSearch(){
  const input=document.getElementById('search');
  const clearBtn=document.getElementById('clear-search');
  const box=document.getElementById('search-results');
  if(!input||!box||typeof PAGE_DATA==='undefined') return;

  const flat=[];
  PAGE_DATA.forEach((ch,ci)=>{
    ch.pages.forEach((txt,pi)=>{
      flat.push({chTitle:ch.title,slug:ch.slug,page:pi+1,text:txt});
    });
  });

  function escapeHtml(s){return s.replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
  function snippet(txt,q){
    const i=txt.toLowerCase().indexOf(q.toLowerCase());
    if(i<0) return escapeHtml(txt.slice(0,120))+'…';
    const start=Math.max(0,i-40), end=Math.min(txt.length,i+q.length+80);
    const before=escapeHtml(txt.slice(start,i));
    const hit=escapeHtml(txt.slice(i,i+q.length));
    const after=escapeHtml(txt.slice(i+q.length,end));
    return (start>0?'…':'')+before+'<mark>'+hit+'</mark>'+after+(end<txt.length?'…':'');
  }
  function run(q){
    if(!q||q.length<2){box.hidden=true;box.innerHTML='';clearBtn.hidden=true;return;}
    clearBtn.hidden=false;
    const ql=q.toLowerCase();
    const hits=flat.filter(h=>h.text.toLowerCase().includes(ql)).slice(0,30);
    if(hits.length===0){box.innerHTML='<div class="empty">검색 결과 없음</div>';box.hidden=false;return;}
    box.innerHTML=hits.map(h=>`<div class="hit" data-slug="${h.slug}" data-page="${h.page}"><div class="hit-title">${escapeHtml(h.chTitle)} · ${h.page}p</div><div class="hit-snippet">${snippet(h.text,q)}</div></div>`).join('');
    box.hidden=false;
  }
  let t;
  input.addEventListener('input',e=>{clearTimeout(t);t=setTimeout(()=>run(e.target.value.trim()),120);});
  clearBtn.addEventListener('click',()=>{input.value='';run('');input.focus();});
  box.addEventListener('click',e=>{
    const hit=e.target.closest('.hit');
    if(!hit) return;
    const slug=hit.dataset.slug, page=hit.dataset.page;
    const img=document.querySelector(`#ch-${slug} figure[data-page="${page}"]`);
    if(img){img.scrollIntoView({behavior:'smooth',block:'start'});img.classList.add('highlight');setTimeout(()=>img.classList.remove('highlight'),1500);}
  });
}

// 홈 전체 검색
function setupHomeSearch(){
  const input=document.getElementById('search-all');
  const box=document.getElementById('search-all-results');
  if(!input||!box||typeof ALL_DATA==='undefined') return;

  const flat=[];
  ALL_DATA.units.forEach(u=>{
    u.chapters.forEach(ch=>{
      ch.pages.forEach((txt,pi)=>{
        flat.push({unitTitle:u.title,unitHref:u.href,chTitle:ch.title,slug:ch.slug,page:pi+1,text:txt});
      });
    });
  });

  function escapeHtml(s){return s.replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
  function snippet(txt,q){
    const i=txt.toLowerCase().indexOf(q.toLowerCase());
    if(i<0) return escapeHtml(txt.slice(0,120))+'…';
    const start=Math.max(0,i-40), end=Math.min(txt.length,i+q.length+80);
    return (start>0?'…':'')+escapeHtml(txt.slice(start,i))+'<mark>'+escapeHtml(txt.slice(i,i+q.length))+'</mark>'+escapeHtml(txt.slice(i+q.length,end))+(end<txt.length?'…':'');
  }
  function run(q){
    if(!q||q.length<2){box.innerHTML='';return;}
    const ql=q.toLowerCase();
    const hits=flat.filter(h=>h.text.toLowerCase().includes(ql)).slice(0,40);
    if(hits.length===0){box.innerHTML='<div class="empty">검색 결과 없음</div>';return;}
    box.innerHTML=hits.map(h=>`<a class="hit" href="${h.unitHref}#ch-${h.slug}"><div class="hit-title">${escapeHtml(h.unitTitle)} → ${escapeHtml(h.chTitle)} · ${h.page}p</div><div class="hit-snippet">${snippet(h.text,q)}</div></a>`).join('');
  }
  let t;
  input.addEventListener('input',e=>{clearTimeout(t);t=setTimeout(()=>run(e.target.value.trim()),150);});
}

document.addEventListener('DOMContentLoaded',()=>{setupUnitSearch();setupHomeSearch();});
