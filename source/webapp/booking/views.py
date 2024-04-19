from flask import Blueprint, flash, render_template, redirect, url_for

from webapp.lib.db import db
from webapp.booking.forms import AddApartmensForm
from webapp.lib.models import Apartmens, ApartmensTypeChoice, PaymensTypeChoice

blueprint = Blueprint("apartmens", __name__, url_prefix="/users")


@blueprint.route("/apartmens")
def apartmens():
    title = "Apartmens add"
    form = AddApartmensForm()
    rent_options = [choice.value for choice in ApartmensTypeChoice]
    payment_options = [choice.value for choice in PaymensTypeChoice]
    return render_template(
        "booking/add_form_apart.html",
        page_title=title,
        form=form,
        rent_options=rent_options,
        payment_options=payment_options,
    )


@blueprint.route("add-apartmens", methods=["POST"])
def add_apartmens():
    form = AddApartmensForm()
    if form.validate_on_submit():
        # Получаем rent_type из формы
        rent_type = form.rent_type.data
        payment_type = form.payment_type.data
        # Подтверждаем, что выбранный rent_type является допустимым типом выбора
        if rent_type not in [choice.value for choice in ApartmensTypeChoice]:
            flash("Выбран не верный тип аренды")
            return redirect(url_for("apartmens.apartmens"))

        if payment_type not in [choice.value for choice in PaymensTypeChoice]:
            flash("Выбран не верный тип оплаты")
            return redirect(url_for("apartmens.apartmens"))

        new_apartmens = Apartmens(
            country=form.country.data,
            city=form.city.data,
            address=form.address.data,
            description=form.description.data,
            payment_type=payment_type,
            rent_type=rent_type,
            floor=form.floor.data,
            apartment_number=form.apartment_number.data,
            number_of_beds=form.number_of_beds.data,
            number_of_guests=form.number_of_guests.data,
            footege_room=form.footege_room.data,
        )
        db.session.add(new_apartmens)
        db.session.commit()
        flash("Обьявление отправлено на модерацию.")
        return redirect(url_for("intro.index"))
    flash("Заполните все поля или исправте ошибки в формате.")
    return redirect(url_for("apartmens.apartmens"))
