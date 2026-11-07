# Gera as páginas estáticas a partir de templates simples (cabeçalho/rodapé compartilhados).
import pathlib
OUT = pathlib.Path(__file__).parent / "site"
NAV = [("index.html","Início"),("trabalhos.html","Trabalhos"),("artista.html","A artista"),("cuidados.html","Cuidados"),("orcamento.html","Orçamento")]

def page(fname, title, body, desc="Prévia visual — proposta de site para a tatuadora Trinity. Demonstração, sem serviços ativos.", cls=""):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow,noarchive">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0a0a0a">
<title>{title} · Trinity (prévia)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@400;500;700&family=Permanent+Marker&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body class="{cls}">
<a class="skip" href="#main">Pular para o conteúdo</a>
<div class="demo-strip" role="note">Proposta visual · demonstração · nenhum serviço está ativo</div>
<header class="site-header">
  <a class="brand" href="index.html" aria-label="Trinity — início"><span class="brand-mark" aria-hidden="true">T</span><span>Trinity<small>tattoo</small></span></a>
  <nav class="nav" id="nav" aria-label="Principal">{links}</nav>
  <a class="btn btn-sm hide-m" href="orcamento.html">Conte sua ideia</a>
  <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="nav" aria-label="Abrir menu"><span></span><span></span></button>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="foot-grid">
    <div><p class="foot-brand">Trinity<em> tattoo</em></p><p class="muted">Tatuadora no Espírito Santo · Glória, Vila Velha.<br>Atendimento no estúdio Dangeon Ink.</p></div>
    <div><p class="eyebrow">Navegar</p>{links}</div>
    <div><p class="eyebrow">Contato</p><button class="linklike" data-demo="O contato por WhatsApp está em modo demonstração: nenhuma conversa é aberta.">WhatsApp (demonstração)</button><p class="muted small">Endereço exato e horários: a confirmar com a artista.</p></div>
  </div>
  <div class="foot-bottom"><p class="small muted">Prévia visual criada como proposta. Não é o site oficial da artista. Imagens marcadas como “pendente” são placeholders.</p><a class="panel-link" href="painel.html">Ver painel demonstrativo</a></div>
</footer>
<button class="wa-float" data-demo="Botão de WhatsApp em modo demonstração. Nenhuma mensagem é enviada." aria-label="WhatsApp (demonstração)"><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M4 20l1.3-4.2A8 8 0 1 1 8.300 18.800z"/><path fill="currentColor" d="M9 8.500c.3 2.800 2.700 5.200 5.500 5.600l1.200-1.300-1.800-.9-.8.700c-1-.4-1.800-1.200-2.200-2.200l.7-.8-.9-1.800z"/></svg><span class="wa-tag">demo</span></button>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="js/app.js" defer></script>
</body>
</html>
'''

def w(name, html): (OUT/name).write_text(html, encoding="utf-8")

# ---------------- INÍCIO ----------------
w("index.html", page("index.html","Do traço à pele",'''
<section class="hero" id="inicio">
  <svg class="hero-lines" viewBox="0 0 800 800" aria-hidden="true" preserveAspectRatio="xMidYMid slice">
    <path class="draw" d="M80 700 C 200 520, 160 360, 330 300 S 560 120, 720 180"/>
    <path class="draw d2" d="M120 760 C 260 620, 300 520, 420 470 S 600 330, 700 360"/>
    <path class="draw d3" d="M540 80 C 500 200, 620 260, 560 400 S 440 560, 520 720"/>
    <circle class="draw d4" cx="560" cy="400" r="46"/>
  </svg>
  <div class="hero-in">
    <p class="eyebrow reveal">Tatuadora · Glória, Vila Velha — ES</p>
    <h1 class="hero-title reveal"><span>Do traço</span> <em>à pele.</em></h1>
    <p class="lead reveal">Anime, lettering e composições em preto marcante, desenhados sob medida para o corpo de quem vai carregar. Autoria da Trinity, do rascunho à sessão.</p>
    <div class="cta-row reveal"><a class="btn" href="trabalhos.html">Explorar trabalhos</a><a class="btn btn-ghost" href="orcamento.html">Conte sua ideia</a></div>
  </div>
  <figure class="hero-fig reveal" data-ph="hero" data-ph-label="Foto real pendente" data-ph-note="Retrato dela tatuando (reel DfSWS_RB8Eu) — arquivo original necessário"></figure>
  <p class="hero-note small muted">Vídeo de abertura (desenho → preparação → execução → resultado) ainda não integrado: depende dos arquivos originais.</p>
</section>

