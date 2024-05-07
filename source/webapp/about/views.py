from flask import  Blueprint, render_template, current_app

blueprint = Blueprint('about', __name__)

@blueprint.route('/about')
def index():
    title = "EasyNest"
    return render_template('about/index.html', page_title=title)