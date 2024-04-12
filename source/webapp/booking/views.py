from flask import  Blueprint, render_template, current_app

blueprint = Blueprint('booking', __name__)

@blueprint.route('/booking')
def index():
    title = "EasyNest"
    return render_template('booking/index.html', page_title=title)