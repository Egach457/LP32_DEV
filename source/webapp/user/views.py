from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from webapp.lib.db import db
from webapp.lib.models import User
from webapp.user.forms import LoginForm, RegistrationForm
from werkzeug.wrappers import Response


blueprint = Blueprint("user", __name__, url_prefix="/users")


@blueprint.route("/login")
def login() -> str | Response:
    if current_user.is_authenticated:
        return redirect(url_for("intro.index"))

    title = "Login"
    login_form = LoginForm()
    return render_template("user/login.html", page_title=title, form=login_form)


# Изменил redirect(intro.index)
@blueprint.route("/process-login", methods=["POST"])
def process_login() -> str | Response:
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter(User.email == form.email.data).first()
        if email and email.check_password(form.password.data):
            login_user(email, remember=form.remember_me.data)
            flash("Вошли на сайт")
            return redirect(url_for("intro.index"))

    flash("Неправильно имя или пароль")
    return redirect(url_for("user.login"))


@blueprint.route("/logout")
def logout() -> str | Response:
    logout_user()
    flash("Вы успешно разлогинились")
    return redirect(url_for("intro.index"))


@blueprint.route("/register")
def register() -> str | Response:
    if current_user.is_authenticated:
        return redirect(url_for("intro.index"))
    title = "Registration"
    form = RegistrationForm()
    return render_template("user/registration.html", page_title=title, form=form)


@blueprint.route("/process-reg", methods=["POST"])
def process_reg() -> str | Response:
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone=form.phone.data,
            email=form.email.data,
            role="user",
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        # BUG: нет оповещения. Появляется на другой странице.
        flash("Вы успешно зарегистрировались")
        return redirect(url_for("intro.index"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Ошибка в поле {}: {}".format(getattr(form, field).label.text, error))
        return redirect(url_for("user.register"))
