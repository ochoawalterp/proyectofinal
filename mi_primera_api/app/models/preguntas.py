# Importamos la variable que hace referencia a mi base de datos
from app.extensions import db
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


class Preguntas(db.Model):
    __tablename__ = 'pregunta' # -< indica a que tabla hace referencia este modelo esto en la bd
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String, nullable=False)
    contenido = db.Column(db.String, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)


      # Validación básica
   

    def save(self):
        # Guarda el objeto en la base de datos
        db.session.add(self)
        db.session.commit()

    

    

    #La contraseña que nos manda el usuaruio le llega a la funcion generete_password_hash
    # Esta funcion encripta la contraseña y el hash creado lo guarda en el atributo password
    # que es el que le llega a la BD

    # def hashear_password(self,password):
    #     self.password = generate_password_hash(password)


    # esta funcion recibe la contraseña en texto plano y la compara con el hash que esta 
    #almacenado en la BD, SI CONSIDE NOS REGRESA UN TRUE Y SI NO UN FALSE
    # def verificar_password(self, password):
    #     return check_password_hash(self.password, password)

    




#METODO DE LA CLASE USER
    # def save(self):
        #CREA UNA SESION CON MI BASE DE DATOS
        # db.session.add(self)

        #EN ESA CONESXION GUARDAMOS LOS CAMBIOS Y LA CERRAMOS
        # db.session.commit()

    # def delete(self):
        #abre una sesion con mi db
        # db.session.delete(self)

        #SE GUARDAN LOS CAM BIOS Y SE CIERRA LA CONEXION
        # db.session.commit()