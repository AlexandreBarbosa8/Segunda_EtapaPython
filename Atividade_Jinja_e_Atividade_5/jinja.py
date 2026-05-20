from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if usuario.lower() == 'Nome' and senha == 'Matricula':
            return f"<h1>Bem-vindo, {usuario}! Acesso autorizado.</h1>"
        else:
            return "<h1>Login inválido. Tente novamente.</h1>"
            
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
