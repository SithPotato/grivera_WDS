from flask import Flask, render_template

app = Flask(__name__)

usuarios = [
    {"nombre": "Ana", "correo": "ana@email.com"},
    {"nombre": "Juan", "correo": "juan@email.com"}
]

@app.route('/usuarios_web')
def usuarios_web():
    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
