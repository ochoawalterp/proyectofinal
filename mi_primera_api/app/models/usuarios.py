# Importamos la variable que hace referencia a mi base de datos
from app.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'usuario' # -< indica a que tabla hace referencia este modelo esto en la bd
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable =False)
    password = db.Column(db.Text(),nullable = False)




    # class Usuarios(db.Model):
    # __tablename__ = 'usuarios'
    # id = db.Column(db.Integer, primary_key=True)
    # nombre = db.Column(db.String, nullable=False)
    # preguntas = db.relationship('Preguntas', backref='usuario', lazy=True)


    #La contraseña que nos manda el usuaruio le llega a la funcion generete_password_hash
    # Esta funcion encripta la contraseña y el hash creado lo guarda en el atributo password
    # que es el que le llega a la BD

    def hashear_password(self,password):
        self.password = generate_password_hash(password)


    # esta funcion recibe la contraseña en texto plano y la compara con el hash que esta 
    #almacenado en la BD, SI CONSIDE NOS REGRESA UN TRUE Y SI NO UN FALSE
    def verificar_password(self, password):
        return check_password_hash(self.password, password)


#METODO DE LA CLASE USER
    def save(self):
        #CREA UNA SESION CON MI BASE DE DATOS
        db.session.add(self)

        #EN ESA CONESXION GUARDAMOS LOS CAMBIOS Y LA CERRAMOS
        db.session.commit()

    def delete(self):
        #abre una sesion con mi db
        db.session.delete(self)

        #SE GUARDAN LOS CAMBIOS Y SE CIERRA LA CONEXION
        db.session.commit()