from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planeta_id = db.Column(db.Integer)
    name = db.Column(db.String(200))
    diametro = db.Column(db.Integer)
    clima = db.Column(db.String(200))

class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    altura = db.Column(db.Integer)
    peso = db.Column(db.Integer)
    color_piel = db.Column(db.String(200))

class Vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    modelo = db.Column(db.String(200))
    velocidad = db.Column(db.Integer)
    color = db.Column(db.String(200))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }