from flask import Blueprint, render_template

blueprint = Blueprint("intro", __name__)

@blueprint.route("/")
def index():
    title = "Первая страница"
    return render_template("intro/index.html", page_title=title)

