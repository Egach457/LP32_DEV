import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from webapp.about.views import blueprint as about_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.booking.views import blueprint as booking_blueprint
from webapp.booking_list.views import blueprint as booking_list
from webapp.card_details.views import blueprint as card_details_blueprint
from webapp.intro.views import blueprint as intro_blueprint
from webapp.lib.db import db
from webapp.lib.models import User
from webapp.user.views import blueprint as user_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    load_dotenv()
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    db.init_app(app)
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user.login"

    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(intro_blueprint)
    app.register_blueprint(booking_blueprint)
    app.register_blueprint(about_blueprint)
    app.register_blueprint(card_details_blueprint)
    app.register_blueprint(booking_list)

    @login_manager.user_loader
    def load_user(user_id: int) -> User:
        return User.query.get(user_id)

    return app
