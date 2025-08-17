from flask import render_template, request, redirect, url_for
from app import app, db
from models import Movimento

@app.route("/")
def index():
    movimentos = Movimento.query.all()
    return render_template("index.html", movimentos=movimentos)

@app.route("/add", methods=["POST"])
def add_movimento():
    tipo = request.form["tipo"]
    valor = float(request.form["valor"])
    descricao = request.form["descricao"]
    categoria = request.form["categoria"]

    novo = Movimento(tipo=tipo, valor=valor, descricao=descricao, categoria=categoria)
    db.session.add(novo)
    db.session.commit()
    return redirect(url_for("index"))
