(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const toast=$('#toast');let tt;
function say(m){toast.textContent=m;toast.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>toast.classList.remove('on'),3600)}
document.addEventListener('click',e=>{const d=e.target.closest('[data-demo]');if(d)say(d.dataset.demo)});

// Menu
const mb=$('#menuBtn'),nav=$('#nav');
const hh=()=>document.documentElement.style.setProperty('--hh',($('.site-header').getBoundingClientRect().bottom)+'px');
function menu(o){mb.setAttribute('aria-expanded',o);mb.setAttribute('aria-label',o?'Fechar menu':'Abrir menu');nav.classList.toggle('open',o);hh()}
mb.addEventListener('click',()=>menu(mb.getAttribute('aria-expanded')!=='true'));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){menu(false);mb.focus()}});
$$('.nav a').forEach(a=>a.addEventListener('click',()=>menu(false)));hh();

// Reveal
const io='IntersectionObserver'in window?new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{threshold:.12}):null;
$$('.reveal').forEach(el=>io?io.observe(el):el.classList.add('in'));

// Placeholders (arte gerada: NÃO são tatuagens nem fotos da artista)
function rnd(seed){let s=0;for(const c of seed)s=(s*31+c.charCodeAt(0))>>>0;return()=>{s=(s*1664525+1013904223)>>>0;return s/4294967296}}
function phSVG(seed,mode){const r=rnd(seed);let p='';for(let i=0;i<7;i++){const y=60+r()*380;p+=`<path d="M-10 ${y} C ${100+r()*60} ${y-140*r()}, ${200+r()*80} ${y+140*r()}, 430 ${y+(r()-.5)*160}" fill="none" stroke="${i%3?'#f2eee8':'#8a0f24'}" stroke-width="${mode==='fill'?10+r()*14:1.4}" stroke-opacity="${mode==='fill'?.85:.55}" stroke-linecap="round"/>`}
return `<svg viewBox="0 0 420 520" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="420" height="520" fill="${mode==='fill'?'#171717':'#232323'}"/>${p}</svg>`}
function paint(el,seed,mode,label,note){el.innerHTML=phSVG(seed,mode)+(label?`<div class="ph-tag"><b>${label}</b>${note||''}</div>`:'')}
const PH={hero:['hero','line'],portrait:['portrait','line'],cmpAfter:['cmpA','fill'],cmpBefore:['cmpB','line']};
$$('[data-ph]').forEach(el=>{const [s,m]=PH[el.dataset.ph]||[el.dataset.ph,'line'];paint(el,s,m,el.dataset.phLabel,el.dataset.phNote)});

