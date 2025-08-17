from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Movimento(db.Model):
    __tablename__ = "movimentos"  # garante o nome da tabela
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # Ex: "Entrada" ou "Saída"
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200))
    categoria = db.Column(db.String(100))
    data = db.Column(db.Date, default=date.today, nullable=False)

    def __repr__(self):
        return f"<Movimento {self.id} - {self.tipo} - {self.valor}>"
