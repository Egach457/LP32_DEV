from flask import Blueprint, render_template
from sqlalchemy import func
from webapp.lib.db import db_session
from webapp.lib.models import Apartmens

blueprint = Blueprint("intro", __name__)


@blueprint.route("/")
def index():
    title = "EasyNest"
    cards = db_session.query(Apartmens).order_by(func.random()).limit(6).all()
    cards_list = [
        {
            "id": apartment.id,
            "country": apartment.country,
            "city": apartment.city,
            "address": apartment.address,
            "title": apartment.title,
            "description": apartment.description,
        }
        for apartment in cards
    ]
    return render_template("cards.html", page_title=title, cards_list=cards_list)
