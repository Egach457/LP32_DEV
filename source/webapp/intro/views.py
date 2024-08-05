from flask import Blueprint, render_template
from webapp.booking_list.models import ShowAnnouncement
from webapp.pydrive.drive import get_photo
from werkzeug.wrappers import Response


blueprint = Blueprint("intro", __name__)


@blueprint.route("/")
def index() -> str | Response:
    title = "EasyNest"
    cards = ShowAnnouncement().show()
    cards_list = [
        {
            "id": apartment.id,
            "country": apartment.country,
            "city": apartment.city,
            "address": apartment.address,
            "title": apartment.title,
            "description": apartment.description,
            "image_path": get_photo(apartment.id),
        }
        for apartment in cards
    ]
    return render_template("cards.html", page_title=title, cards_list=cards_list)
