# se va a encargar de montar el servidor

#flask (f minuscula) es la libreria 
#  Flask (F mayuscula) es el modulo
from flask import Flask, jsonify #<-nos permite crear el servidor
from flask_restful import Api # <-nos permite crear la funcionalidad de API
#cuando importamos un archivo dentro de otro se le coloca el punto
from .routes import APIRoutes
#DESDE EL ARCHIVO CONFIG IMPORTAMOS LA CLASE CONFIG
from .config import Config
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError
#DESDE EL ARCHIVO EXTENSIONS IMPORTAMOS LA VARIABLE BD siempre poner el . 
from .extensions import db, jwt
#Creamos una funcion que configure el servidor

def configurar_app():
    #Almacena el Servidor 
    app = Flask(__name__)
    # LE INDICO A MI APP QUE COMO ARCHIVO DE CONFIGURACION UTILICE CONFIG
    app.config.from_object(Config)
    #LE DECIMOS A MI BASE DE DATOS QUE SE VA A INICIALIZAR EN NUESTRA APP
    db.init_app(app)

    #le decunis a hwt qye se v a a inicializar en nuestra app
    jwt.init_app(app)

    #SE EJECUTA MIENTRAS EL SERVIDOR SE ESTA MONTANDO
    with app.app_context():
        #INICIALIZA TODAS LAS TABLAS DE NUESTRA BASE DE DATOS
        db.create_all()


    #varible que almacena la API
    # Le indicamos sobre que servidor va a interacturar
    api = Api(app)

    # CONFIGURAMOS LAS RUTAS Y LOS RECURSOS
    rutas = APIRoutes()
    rutas.init_api(api)

    @app.errorhandler(NoAuthorizationError)
    def manejar_no_token(error):
        return jsonify( {
            'Mensaje': 'Necesitas un Token para acceder',
            'Error': str(error)

        }),401

    @app.errorhandler(InvalidHeaderError)
    def manejar_token_invalido(error):

        return jsonify({
            'Mensaje':'Token Invalido o mal formado',
            'Error':str(error)
        }),422

    @jwt.expired_token_loader
    def manejar_token_expirado(jwt_header,jwt_payload):
        return jsonify({
            'Mensaje': 'El token ya expiro',
            'Error': 'Token_expired'
        }),401

    return app

