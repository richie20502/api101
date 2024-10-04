from models.usuario import Usuario
from models import db

def obtener_usuario():
    return Usuario.query.all()