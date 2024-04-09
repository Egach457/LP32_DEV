from flask import  Blueprint, render_template, current_app

blueprint = Blueprint('cards', __name__)

@blueprint.route('/')
def index():
    title = "EasyNest"
    return render_template('cards/index.html', page_title=title)