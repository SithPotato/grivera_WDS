from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista en memoria para almacenar los usuarios
usuarios = []

@app.route('/', methods=['GET'])
def info():
    return jsonify({
        "nombre": "Sistema de Gestión de Usuarios y Productos",
        "version": "1.0",
        "autor": "GRR",
        "descripcion": "API para registrar usuarios y listar usuarios"
    })

@app.route('/crear_usuario', methods=['GET'])
def crear_usuario():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No se proporcionaron datos JSON"}), 400
    
    nombre = data.get('nombre')
    correo = data.get('correo')
    
    if not nombre or not correo:
        return jsonify({"error": "Se requieren los campos 'nombre' y 'correo'"}), 400
    
    nuevo_usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(nuevo_usuario)
    
    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}), 201

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
