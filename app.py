from flask import Flask
from config import Config
from models import db  # Importamos la base de datos inicializada
from routes import init_routes  # Importamos las rutas

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos con la app
db.init_app(app)

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

# Registrar las rutas
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
