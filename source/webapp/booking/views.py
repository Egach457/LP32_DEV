from flask import Blueprint, flash, render_template, redirect, url_for

from webapp.lib.db import db
from webapp.booking.forms import AddApartmensForm
from webapp.lib.models import Apartmens, ApartmensTypeChoice

blueprint = Blueprint("apartmens", __name__, url_prefix="/users")

@blueprint.route("/apartmens")
def apartmens():
    title = "Apartmens add"
    form = AddApartmensForm()
    return render_template("booking/add_form_apart.html", page_title=title, form=form)

@blueprint.route("add-apartmens", methods=["POST"])
def add_apartmens():
    form = AddApartmensForm()
    if form.validate_on_submit():
        new_apartmens = Apartmens(
            country=form.country.data,
            city=form.city.data,
            address=form.address.data,
            description=form.description.data,
            rent_type=form.rent_type.data,
            payment_type=form.payment_type.data
        )
        db.session.add(new_apartmens)
        db.session.commit()
        flash("Обьявление отправлено на модерацию.")
        return redirect(url_for("intro.index"))
    flash("Заполните все поля или исправте ошибки в формате.")
    return redirect(url_for("apartmens.apartmens"))
