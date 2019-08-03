import flask

from flask import Flask, render_template, send_from_directory
from typing import Optional

import mrater.data as data


app = Flask(__name__, static_url_path="/static")


@app.route("/favicon.ico")
def get_favicon():
    return "", 404


@app.route("/done")
def get_finished():
    return render_template("done.html")


@app.route("/next", defaults={"page": None}, methods=["POST"])
@app.route("/next/<int:page>", methods=["GET"])
def next_page(page: Optional[int]):
    if flask.request.method == "POST":
        document = flask.request.get_json()

        # Here are the data that could be used:
        # print("Main item id =", document.get("id"))
        # print("Sorted recommended items id =", document.get("sorted"))
        # print("Current page =", document.get("page"))
        # For instance, something like that could be done:
        # data.update(seed=document.get("id"), recommendations=document.get("sorted"))

        page = int(document.get("page", "0")) + 1
        next_page = "/next/{page}".format(page=page) if page <= 1 else "/done"
        return {"next": next_page}
    else:
        page = page or 0
        if page > 1:
            return get_finished()

        pair = data.load(page)
        if pair is None:
            pair = data.load(0)

        (main, all) = pair  # type: ignore
        last_page = page >= 1

        return render_template(
            "index.html", title="Awesome title", main=main, all=all, page=page, last_page=last_page
        )


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def get_index(path: Optional[str]):
    return render_template("start.html", first_page="/next/0")


@app.route("/img/<path:path>")
def send_static(path: Optional[str]):
    return send_from_directory("static/img", path)
