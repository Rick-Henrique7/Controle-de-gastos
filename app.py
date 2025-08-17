from flask import Flask
import sqlite3

app = Flask(__name__)

# --- Configuração do banco ---

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
    conn.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL
        )
    """)
    # Inserir categorias padrão se não existirem
    categorias_padrao = ["Alimentação", "Transporte", "Lazer", "Saúde", "Educação"]
    for cat in categorias_padrao:
        conn.execute("INSERT OR IGNORE INTO categorias (nome) VALUES (?)", (cat,))
    conn.commit()
    conn.close()


# --- Função para conexão com o banco ---
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# --- Importa as rotas e passa o app e get_db_connection ---
from routes import init_routes
init_routes(app, get_db_connection)

if __name__ == "__main__":
    app.run(debug=True)
