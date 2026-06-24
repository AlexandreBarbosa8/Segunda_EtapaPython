# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Alexandre Vieira Barbosa
- Turma: 3B1

---

# Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

H:\Python\Aula12 - Alunos\models\base

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

streamflix.db

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

init, base, filme_favorito e historico busca

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

filme_Favorito.py e historico_busca.py

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

Não sei

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

    @classmethod
    def buscar_por_tmdb(cls, tmdb_id):
        return cls.query.filter_by(tmdb_id=tmdb_id).first()

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

o metodo pega as informaçoes do filme para adicionar como favorito, se já existir ele retorna nada, ou seja não faz nada

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

historico_busca.py  
   @classmethod
    def ultimas(cls, limite=8):
        return cls.query.order_by(cls.data_criacao.desc()).limit(limite).all()

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

alguns campso - cls, tmdb_id, titulo, nota

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

Filme favorito e o Historico de busca, porque ele só precisa do filme favorito e não da pasta inteira
---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

dashboard_bp, favoritos_bp, filmes_bp

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

não sei

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

puxa as infos do filme popular em questão 
@filmes_bp.route("/populares")
def populares():
    api = TmdbApi()
    filmes, demo = api.filmes_populares()
    ids_fav = {f.tmdb_id for f in FilmeFavorito.listar()}

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

filmes_controller linhas 42 começa

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

POST

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

return redirect(url_for("filmes.populares"))

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

app.py  from controllers import dashboard_bp, favoritos_bp, filmes_bp

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

dashboar_controller 
return render_template(
        "index.html",
        populares=populares[:6],
        melhores=melhores[:6],
        total_favoritos=len(favoritos),
        historico=historico,
        modo_demo=demo or api.usando_demo,
    )

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

Camada Model pertence a lógica - dashboard_controller filmes_controller, init
eles chamam a api para pegar os dados dos respectivos filmes


**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

Se a tag do formulário usar method="POST" vai ser request.form

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

H:\Python\Aula12 - Alunos\views\templates

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

layout.html comando {% extends %}

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
      dashboard.index 
      filmes.populares
      filmes.melhores
      filmes.buscar
      favoritos.listar

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

detalhe.html  <div class="streaming-box">

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

um pedaço, o index {% if streaming.flatrate %}

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

Através do if else

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

H:\Python\Aula12 - Alunos\views\static\css    o layout linka CSS

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

{% for filme in filmes %}
{% include "filmes/_card.html" %}

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

Serve para ativar um modo de demonstração da API do imdb

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

Não sei 
----


## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
