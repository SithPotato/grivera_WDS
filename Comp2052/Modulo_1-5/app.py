from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "app": "Servidor Flask Básico",
        "version": "1.0",
        "author": "Gabriel"
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    
    if mensaje:
        respuesta = f"Recibí tu mensaje: {mensaje}"
        return jsonify({"respuesta": respuesta})
    else:
        return jsonify({"error": "No se recibió ningún mensaje"}), 400

# Ruta principal para cargar la página web
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
