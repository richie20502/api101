from models.usuario import Usuario
from models import db

def obtener_usuarios():
    return Usuario.query.all()

def agregar_usuario(nombre, email):
    nuevo_usuario = Usuario(nombre=nombre, email=email)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return "Usuario agregado correctamente"
