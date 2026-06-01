# ⚽ Futebol Agora — Site de Notícias

Site de notícias de futebol que atualiza automaticamente todo dia.

---

## Como colocar no ar (passo a passo)

### 1. Crie sua conta no GitHub
Acesse https://github.com e crie uma conta gratuita.

### 2. Crie um repositório
- Clique em **New repository**
- Nome: `futebol-agora`
- Marque: **Public**
- Clique em **Create repository**

### 3. Suba os arquivos
Faça upload de todos os arquivos deste projeto:
- `index.html`
- `fetch_news.py`
- `.github/workflows/atualizar-noticias.yml`

### 4. Pegue sua API key gratuita
- Acesse https://gnews.io
- Crie uma conta gratuita
- Copie sua **API key**

### 5. Configure o segredo no GitHub
- No seu repositório, vá em **Settings → Secrets → Actions**
- Clique em **New repository secret**
- Nome: `GNEWS_API_KEY`
- Valor: cole sua API key
- Clique em **Add secret**

### 6. Ative o GitHub Pages
- Vá em **Settings → Pages**
- Em "Source", selecione **Deploy from a branch**
- Branch: `main`, pasta: `/ (root)`
- Clique em **Save**

### 7. Seu site está no ar!
Acesse: `https://SEU_USUARIO.github.io/futebol-agora`

Cole sua API key na caixa que aparece na primeira visita — ela fica salva no navegador.

---

## Como funciona a atualização automática

Todo dia às 06:00 (horário de Brasília) o GitHub Actions:
1. Roda o script `fetch_news.py`
2. Busca as últimas notícias de futebol
3. Salva em `noticias.json`
4. Publica automaticamente

Você também pode rodar manualmente a qualquer momento em:
**Actions → Atualizar Notícias Diárias → Run workflow**

---

## Categorias disponíveis
- Brasileirão
- Champions League
- Seleção Brasileira
- Copa do Mundo 2026
- Transferências
- Geral

---

## Plano gratuito GNews
- 100 chamadas por dia
- Suficiente para atualizar 5 categorias por dia com folga
