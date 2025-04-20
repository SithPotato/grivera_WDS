from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/productos')
def productos():
    lista_productos = [
        {"nombre": "Jugo detox", "precio": 50},
        {"nombre": "Té de hierbas", "precio": 30},
        {"nombre": "Miel natural", "precio": 80}
    ]
    return render_template('productos.html', productos=lista_productos)

@main.route('/clientes')
def clientes():
    lista_clientes = [
        {"nombre": "Juan Pérez", "membresia": "Oro"},
        {"nombre": "Ana Gómez", "membresia": "Plata"}
    ]
    return render_template('clientes.html', clientes=lista_clientes)
