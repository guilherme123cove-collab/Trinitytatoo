# Trinity — prévia navegável "Do traço à pele"

**Proposta visual. Nenhum serviço ativo. Não é o site oficial da artista.** Site estático (HTML/CSS/JS puro, sem dependências além de 2 fontes do Google Fonts), `noindex` + `robots.txt` bloqueando tudo.

- Rodar: `cd site && python3 -m http.server 8123` · Regenerar páginas: `python3 build.py`
- Páginas: `index` (home), `trabalhos`, `artista`, `cuidados`, `orcamento`, `painel` (acesso discreto no rodapé: "Ver painel demonstrativo").

## Diagnóstico da referência (giobbeauty.com — somente frontend público)
**Verificado:** SPA Vite + React + Tailwind (bundle único `/assets/index-*.js`, CSS `styles-*.css`; imagens servidas por `lovable.app`). Nav por âncoras (`#home`, `#rentals`…). Animações de entrada por classe (`opacity:0; blur(10px); translateY(30px)` → visível ao entrar na tela, via IntersectionObserver). Marquee em CSS (`@keyframes marquee`). Galeria em faixa horizontal de colunas com cantos arredondados. Comparador: duas `<img>` empilhadas, a "antes" recortada com `clip-path: inset(0 X% 0 0)`, divisor de 1px com alça central, container `touch-none`/`cursor-ew-resize`, miniaturas (`aria-pressed`) para trocar de caso; eventos `pointermove`/`touchmove`. Há `prefers-reduced-motion`. Agendamento sai para Boulevard (link externo).
**Não verificado:** vídeo do hero (não encontrado no HTML inicial; pode ser injetado pelo JS), código-fonte original, backend.
**Por que é eficiente:** hero direto com CTA, ritmo alternado de seções claras/escuras, imagem grande, comparador de baixa fricção, um único destino de ação.
**O que aproveitamos → reinterpretação:** âncoras/ritmo → site multipágina enxuto para artista solo; faixa de galeria → trilho de trabalhos com scroll-snap, setas e arraste (sem bloquear rolagem vertical); comparador clip-path → "Do traço à pele" com divisor por mouse/toque/teclado (`input range` acessível) e legenda do que se compara; reveal on scroll → linha SVG que se desenha na rolagem; CTA externo → formulário **simulado** + painel fictício.

## Limitações desta sessão (declaradas)
- **Instagram da Trinity:** só retorna tela de login para acesso sem autenticação. Não contornei. Nenhuma foto/vídeo foi baixado ou avaliado; **os reels não foram assistidos**. Os IDs de publicações (DbOPc6fEcnn etc.) vêm do seu briefing.
- Não vi a Giob renderizada em navegador (o frontend foi analisado pelo HTML/JS/CSS baixados).

## Mídias utilizadas
Nenhuma foto ou vídeo real. Todas as imagens são **placeholders gráficos gerados em SVG**, marcados "Foto real pendente" com o ID do material necessário. Hero sem vídeo (declarado na tela).

## Materiais reais necessários
1. Vídeo curto dela tatuando (desenho → preparação → execução → resultado) + poster + versão vertical (reel DfSWS_RB8Eu / DfP1swghb_g).
2. Fotos originais: máscaras (DbOPc6fEcnn), Trust The Process (DfPnYgtG8zs), Forgiveness (Dd4cAwnG7A2), Chainsaw Man (DdeHF1om_KU), Musashi (DduJWvyGyih), com detalhe e relação com a anatomia; retrato autorizado.
3. Pares reais correspondentes (desenho↔pele, cobertura, recém-feita↔cicatrizada), com legenda.
4. Textos aprovados: bio, cuidados pré/pós, estilos/técnicas, política de rascunho, horários, endereço, valores de fechamento.
5. Confirmação de autorização de uso das imagens.

## Verificações feitas (Chromium headless/Playwright; **nenhum aparelho físico testado**)
- 6 páginas × larguras 390, 820 e 1440: sem overflow horizontal, sem erros de JS.
- Menu mobile abre/fecha (botão e Escape); trilho avança; comparador responde às setas; modal abre e fecha com Escape; formulário completa as 4 etapas e exibe "Esta é uma demonstração. Nenhum pedido foi enviado."
- Revisão visual de screenshots da home (desktop e mobile).
- **Não feito:** auditoria formal de contraste (paleta escolhida para alto contraste), teste com leitor de tela, medição de performance real (sem imagens reais ainda), teste de vídeo.

## Fora de escopo, por regra
Sem envio, armazenamento, backend, upload, pagamento, login, reserva ou abertura de WhatsApp (botão flutuante só mostra aviso). Publicação em endereço de demonstração **não foi feita**; ao publicar, manter `noindex`.
