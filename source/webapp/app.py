from flask import Flask, render_template, flash, redirect, url_for
from cards.views import blueprint as cards_blueprint





def create_app():
    app = Flask(__name__)
    #app.config.from_pyfile('config.py')

    app.register_blueprint(cards_blueprint)
    
    

    




    return app