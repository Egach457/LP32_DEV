from flask import  Blueprint, render_template, current_app
from webapp.lib.models import Apartmens, Propertie, Comfort

blueprint = Blueprint('booking_list', __name__)

@blueprint.route('/booking_list')
def index():
    title = "Ваши объявления"

    return render_template('booking_list/index.html', page_title=title)