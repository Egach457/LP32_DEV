from flask import Flask, render_template, flash, redirect, url_for
from cards.views import blueprint as cards_blueprint
from about.views import blueprint as about_blueprint
from booking.views import blueprint as booking_blueprint





def create_app():
    app = Flask(__name__, static_folder='static')
    #app.config.from_pyfile('config.py')

    app.register_blueprint(cards_blueprint)
    app.register_blueprint(about_blueprint)
    app.register_blueprint(booking_blueprint)
    
    

    




    return app