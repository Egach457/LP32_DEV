import os

from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, login_required, current_user, login_user, logout_user

from webapp.forms import LoginForm
from lib.models import User
from lib.db import db
from lib.config import CONFIG_APP

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(CONFIG_APP)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        title = "Первая страница"
        return render_template("index.html", page_title=title)


    @app.route("/login")
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("index"))

        title = "Login"
        login_form = LoginForm()
        return render_template("login.html", page_title=title, form=login_form)


    @app.route("/process-login", methods=["POST"])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            email = User.query.filter(User.email == form.email.data).first()
            if email and email.check_password(form.password.data):
                login_user(email)
                flash("Вошли на сайт")
                return redirect(url_for("index"))
        
        flash("Неправильно имя или пароль")
        return redirect(url_for("login"))


    @app.route("/logout")
    def logout():
        logout_user()
        flash("Вы успешно разлогинились")
        return redirect(url_for('index'))

    @app.route("/admin")
    @login_required
    def admin_index():
        if current_user.is_admin:
            return "Доступ для admin"
        else:
            return "Нет доступа admin"



    return app


