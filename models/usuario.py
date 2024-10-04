from  models import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(50), nullable= False)
    email = db.Column(db.String(50), nullable= False, unique= True)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'