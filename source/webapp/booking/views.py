from flask import  Blueprint, render_template, current_app
from lib.models import Apartmens

blueprint = Blueprint('booking', __name__)

@blueprint.route('/booking')
def index():
    title = "EasyNest"
    apartment = Apartmens.query.get_or_404(apartmens_id)
    return render_template('booking/index.html', page_title=title, apartment=apartment )