// Trabalhos: fotos reais publicadas pela artista (títulos conforme as legendas dela)
const WORKS=[
{id:'DdeHF1om_KU',f:'makima',t:'Makima',d:'Chainsaw Man, em preto e cinza no braço.'},
{id:'DbOPc6fEcnn',f:'oni',t:'Máscara oni',d:'Blackwork de perna inteira.'},
{id:'DduJWvyGyih',f:'musashi',t:'Miyamoto Musashi',d:'Vagabond, no antebraço.'},
{id:'DfLHP1CgcXX',f:'kurapika',t:'Kurapika',d:'Hunter x Hunter, no antebraço.'},
{id:'DczCuhOgVih',f:'mao-blackwork',t:'Mão em blackwork',d:'Composição que fecha a mão inteira.'},
{id:'DfPnYgtG8zs',f:'trust-the-process',t:'Trust The Process',d:'Lettering desenhado para a anatomia da costela.'},
{id:'DdUS5k-m7Xq',f:'mao-ornamental',t:'Mão ornamental',d:'Blackwork ornamental na mão.'},
{id:'Db3iPOmFGD9',f:'freehand',t:'Freehand',d:'Desenhado direto na pele, sem decalque.'},
{id:'DcbvrqOG3kP',f:'castles',t:'Castles',d:'Do desenho à pele, no antebraço.'},
{id:'DbyKijrEfwZ',f:'malenia',t:'Malenia',d:'Elden Ring, no braço.'}];
const img=(src,alt,lazy)=>`<img src="${src}" alt="${alt}"${lazy?' loading="lazy" decoding="async"':''} width="1080" height="1350">`;
function card(w,i){const b=document.createElement('button');b.className='card';b.type='button';b.dataset.i=i;b.setAttribute('aria-label','Abrir '+w.t);
b.innerHTML=`<figure>${img('media/trabalhos/'+w.f+'-sm.jpg','Tatuagem: '+w.t,true)}</figure><h3>${w.t}</h3><p>${w.d}</p>`;b.addEventListener('click',()=>openV(i));return b}
const rail=$('#rail'),grid=$('#worksGrid');
if(rail)WORKS.slice(0,6).forEach((w,i)=>rail.append(card(w,i)));
if(grid)WORKS.forEach((w,i)=>grid.append(card(w,i)));
// Rail: controles, arraste com mouse (toque usa rolagem nativa)
if(rail){const cs=()=>$$('.card',rail);let cur=0;
function mark(){const c=rail.getBoundingClientRect();let best=0,bd=1e9;cs().forEach((el,i)=>{const r=el.getBoundingClientRect();const d=Math.abs(r.left+r.width/2-(c.left+c.width/2));if(d<bd){bd=d;best=i}});cur=best;cs().forEach((el,i)=>el.classList.toggle('active',i===best));$('#railCount').textContent=(best+1)+' / '+cs().length}
const go=n=>{cur=Math.max(0,Math.min(cs().length-1,n));cs()[cur].scrollIntoView({behavior:reduce?'auto':'smooth',inline:'center',block:'nearest'})};
$('#railPrev').onclick=()=>go(cur-1);$('#railNext').onclick=()=>go(cur+1);
rail.addEventListener('scroll',()=>requestAnimationFrame(mark),{passive:true});
rail.addEventListener('keydown',e=>{if(e.key==='ArrowRight')go(cur+1);if(e.key==='ArrowLeft')go(cur-1)});
let sx,sl,down=false,moved=false;rail.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse')return;down=true;moved=false;sx=e.clientX;sl=rail.scrollLeft});
addEventListener('pointermove',e=>{if(!down)return;const dx=e.clientX-sx;if(Math.abs(dx)>5){moved=true;rail.classList.add('drag')}rail.scrollLeft=sl-dx});
addEventListener('pointerup',()=>{if(down){down=false;rail.classList.remove('drag')}});
rail.addEventListener('click',e=>{if(moved){e.stopPropagation();e.preventDefault();moved=false}},true);mark()}

// Viewer
let dlg,vi=0,opener;
function ensureD(){if(dlg)return;dlg=document.createElement('dialog');dlg.className='viewer';dlg.setAttribute('aria-label','Detalhe do trabalho');
dlg.innerHTML='<button class="circle vw-close" aria-label="Fechar">✕</button><div class="vw"><figure id="vwF"></figure><div class="vw-info"><p class="eyebrow">Trabalho</p><h2 id="vwT"></h2><p id="vwD"></p><p class="small muted">Foto publicada pela artista no Instagram.</p><div class="vw-nav"><button class="circle" id="vwP" aria-label="Anterior">←</button><button class="circle" id="vwN" aria-label="Próximo">→</button><a class="btn btn-sm" href="orcamento.html" style="margin-left:auto">Conte sua ideia</a></div></div></div>';
document.body.append(dlg);$('.vw-close',dlg).onclick=()=>dlg.close();$('#vwP').onclick=()=>show(vi-1);$('#vwN').onclick=()=>show(vi+1);
dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close()});dlg.addEventListener('close',()=>{document.body.style.overflow='';opener&&opener.focus()});
dlg.addEventListener('keydown',e=>{if(e.key==='ArrowRight')show(vi+1);if(e.key==='ArrowLeft')show(vi-1)})}
function show(i){vi=(i+WORKS.length)%WORKS.length;const w=WORKS[vi];$('#vwF').innerHTML=img('media/trabalhos/'+w.f+'.jpg','Tatuagem: '+w.t);$('#vwT').textContent=w.t;$('#vwD').textContent=w.d}
function openV(i){opener=document.activeElement;ensureD();show(i);dlg.showModal();document.body.style.overflow='hidden'}

