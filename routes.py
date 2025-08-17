from flask import render_template, request, redirect, url_for
from datetime import datetime

def init_routes(app, get_db_connection):

    @app.route("/")
    def index():
        categoria = request.args.get("categoria")
        mes = request.args.get("mes")
        ano = request.args.get("ano")

        query = "SELECT * FROM movimentos WHERE 1=1"
        params = []

        if categoria:
            query += " AND categoria=?"
            params.append(categoria)
        if mes:
            query += " AND strftime('%m', data)=?"
            params.append(f"{int(mes):02d}")
        if ano:
            query += " AND strftime('%Y', data)=?"
            params.append(ano)

        query += " ORDER BY data DESC"

        conn = get_db_connection()
        movimentos = conn.execute(query, params).fetchall()
        conn.close()

        # Definir mês e ano padrão para o link do relatório
        now = datetime.now()
        mes_link = mes if mes else f"{now.month:02d}"
        ano_link = ano if ano else str(now.year)

        return render_template(
            "index.html",
            movimentos=movimentos,
            categoria=categoria,
            mes=mes,
            ano=ano,
            mes_link=mes_link,
            ano_link=ano_link
        )

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

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit(id):
        conn = get_db_connection()
        movimento = conn.execute("SELECT * FROM movimentos WHERE id = ?", (id,)).fetchone()

        if request.method == "POST":
            tipo = request.form["tipo"]
            valor = request.form["valor"]
            descricao = request.form["descricao"]
            categoria = request.form["categoria"]
            data = request.form["data"]

            conn.execute(
                "UPDATE movimentos SET tipo=?, valor=?, descricao=?, categoria=?, data=? WHERE id=?",
                (tipo, valor, descricao, categoria, data, id)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

        conn.close()
        return render_template("edit.html", movimento=movimento)

    @app.route("/delete/<int:id>", methods=["POST"])
    def delete(id):
        conn = get_db_connection()
        conn.execute("DELETE FROM movimentos WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    @app.route("/relatorio", methods=["GET"])
    def relatorio():
        mes = request.args.get("mes")
        ano = request.args.get("ano")

        if not mes or not ano:
            now = datetime.now()
            mes = f"{now.month:02d}"
            ano = str(now.year)

        conn = get_db_connection()
        movimentos = conn.execute(
            "SELECT * FROM movimentos WHERE strftime('%m', data)=? AND strftime('%Y', data)=?",
            (mes, ano)
        ).fetchall()

        # Calcula totais
        total_receitas = sum(m['valor'] for m in movimentos if m['tipo'].lower() == 'receita')
        total_despesas = sum(m['valor'] for m in movimentos if m['tipo'].lower() == 'despesa')
        saldo = total_receitas - total_despesas

        # Monta dicionário de categorias para gráfico
        categorias = {}
        for m in movimentos:
            if m['tipo'].lower() == 'despesa':
                cat = m['categoria'] or "Sem Categoria"
                categorias[cat] = categorias.get(cat, 0) + m['valor']

        conn.close()

        # Passa categorias para o template usando tojson
        return render_template(
            "relatorio.html",
            mes=mes,
            ano=ano,
            total_receitas=total_receitas,
            total_despesas=total_despesas,
            saldo=saldo,
            categorias=categorias  # no template usar {{ categorias | tojson | safe }}
        )
