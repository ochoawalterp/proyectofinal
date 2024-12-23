
from app.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class Preguntas(db.Model):
    __tablename__ = 'usuario' # -< indica a que tabla hace referencia este modelo esto en la bd
    id = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, nullable=False)
    id_pregunta = db.Column(db.Integer, nullable=False)
    contenido = db.Column(db.String, nullable =False)
