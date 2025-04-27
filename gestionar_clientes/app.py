from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar usuarios
usuarios = []

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'nombre_sistema': 'Gestión de Usuarios y Productos',
        'version': '1.0',
        'autor': 'Tu Nombre',
        'descripcion': 'API para administrar usuarios y productos.'
    })

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No se recibieron datos JSON.'}), 400

    nombre = data.get('nombre')
    correo = data.get('correo')

    if not nombre or not correo:
        return jsonify({'error': 'Se requiere "nombre" y "correo" para crear un usuario.'}), 400

    nuevo_usuario = {
        'id': len(usuarios) + 1,
        'nombre': nombre,
        'correo': correo
    }

    usuarios.append(nuevo_usuario)
    return jsonify({'mensaje': 'Usuario creado exitosamente.', 'usuario': nuevo_usuario}), 201

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({'usuarios': usuarios})

if __name__ == '__main__':
    app.run(debug=True)
