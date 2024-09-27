from flask import Flask
from routes import init_routes

app = Flask(__name__)

# Registrar todas las rutas
init_routes(app)

@app.route('/')
def home():
    return {
        "message": "Bienvenido a la API de Flask DSM 101"
    }

if __name__ == '__main__':
    app.run(debug=True)
