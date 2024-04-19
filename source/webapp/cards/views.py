from flask import  Blueprint, render_template, current_app
from lib.models import Apartmens
from sqlalchemy import func
from lib.db import db_session

blueprint = Blueprint('cards', __name__)

@blueprint.route('/')
def index():
    title = "EasyNest"
    cards = db_session.query(Apartmens).order_by(func.random()).limit(6).all()
    cards_list = [
    {"id": apartment.id, "country": apartment.country, "city": apartment.city,
     "address": apartment.address, "title": apartment.title,
     "description": apartment.description}
    for apartment in cards
    ]
    return render_template('cards/index.html', page_title=title, cards_list=cards_list)