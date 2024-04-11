from flask import Blueprint, render_template

blueprint = Blueprint("intro", __name__)

@blueprint.route("/")
def index():
    title = "Daily Rent"
    return render_template("base_intro.html", page_title=title)
