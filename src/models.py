from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)    
    
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
    
class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)

    planeta_id = db.Column(db.Integer, db.ForeignKey("planetas.id"))
    planeta = db.relationship("Planetas", backref='users', lazy=True)

    personaje_id = db.Column(db.Integer, db.ForeignKey("personajes.id"))
    personaje = db.relationship("Personajes", backref='users', lazy=True)

    nave_id = db.Column(db.Integer, db.ForeignKey("naves.id"))
    nave = db.relationship("Naves", backref='users', lazy=True)    

class Planetas(db.Model):
    __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    diametro = db.Column(db.Integer)
    clima = db.Column(db.String(200))

    def __repr__(self):
        return '<Planetas %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diametro": self.diametro,
            "clima": self.clima
        }

class Personajes(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    altura = db.Column(db.Integer)
    peso = db.Column(db.Integer)    
    color_piel = db.Column(db.String(200))

    def __repr__(self):
        return '<Personajes %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "altura": self.altura,
            "peso": self.peso,
            "color_piel": self.color_piel
        }
    
class Naves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    modelo = db.Column(db.String(200))
    capacidad_tripulacion = db.Column(db.Integer)
    carga = db.Column(db.Integer)
    clase = db.Column(db.String(200))

    def __repr__(self):
        return '<Naves %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "modelo": self.modelo,
            "capacidad_tripulacion": self.capacidad_tripulacion,
            "carga": self.carga            
        }