<section class="sec" id="selecao">
  <div class="sec-head"><p class="eyebrow">Trabalhos selecionados</p><h2 class="h2">Traços que <em>ficam.</em></h2></div>
  <div class="rail-wrap">
    <div class="rail" id="rail" tabindex="0" role="region" aria-label="Trabalhos selecionados, role para os lados"></div>
    <div class="rail-ctl"><button class="circle" id="railPrev" aria-label="Trabalho anterior">←</button><span class="small muted" id="railCount">1 / 6</span><button class="circle" id="railNext" aria-label="Próximo trabalho">→</button><a class="btn btn-ghost btn-sm" href="trabalhos.html">Ver todos</a></div>
  </div>
</section>

<section class="sec sketch" id="traco">
  <svg class="scroll-line" viewBox="0 0 40 1000" preserveAspectRatio="none" aria-hidden="true"><path id="scrollPath" d="M20 0 C 36 120, 4 220, 20 340 S 36 560, 20 700 S 6 880, 20 1000"/></svg>
  <div class="sec-head"><p class="eyebrow">Do traço à pele</p><h2 class="h2">Arraste e veja o desenho <em>virar tatuagem.</em></h2><p class="lead sm">Aqui entram pares reais: a arte e o resultado do mesmo trabalho. Nunca imagens diferentes simulando transformação.</p></div>
  <div class="cmp-grid">
    <div>
      <div class="cmp" id="cmp" data-pos="50">
        <div class="cmp-layer cmp-after" data-ph="cmpAfter"></div>
        <div class="cmp-layer cmp-before" data-ph="cmpBefore"></div>
        <span class="tag tag-l" id="tagL">Desenho</span><span class="tag tag-r red" id="tagR">Na pele</span>
        <div class="cmp-handle" aria-hidden="true"><span>‹ ›</span></div>
        <input class="cmp-range" type="range" min="0" max="100" value="50" aria-label="Divisor do comparador: desenho à esquerda, resultado na pele à direita">
      </div>
      <p class="badge-ill">Material ilustrativo · par real pendente — este exemplo não é trabalho da artista.</p>
    </div>
    <div class="cmp-side">
      <p class="eyebrow">O que está sendo comparado</p>
      <div class="chips" role="group" aria-label="Tipo de comparação">
        <button class="chip on" data-case="0" aria-pressed="true">Desenho → pele</button>
        <button class="chip" data-case="1" aria-pressed="false">Cobertura</button>
        <button class="chip" data-case="2" aria-pressed="false">Recém-feita → cicatrizada</button>
      </div>
      <p class="cmp-desc" id="cmpDesc"></p>
      <p class="small muted">Mouse, toque ou teclado (← →). Cada caso real será legendado com o que mostra: nada de “cicatrizada” como “antes”.</p>
    </div>
  </div>
</section>

<section class="sec split" id="artista-resumo">
  <figure class="split-fig" data-ph="portrait" data-ph-label="Foto real pendente" data-ph-note="Retrato no estúdio (reel DfP1swghb_g) — arquivo original necessário"></figure>
  <div>
    <p class="eyebrow">A artista e o processo</p>
    <h2 class="h2">Cada peça nasce <em>para uma anatomia.</em></h2>
    <p class="lead sm">Trinity mistura referências de anime e mangá, lettering e blocos de preto com leitura firme. O desenho é pensado junto com a região do corpo e a ideia de quem chega.</p>
    <ol class="steps">
      <li><b>Ideia</b><span>Você conta o que imagina e envia referências.</span></li>
      <li><b>Avaliação</b><span>Ela mesma avalia e responde o orçamento.</span></li>
      <li><b>Desenho</b><span>A arte é construída para o seu corpo.</span></li>
      <li><b>Sessão</b><span>Execução no estúdio, com cuidado e acompanhamento.</span></li>
    </ol>
    <a class="btn btn-ghost" href="artista.html">Conhecer o processo</a>
  </div>
</section>

<section class="sec cta-band">
  <p class="eyebrow">Convite</p>
  <h2 class="h2 big">Tem uma ideia? <em>Conte pra ela.</em></h2>
  <p class="lead sm">O pedido chega organizado — ideia, região, tamanho e referências — para a Trinity avaliar e responder pessoalmente.</p>
  <a class="btn" href="orcamento.html">Conte sua ideia</a>
