# En el archivo routes nosotros vamos a tener las rutas (paths)
# que el servidor va a poder manejar
from flask import Flask, jsonify
from flask_restful import Resource
from flask import request, render_template, make_response,redirect,url_for #<- Nos permite interceptar la info del usuario
from .methods import user_register
from .methods import user_login
from .models.preguntas import Preguntas
 
from flask_jwt_extended import jwt_required

from .extensions import db

app = Flask(__name__)
# # Creamos un recurso que nuestra aplicación puede cargar (METODO)
class HolaMundo(Resource):
   # Este método se ejecuta cuando el usuario lo llama con un GET
  def get(self):
    pagina = render_template('index.html')
    respuesta= make_response(pagina)

    return respuesta

#   def post(self):
#     data = {
#       'nombre': 'Walter',
#       'edad': 23,
#       'signo': 'Geminis'

#     }
#     return data
  

# class Prueba(Resource):
#   def get(self):
# #         # Renderiza el HTML inicial
#       pagina = render_template('prueba.html')
#       respuesta= make_response(pagina)
#       return respuesta

#   def post(self):
# #         # Información que se enviará al cliente
#     cursos = {
#              'nombre': 'Manolo',
#              'edad': 50,
#              'signo': 'Janpier'
#             }
#     return cursos  # Devuelve el JSON



    


class Mostrar_preguntas(Resource):
  def get(self):
         # Obtiene todas las preguntas de la base de datos
    preguntas = Preguntas.query.all()
     # Transforma las preguntas a un formato adecuado
    lista_preguntas = [
             {
                 'titulo': pregunta.titulo,
                 'contenido': pregunta.contenido,
                 'id_usuario': pregunta.id_usuario
             }
             for pregunta in preguntas
         ]

    datos = {
             'titulo': 'Listado de Preguntas',
             'bienvenida': 'Bienvenido',
             'preguntas': lista_preguntas,
             'num_preguntas': len(lista_preguntas)
         }
    print(datos)
         # Renderiza el HTML
    pagina = render_template('index.html', **datos)
    respuesta = make_response(pagina)
    return respuesta
    
class Obtener_bd(Resource):
  # Como el usuario envia información utilizamos un post
  def get(self):
    # Información que el usario envia a través del post
    user_info = request.form
    username = user_info.get('nombre')
    email = user_info.get('correo')



 







class Registro(Resource):
  # Como el usuario envia información utilizamos un post
  def post(self):
    # Información que el usario envia a través del post
    user_info = request.form
    usuario = user_info.get('nombre')
    apellido = user_info.get('apellido')
    correo = user_info.get('correo')
    password = user_info.get('password')

    respuesta, status = user_register(usuario,apellido,correo,password)

    #return respuesta, status
    return respuesta ,status

# Van a crear un recurso para el login, le van a asigar una ruta y su servidor tiene que recibir
# la siguiente información del cliente: "correo" y "contraseña"
class Login(Resource):

  def get(self):
    pagina = render_template('login.html')
    respuesta= make_response(pagina)

    return respuesta


  # Como el usuario envia información utilizamos un post
  def post(self):
    # Información que el usario envia a través del post
    user_info = request.form
    correo = user_info.get('correo')
    password = user_info.get('password')
    respuesta, status = user_login(correo,password)
    return respuesta, status

  # def prueba(self):
  #   return render_template('layout.html')

#Un recurso que se ejecuta cuando el usuario accede a la ruta  "/restringido"
class Restringido(Resource):
  
  @jwt_required()#Verificamos si mi usuario esta autorizado
  def get(self):
    pagina = render_template('restringido.html')
    respuesta= make_response(pagina)


    return respuesta


# Simplemente se va a encargar de darle rutas a mis recursos
class APIRoutes:
  def init_api(self, api):
    api.add_resource(HolaMundo, '/')
    api.add_resource(Registro, '/registro')
    api.add_resource(Login, '/login')
    api.add_resource(Restringido, '/restringido')
    api.add_resource(Mostrar_preguntas, '/index')
   