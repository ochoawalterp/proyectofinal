#Ejecuta todas las peticiones que se hagan a la BD

from .models.usuarios import User
from .models.preguntas import Preguntas
from flask_jwt_extended import create_access_token


from datetime import timedelta

def user_register(nombre, apellido,correo, password):

    #Buscar si el correo del usuario ya esta registrado
    usuario_existente = User.query.filter_by(correo= correo).first()

    if usuario_existente is not None:
        return {'error': 'El usuario ya esta registrado :-('}, 403

    #creamos un objeto de tipo User con los valores que el cliente solicito
    nuevo_usuario = User(nombre=nombre, apellido=apellido, correo=correo,password=password)

    #Este metodo  lo que hace es recibir la pass en texto plano, hashearla y guardarla
    # de nuestro objeto
    nuevo_usuario.hashear_password(password=password)

    #INVOCAMOS EL METODO SAVE QUE SE ENCARGA DE HACER TODO EL PROCESO PARA GUARDARLO EN MI BD
    nuevo_usuario.save()

    return{
        'status': 'Usuario registrado',
        'correo': correo,
        'nombre':nombre 
    }, 200
  

def user_pregunta(titulo, contenido, id_usuario):
    # Buscar si ya existe una pregunta con los mismos datos
    pregunta_existente = Preguntas.query.filter_by(titulo=titulo, contenido=contenido, id_usuario=id_usuario).first()

    if pregunta_existente is not None:
        return {'error': 'La pregunta ya existe'}, 400

    # Creamos un nuevo objeto Preguntas
    nueva_pregunta = Preguntas(titulo=titulo, contenido=contenido, id_usuario=id_usuario)

    # Guardamos la nueva pregunta en la base de datos
    nueva_pregunta.save()

    return {
        'status': 'Pregunta registrada',
        'titulo': titulo,
        'contenido': contenido,
        'id_usuario': id_usuario
    }, 201












#Esta funcion se encarga de hacer el login en nuestra API
def user_login(correo,password):

#Tenemos que verificar que el usuario al que se esta intentando logear existe

#En mi base de datos se va a buscar or el correo que el cliente haua mandadp
    usuario_existente = User.query.filter_by(correo=correo).first()
#ESTE COMANDO DE ARRIBA REGRESA 1 DE DOS VALORES

#1 Si encuentra una cooincidencia la muestra
 
#2 SI NO ENCUETRA NADA REGRESA NONE.


#Esta condicional determina si mi usario esta registrado en la BD
    if usuario_existente is None:
    #Si el correo no esta registrado en mi DB arrojamos un error
        return {'Status': 'El correo o la contraseña esta mal :( '}, 400

    #Verificamos que la contrasenia coninciad con la que esta en la DB(TRUE O FALSE)
    elif usuario_existente.verificar_password(password = password):
        
        caducidad = timedelta(minutes= 1000)
        
        #Le creamos un token de acceso
        token_acceso = create_access_token(identity= usuario_existente.nombre,expires_delta=caducidad)



        #Retornamos un mensaje sesion iniciada y el token que generamos
        return{'Status': 'Sesión iniciada',
               'Token': token_acceso               
               }, 200
    
    
    #Si no coincide entonces le arrojamos un error al usuario
    else:
        return {'Status': 'El correo o la contraseña esta mal :('},400