// Comparador
const cmp=$('#cmp');
if(cmp){const range=$('.cmp-range',cmp),bef=$('.cmp-before',cmp),hd=$('.cmp-handle',cmp);
const set=v=>{v=Math.max(0,Math.min(100,v));range.value=v;bef.style.clipPath=`inset(0 ${100-v}% 0 0)`;hd.style.left=v+'%'};
range.addEventListener('input',()=>set(+range.value));set(50);
// Pares reais do mesmo trabalho (fotos e vídeo publicados pela artista)
const CASES=[
{a:'Desenho',b:'Na pele',l:'par-castles-desenho',r:'par-castles-pele',t:'Castles: a arte que ela desenhou e a mesma peça já tatuada no antebraço.'},
{a:'Marcação',b:'Tatuagem',l:'par-freehand-marcacao',r:'par-freehand-pronta',t:'Freehand: o desenho riscado direto na pele e o resultado no mesmo braço.'},
{a:'Recém-feita',b:'Cicatrizada',l:'par-oni-recem',r:'par-oni-cicatrizada',t:'Máscara oni: a mesma tatuagem logo após a sessão e depois de cicatrizada. Fotos de momentos diferentes; ângulo e luz mudam.'}];
const load=k=>{$('#tagL').textContent=k.a;$('#tagR').textContent=k.b;$('#cmpDesc').textContent=k.t;
$('.cmp-before').innerHTML=img('media/trabalhos/'+k.l+'.jpg',k.a+' — '+k.t);$('.cmp-after').innerHTML=img('media/trabalhos/'+k.r+'.jpg',k.b+' — '+k.t);set(50)};
$$('.chip').forEach(c=>c.onclick=()=>{$$('.chip').forEach(x=>{x.classList.remove('on');x.setAttribute('aria-pressed','false')});c.classList.add('on');c.setAttribute('aria-pressed','true');load(CASES[+c.dataset.case])});
load(CASES[0])}

// Linha que se desenha na rolagem
const sp=$('#scrollPath');
if(sp){const L=sp.getTotalLength();sp.style.strokeDasharray=L;sp.style.strokeDashoffset=reduce?0:L;const sec=sp.closest('section');let tk=false;
const up=()=>{tk=false;if(reduce)return;const r=sec.getBoundingClientRect(),p=Math.min(1,Math.max(0,(innerHeight*.75-r.top)/(r.height)));sp.style.strokeDashoffset=L*(1-p)};
addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(up)}},{passive:true});up()}

// Formulário (simulação local)
const q=$('#quote');
if(q){let s=0;const steps=$$('.step',q),pr=$$('.progress li',q),nx=$('#next'),pv=$('#prev'),er=$('#err');
function render(){steps.forEach((x,i)=>x.classList.toggle('on',i===s));pr.forEach((x,i)=>x.classList.toggle('on',i<=s));pv.hidden=s===0;nx.textContent=s===3?'Simular envio':'Continuar';er.textContent='';
if(s===3){const f=new FormData(q);const rows=[['Nome',f.get('nome')],['Contato',f.get('contato')],['Ideia',f.get('ideia')],['Região',f.get('regiao')],['Tamanho',f.get('tamanho')],['Período',f.get('periodo')],['Cobertura/reforma',f.get('cobertura')?'Sim':'Não'],['Referências',$$('#refs li').map(x=>x.textContent).join(', ')||'—']];
$('#review').innerHTML='';rows.forEach(([k,v])=>{const d=document.createElement('div');d.innerHTML='<dt></dt><dd></dd>';d.firstChild.textContent=k;d.lastChild.textContent=v||'—';$('#review').append(d)})}}
nx.onclick=()=>{const req=$$('[required]',steps[s]).find(i=>!i.value.trim());if(req){er.textContent='Preencha o campo obrigatório para continuar.';req.focus();return}
if(s<3){s++;render();$('legend',steps[s]).scrollIntoView({block:'center'});}else{q.hidden=true;$('#done').hidden=false;$('#done').focus()}};
pv.onclick=()=>{s--;render()};
const drop=$('#drop');let n=0;const add=()=>{n++;const li=document.createElement('li');li.textContent='referencia-ficticia-'+n+'.jpg (simulado)';$('#refs').append(li)};drop.onclick=add;drop.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();add()}};
$('#again').onclick=()=>{q.reset();$('#refs').innerHTML='';s=0;n=0;q.hidden=false;$('#done').hidden=true;render()};
q.addEventListener('submit',e=>e.preventDefault());render()}

