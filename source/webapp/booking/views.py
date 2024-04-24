from flask import Blueprint, flash, render_template, redirect, url_for

from webapp.lib.db import db
from webapp.booking.forms import AddApartmensForm
from webapp.lib.models import (
    Apartmens,
    ApartmensTypeChoice,
    PaymensTypeChoice,
    Comfort,
    Propertie,
)

blueprint = Blueprint("apartmens", __name__, url_prefix="/users")


# TODO: пускать пользователя к форме через проверку юзера
@blueprint.route("/apartmens")
def apartmens():
    title = "Apartmens add"
    form = AddApartmensForm()
    rent_options = [(choice.name, choice.value) for choice in ApartmensTypeChoice]
    payment_options = [(choice.name, choice.value) for choice in PaymensTypeChoice]
    print(rent_options)
    print(payment_options)
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
        if rent_type not in [choice.name for choice in ApartmensTypeChoice]:
            flash("Выбран не верный тип аренды")
            return redirect(url_for("apartmens.apartmens"))

        if payment_type not in [choice.name for choice in PaymensTypeChoice]:
            flash("Выбран не верный тип оплаты")
            return redirect(url_for("apartmens.apartmens"))

        apartmens = Apartmens(
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
            room_area=form.room_area.data,
        )
        try:
            db.session.add(apartmens)
            db.session.commit()
        except Exception as e:
            flash(f"Ошибка ввода: {str(e)}")
            db.session.rollback()
            return redirect(url_for("apartmens.apartmens"))

            comfort = Comfort(
                apartmens_id=apartmens.id,
                wi_fi=form.wi_fi.data,
                hair_dryer=form.hair_dryer.data,
                towels=form.towels.data,
                balcony=form.balcony.data,
                air_conditioner=form.air_conditioner.data,
                tv=form.tv.data,
            )
            db.session.add(comfort)
            db.session.commit()

        propertie = Propertie(
            apartmens_id=apartmens.id,
            no_children=form.no_children.data,
            no_parties=form.no_parties.data,
            no_smoking=form.no_smoking.data,
            no_pets=form.no_pets.data,
        )
        db.session.add(propertie)
        db.session.commit()
        flash("Обьявление отправлено на модерацию.")
        return redirect(url_for("intro.index"))
    flash(f"Заполните все поля или исправте ошибки в формате. {form.errors}")
    return redirect(url_for("apartmens.apartmens"))