</section>
'''))

# ---------------- TRABALHOS ----------------
w("trabalhos.html", page("trabalhos.html","Trabalhos",'''
<section class="page-head"><p class="eyebrow">Portfólio</p><h1 class="h1">Trabalhos</h1><p class="lead sm">Seleção em construção. Cada projeto abre em tela ampliada. Categorias serão criadas só quando os trabalhos reais as sustentarem.</p></section>
<section class="sec tight"><div class="works" id="worksGrid"></div></section>
'''))

# ---------------- ARTISTA ----------------
w("artista.html", page("artista.html","A artista e o processo",'''
<section class="page-head"><p class="eyebrow">A artista e o processo</p><h1 class="h1">Trinity, <em>autoria na pele.</em></h1></section>
<section class="sec split tight">
  <figure class="split-fig" data-ph="portrait" data-ph-label="Foto real pendente" data-ph-note="Retrato autorizado da artista"></figure>
  <div>
    <p class="lead">Tatuadora no Espírito Santo, atende na Glória, Vila Velha, no estúdio Dangeon Ink. Seu portfólio passa por anime e mangá, lettering e composições com preto marcante.</p>
    <p>Texto biográfico completo: <span class="pending">pendente de aprovação da artista</span>.</p>
    <h2 class="h3">Arte autoral, freehand e encomendas</h2>
    <p>A Trinity quer reunir num só lugar suas artes autorais, o trabalho em freehand e as encomendas de desenho. Os conteúdos reais serão adicionados conforme os arquivos forem fornecidos.</p>
  </div>
</section>
<section class="sec">
  <div class="sec-head"><p class="eyebrow">Processo</p><h2 class="h2">Do primeiro contato <em>à sessão.</em></h2></div>
  <ol class="timeline">
    <li><span class="n">01</span><h3>Você conta a ideia</h3><p>Pelo formulário: ideia, região do corpo, tamanho aproximado e referências.</p></li>
    <li><span class="n">02</span><h3>Ela avalia</h3><p>A Trinity continua respondendo pessoalmente. O pedido organizado ajuda a avaliar mais rápido, sem prometer prazo.</p></li>
    <li><span class="n">03</span><h3>O desenho</h3><p>Arte pensada para a anatomia. <span class="pending">Política de rascunho antes da sessão (ex.: envio com antecedência e finalização na sessão): em consulta, não definida.</span></p></li>
    <li><span class="n">04</span><h3>A sessão</h3><p>Duração, valor e disponibilidade são definidos por ela após a avaliação.</p></li>
  </ol>
