from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data/eventos.json"


# ---------- Helpers ----------
def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_events(events):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)


def next_id(events):
    if not events:
        return 1
    return max(e["id"] for e in events) + 1


# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def index():
    eventos = load_events()

    if request.method == "POST":
        novo_evento = {
            "id": next_id(eventos),
            "titulo": request.form["titulo"],
            "descricao": request.form.get("descricao", ""),
            "data_inicio": request.form["data_inicio"],
            "data_fim": request.form["data_fim"],
            "prioridade": request.form["prioridade"],
        }

        eventos.append(novo_evento)
        save_events(eventos)
        return redirect(url_for("index"))

    return render_template("index.html", eventos=eventos)


@app.route("/remover/<int:evento_id>", methods=["POST"])
def remover(evento_id):
    eventos = load_events()
    eventos = [e for e in eventos if e["id"] != evento_id]
    save_events(eventos)
    return redirect(url_for("index"))


@app.route("/editar/<int:evento_id>", methods=["GET", "POST"])
def editar(evento_id):
    eventos = load_events()
    evento = next((e for e in eventos if e["id"] == evento_id), None)

    if not evento:
        return redirect(url_for("index"))

    if request.method == "POST":
        evento["titulo"] = request.form["titulo"]
        evento["descricao"] = request.form.get("descricao", "")
        evento["data_inicio"] = request.form["data_inicio"]
        evento["data_fim"] = request.form["data_fim"]
        evento["prioridade"] = request.form["prioridade"]

        save_events(eventos)
        return redirect(url_for("index"))

    return render_template("index.html", eventos=eventos, evento_editar=evento)


if __name__ == "__main__":
    app.run(debug=True)
