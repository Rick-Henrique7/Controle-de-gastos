from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# --- Função para criar o banco e a tabela, se não existirem ---
def init_db():
    conn = sqlite3.connect("database.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS movimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            descricao TEXT,
            categoria TEXT,
            data TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Inicializa o banco
init_db()

# --- Função para conexão com o banco ---
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# --- Rotas ---
@app.route("/")
def index():
    conn = get_db_connection()
    movimentos = conn.execute("SELECT * FROM movimentos ORDER BY data DESC").fetchall()
    conn.close()
    return render_template("index.html", movimentos=movimentos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        tipo = request.form["tipo"]
        valor = request.form["valor"]
        descricao = request.form["descricao"]
        categoria = request.form["categoria"]
        data = request.form["data"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO movimentos (tipo, valor, descricao, categoria, data) VALUES (?, ?, ?, ?, ?)",
            (tipo, valor, descricao, categoria, data)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
