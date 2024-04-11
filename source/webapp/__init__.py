from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from flask_migrate import Migrate


from webapp.intro.views import blueprint as intro_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.booking.views import blueprint as booking_blueprint
from webapp.user.models import User
from webapp.lib.db import db
from webapp.lib.config import CONFIG_APP

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(CONFIG_APP)
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user.login"

    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(intro_blueprint)
    app.register_blueprint(booking_blueprint)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    return app
