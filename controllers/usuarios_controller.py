from models.usuario import Usuario
from models import db

def obtener_usuario():
    return Usuario.query.all()

def agregar_usuario(data):
    nuevo_usuario = Usuario(nombre= data['nombre'], email= data['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return "Usuario agregado correctamente"