</section>
<section class="sec cta-band"><h2 class="h2">Pronto para <em>começar o traço?</em></h2><a class="btn" href="orcamento.html">Conte sua ideia</a></section>
'''))

# ---------------- CUIDADOS ----------------
faq = [
 ("Cuidados antes da sessão","Estrutura reservada. O conteúdo será redigido e aprovado pela Trinity — não publicamos recomendações que ela ainda não validou."),
 ("Cuidados na cicatrização","Estrutura reservada, pendente de aprovação da artista. Nenhuma orientação de saúde é inventada nesta prévia."),
 ("Estilos e técnicas","Anime/mangá, lettering e composições em preto aparecem no portfólio. A lista oficial de estilos e técnicas será confirmada por ela."),
 ("Cobertura e reforma","Avaliadas caso a caso. Marque a opção no formulário e envie fotos de referência."),
 ("Valores e fechamentos","A tabela de preços para fechamentos foi mencionada, mas não há valores aprovados para publicar."),
 ("Horários e localização","Glória, Vila Velha (ES), no estúdio Dangeon Ink. Horários e endereço completo: a confirmar."),
 ("Rascunho antes da sessão","Ideia em consulta com o público: enviar um rascunho com alguns dias de antecedência e finalizar a arte junto na sessão. Ainda não é política definida."),
]
items = "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)
w("cuidados.html", page("cuidados.html","Cuidados e dúvidas",f'''
<section class="page-head"><p class="eyebrow">Cuidados e dúvidas</p><h1 class="h1">Antes, durante <em>e depois.</em></h1><p class="lead sm">Estrutura editorial pronta. Os textos finais aguardam aprovação da artista.</p></section>
<section class="sec tight faq-wrap">{items}</section>
<section class="sec cta-band"><h2 class="h2">Ficou uma dúvida? <em>Pergunte no pedido.</em></h2><a class="btn" href="orcamento.html">Conte sua ideia</a></section>
'''))

# ---------------- ORÇAMENTO ----------------
w("orcamento.html", page("orcamento.html","Orçamento",'''
<section class="page-head"><p class="eyebrow">Orçamento e agenda</p><h1 class="h1">Conte sua <em>ideia.</em></h1><p class="lead sm">Preencha com calma. A Trinity avalia e responde pessoalmente — duração, valor e disponibilidade dependem dela.</p></section>
<section class="sec tight form-sec">
  <div class="demo-box" role="note"><b>Demonstração.</b> Nada é enviado, salvo ou reservado. Os dados digitados ficam só nesta tela e somem ao recarregar.</div>
  <form id="quote" class="quote" novalidate>
    <ol class="progress" aria-label="Etapas"><li class="on">Você</li><li>Ideia</li><li>Detalhes</li><li>Revisão</li></ol>
    <fieldset class="step on" data-step="0"><legend>Quem é você</legend>
      <label>Nome<input name="nome" autocomplete="off" required></label>
      <label>Contato (WhatsApp ou e-mail)<input name="contato" autocomplete="off" required></label>
    </fieldset>
    <fieldset class="step" data-step="1"><legend>A ideia</legend>
      <label>Descreva a tatuagem<textarea name="ideia" rows="5" required placeholder="Ex.: personagem de anime no antebraço, em preto com traço firme"></textarea></label>
      <label>Referências <span class="muted">(simulação — nenhum arquivo é enviado)</span><div class="drop" id="drop" tabindex="0" role="button">Toque para simular o anexo de imagens</div></label>
      <ul class="refs" id="refs"></ul>
    </fieldset>
    <fieldset class="step" data-step="2"><legend>Detalhes</legend>
      <label>Região do corpo<select name="regiao"><option value="">Selecione</option><option>Braço</option><option>Antebraço</option><option>Perna</option><option>Costas</option><option>Peito</option><option>Pescoço</option><option>Outra</option></select></label>
      <label>Tamanho aproximado<select name="tamanho"><option value="">Selecione</option><option>Pequeno (até a palma da mão)</option><option>Médio</option><option>Grande</option><option>Fechamento</option><option>Não sei</option></select></label>
      <label>Preferência de período<select name="periodo"><option value="">Selecione</option><option>Manhã</option><option>Tarde</option><option>Sem preferência</option></select></label>
      <label class="check"><input type="checkbox" name="cobertura"> É cobertura ou reforma de uma tatuagem existente</label>
    </fieldset>
    <fieldset class="step" data-step="3"><legend>Revisão</legend>
      <dl class="review" id="review"></dl>
      <p class="small muted">Em um site real, este resumo chegaria organizado para a artista avaliar. Aqui, nada é enviado.</p>
    </fieldset>
    <div class="form-nav"><button type="button" class="btn btn-ghost" id="prev" hidden>Voltar</button><button type="button" class="btn" id="next">Continuar</button></div>
    <p class="err" id="err" role="alert"></p>
  </form>
  <div class="done" id="done" hidden tabindex="-1">
    <p class="eyebrow">Simulação concluída</p>
    <h2 class="h2">Esta é uma demonstração. <em>Nenhum pedido foi enviado.</em></h2>
    <p class="lead sm">Nenhuma sessão foi confirmada, nenhum horário foi reservado e nenhum dado foi salvo.</p>
    <p class="pending">Exemplo de como a artista veria o pedido: <a href="painel.html">ver painel demonstrativo</a>.</p>
    <button class="btn btn-ghost" id="again">Refazer simulação</button>
  </div>
</section>
'''))

# ---------------- PAINEL ----------------
w("painel.html", page("painel.html","Painel demonstrativo",'''
<section class="page-head"><p class="eyebrow">Painel demonstrativo</p><h1 class="h1">Pedidos <em>organizados.</em></h1><p class="lead sm">Extensão proposta. Dados 100% fictícios, sem login e sem backend.</p></section>
<section class="sec tight">
  <div class="demo-box"><b>Todos os nomes, datas e valores abaixo são fictícios.</b> Servem só para mostrar como o atendimento pode ficar claro.</div>
  <div class="stats">
    <div><b>5</b><span>aguardando avaliação</span></div><div><b>3</b><span>orçamentos em andamento</span></div><div><b>2</b><span>desenhos em etapas</span></div><div><b>4</b><span>próximas sessões</span></div>
  </div>
  <div class="tabs" role="tablist" aria-label="Seções do painel">
    <button role="tab" aria-selected="true" data-tab="pedidos">Pedidos</button><button role="tab" aria-selected="false" data-tab="agenda">Calendário</button><button role="tab" aria-selected="false" data-tab="desenhos">Etapas do desenho</button><button role="tab" aria-selected="false" data-tab="bloqueios">Bloqueios</button>
  </div>
  <div class="tabpane on" id="tab-pedidos"><div class="kanban" id="kanban"></div></div>
  <div class="tabpane" id="tab-agenda"><p class="small muted">Mês fictício. Sessões em vermelho, bloqueios hachurados.</p><div class="cal" id="cal"></div></div>
  <div class="tabpane" id="tab-desenhos"><div class="draws" id="draws"></div></div>
  <div class="tabpane" id="tab-bloqueios"><p class="lead sm">Dias e períodos em que ela não atende. Clique para alternar (simulação local).</p><div class="blocks" id="blocks"></div></div>
</section>
''', cls="panel"))
print("ok")
