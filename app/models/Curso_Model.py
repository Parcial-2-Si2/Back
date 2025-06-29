from app import db

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    Paralelo = db.Column(db.String(255))
    Turno = db.Column(db.String(255))
    Nivel = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))

    materias = db.relationship('MateriaCurso', back_populates='curso', lazy=True)
