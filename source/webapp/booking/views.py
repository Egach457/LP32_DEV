import os

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from webapp.booking.forms import AddApartmensForm
from webapp.lib.db import db
from webapp.lib.models import Apartmens, ApartmensTypeChoice, Comfort, PaymensTypeChoice, Payment, Propertie
from webapp.pydrive.custom_temp.create_custom_temp_dir import create_custom_temp_dir
from webapp.pydrive.drive import upload_photo
from werkzeug.utils import secure_filename
from werkzeug.wrappers import Response


blueprint = Blueprint("apartmens", __name__, url_prefix="/users")


@blueprint.route("/apartmens")
@login_required
def apartmens() -> str:
    title = "Создание объявления"
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
def add_apartmens() -> Response:
    form = AddApartmensForm()
    if form.validate_on_submit():

        # Получаем rent_type из формы
        rent_type: str | None = form.rent_type.data
        payment_type: str | None = form.payment_type.data

        # Получаем файл изображения
        image_file = request.files[form.image.name]

        if image_file:

            # Создайте собственный временный каталог с помощью функции create_custom_temp_dir()
            custom_temp_dir: str = create_custom_temp_dir()

            # Временно сохраняем файл в пользовательском каталоге
            temp_file_path: str = os.path.join(custom_temp_dir, secure_filename(image_file.filename))
            image_file.save(temp_file_path)

            # Загружаем файл на Google Disk
            file_id: str = upload_photo(temp_file_path)
        if rent_type not in [choice.value for choice in ApartmensTypeChoice]:
            flash("Выбран тип аренды")
            return redirect(url_for("apartmens.apartmens"))

        if payment_type not in [choice.value for choice in PaymensTypeChoice]:
            flash("Выбран тип оплаты")
            return redirect(url_for("apartmens.apartmens"))

        try:
            apartmens = Apartmens(
                user_id=current_user.id,
                country=form.country.data,
                city=form.city.data,
                address=form.address.data,
                title=form.title.data,
                description=form.description.data,
                payment_type=payment_type,
                rent_type=rent_type,
                image_path=file_id,
            )
            db.session.add(apartmens)
            db.session.commit()

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

            payments = Payment(
                apartmens_id=apartmens.id,
                price=form.price.data,
            )
            db.session.add(payments)
            db.session.commit()

            propertie = Propertie(
                apartmens_id=apartmens.id,
                floor=form.floor.data,
                apartment_number=form.apartment_number.data,
                number_of_beds=form.number_of_beds.data,
                number_of_guests=form.number_of_guests.data,
                room_area=form.room_area.data,
                no_children=form.no_children.data,
                no_parties=form.no_parties.data,
                no_smoking=form.no_smoking.data,
                no_pets=form.no_pets.data,
            )
            db.session.add(propertie)
            db.session.commit()
            os.remove(temp_file_path)
            os.rmdir(custom_temp_dir)
        except Exception as e:
            flash(f"Ошибка ввода: {str(e)}")
            db.session.rollback()
            return redirect(url_for("apartmens.apartmens"))
        flash("Обьявление отправлено на модерацию.")
        return redirect(url_for("intro.index"))
    flash(f"Заполните все поля или исправте ошибки в формате. {form.errors}")
    return redirect(url_for("apartmens.apartmens"))
