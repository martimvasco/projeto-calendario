from flask import Flask, render_template, request, redirect
from datetime import datetime

from models.event import Event
from models.category import Category
from models.calendar_manager import CalendarManager

app = Flask(__name__)
manager = CalendarManager()

categoria_default = Category(1, "Geral", "Categoria padrão")


@app.route("/")
def index():
    return render_template("index.html", eventos=manager.eventos)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    evento = Event(
        len(manager.eventos) + 1,
        request.form["titulo"],
        request.form["descricao"],
        datetime.fromisoformat(request.form["data_inicio"]),
        datetime.fromisoformat(request.form["data_fim"]),
        request.form["prioridade"],
        categoria_default
    )

    manager.adicionar_evento(evento)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
