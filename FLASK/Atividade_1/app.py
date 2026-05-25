from flask import Flask

app = Flask(__name__)


@app.route("/")
def explicar():
    return '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Currículo Profissional</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1 {
            color: #0056b3;
            margin-bottom: 5px;
        }
        h2 {
            color: #333;
            border-bottom: 2px solid #0056b3;
            padding-bottom: 5px;
            margin-top: 30px;
        }
        .contato {
            font-style: italic;
            color: #666;
            margin-bottom: 20px;
        }
        .item {
            margin-bottom: 15px;
        }
        .cargo {
            font-weight: bold;
            color: #0056b3;
        }
        .empresa-data {
            font-weight: bold;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Cabeçalho -->
        <h1>Alexandre Vieira Barbosa</h1>
        <p class="contato">Belo Horizonte, MG | (XX) XXXXX-XXXX | seu.email@email.com | linkedin.com</p>

        <!-- Resumo -->
        <h2>Resumo Profissional</h2>
        <p>Trabalhei alguns messes como analista de dados na empresa ISG ENGENHARIA E CONSULTORIA LTDA, e atualmente estou no 3 ano do colegio cotemig fazendo curso tecnico dentro da area da TEC.</p>

        <!-- Experiência -->
        <h2>Experiência Profissional</h2>
        <div class="item">
            <span class="cargo">Assistente em Analise de dados</span> — <span class="empresa-data"> IDG ENGENHARIA E CONSULTORIA LTDA </span>
            <p>O Assistente de Análise de Dados atua na coleta, limpeza, estruturação e validação de dados, apoiando equipes de BI e analistas na criação de relatórios e dashboards.</p>
        </div>
        
        <!-- Competências -->
        <h2>Competências Técnicas</h2>
        <ul>
            <li>Linguagens: Python, SQL, HTML, CSS</li>
            <li>Frameworks: Flask, Git, Docker</li>
            <li>Bancos de dados: MySQL</li>
        </ul>
    </div>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)
