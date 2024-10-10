from models.usuario import Usuario
from models import db

def obtener_usuario():
    return Usuario.query.all()

def agregar_usuario(data):
    nuevo_usuario = Usuario(nombre= data['nombre'], email= data['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return "Usuario agregado correctamente"



def actualizar_usuario(id,data):
    usuario = Usuario.query.get(id)
    print("usuaro query")
    print(usuario.nombre)
    print(usuario.email)
    if usuario:
        usuario.nombre = data['nombre']
        usuario.email = data['email']
        print('update usuario')
        print(usuario.nombre)
        print(usuario.email)
        db.session.commit()
        return "Usuario actualizado correctamente"
    else:
        return "Usuario no encontrado"
    
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return "Usuario eliminado correctamente"
    else:
        return "Usuario no encontrado"