from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route('', methods=['GET'])
def info():
    return jsonify({
        "nombre": "Capstone API",
        "version": "1.0",
        "descripcion": "Servidor Flask con rutas básicas"
    })

@app.route('/', methods=['POST'])
def mensaje():
    data = request.get_json()
    if not data or 'mensaje' not in data:
        return jsonify({"error": "Falta el campo 'mensaje'"}), 400

    mensaje_recibido = data['mensaje']
    respuesta = f"Hola, recibí tu mensaje: '{mensaje_recibido}'"
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)