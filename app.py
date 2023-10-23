from flask import Flask

app = Flask(__name__)

# Rutas y vistas
@app.route('/')
def index():
    return '¡Hola, mundo!'