// Painel (dados fictícios)
if($('#kanban')){
const REQ=[
['Aguardando avaliação',[['Cliente fictício A','Personagem de anime, antebraço, preto','Grande',1,'há 2 dias'],['Cliente fictício B','Lettering curto, costela','Pequeno',0,'há 1 dia'],['Cliente fictício C','Cobertura de tatuagem antiga, perna','Médio',1,'hoje']]],
['Orçamento em andamento',[['Cliente fictício D','Fechamento de braço','Fechamento',0,'ref. recebidas'],['Cliente fictício E','Máscaras, panturrilha','Médio',0,'aguardando resposta']]],
['Sessão marcada (exemplo)',[['Cliente fictício F','Lettering, pescoço','Pequeno',0,'dia 12 · 14h (fictício)'],['Cliente fictício G','Retoque','Pequeno',0,'dia 19 · 10h (fictício)']]]];
$('#kanban').innerHTML=REQ.map(([h,a])=>`<div class="col"><h3>${h}</h3>${a.map(r=>`<div class="req"><b>${r[0]}</b><p>${r[1]}</p><div class="meta"><span>${r[2]}</span>${r[3]?'<span class="hot">cobertura/reforma</span>':''}<span>${r[4]}</span></div></div>`).join('')}</div>`).join('');
const cal=$('#cal');let h=['D','S','T','Q','Q','S','S'].map(d=>`<div class="dow">${d}</div>`).join('');for(let i=0;i<3;i++)h+='<div></div>';
const S={12:'Sessão fict.',19:'Sessão fict.',24:'Sessão fict.',27:'Sessão fict.'},B={5:1,6:1,20:1,21:1};
for(let d=1;d<=30;d++)h+=`<div class="day ${S[d]?'s':B[d]?'b':''}">${d}<i>${S[d]||(B[d]?'bloqueado':'')}</i></div>`;cal.innerHTML=h;
const ST=['Ideia','Rascunho','Revisão','Final'];
$('#draws').innerHTML=[['Cliente fictício F · lettering',2],['Cliente fictício G · retoque',3],['Cliente fictício A · anime',1],['Cliente fictício D · fechamento',0]].map(([n,k])=>`<div class="dr"><b>${n}</b><div class="stg">${ST.map((_,i)=>`<i class="${i<=k?'on':''}"></i>`).join('')}</div><div class="stl">${ST.map(x=>`<span>${x}</span>`).join('')}</div></div>`).join('');
$('#blocks').innerHTML=['Seg manhã','Seg tarde','Ter manhã','Ter tarde','Qua manhã','Qua tarde','Qui manhã','Qui tarde','Sex manhã','Sex tarde','Sáb manhã','Sáb tarde'].map((t,i)=>`<button class="blk" aria-pressed="${i===3||i===10}">${t}</button>`).join('');
$('#blocks').onclick=e=>{const b=e.target.closest('.blk');if(b)b.setAttribute('aria-pressed',b.getAttribute('aria-pressed')!=='true')};
$$('.tabs button').forEach(b=>b.onclick=()=>{$$('.tabs button').forEach(x=>x.setAttribute('aria-selected',x===b));$$('.tabpane').forEach(p=>p.classList.toggle('on',p.id==='tab-'+b.dataset.tab))})}
})();
