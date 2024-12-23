from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


#Creamos una instancia llamada db la cual nos ayudara a establecer conexión con la base de datos
db= SQLAlchemy()

#CREAMOS UNA CLASE LLAMADA JWT LA CUAL NOS AYUDARA A MANEJAR TODOS LOS TOKENS
#QUE PASEN POR NUEESTRA API
jwt = JWTManager()
