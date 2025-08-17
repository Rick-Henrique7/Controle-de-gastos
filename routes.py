from flask import render_template, request, redirect, url_for

def init_routes(app, get_db_connection):

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
