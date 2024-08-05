from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from webapp.booking_list.forms import EditApartmentForm
from webapp.booking_list.models import DeleteAnnouncement, EditAnnouncement, UserShowAnnouncement
from webapp.lib.db import db
from webapp.lib.models import Apartmens
from werkzeug.wrappers import Response


blueprint = Blueprint("booking_list", __name__, url_prefix="/users")


@blueprint.route("/booking_list")
@login_required
def my_booking_list() -> str | Response:

    title = "Ваши объявления"
    show_announcement = UserShowAnnouncement(user_id=current_user.id)
    apartmens = show_announcement.show()
    return render_template(
        "booking_list/index.html",
        page_title=title,
        apartmens=apartmens,
    )


@blueprint.route("/booking_list/edit/<int:apartment_id>", methods=["GET", "POST"])
@login_required
def edit_announcement(apartment_id: int) -> str | Response:
    try:
        session = db.session
        edit_announcement = EditAnnouncement(user_id=current_user.id)
        form = EditApartmentForm()

        if request.method == "POST" and form.validate_on_submit():
            apartment = session.query(Apartmens).filter_by(id=apartment_id, user_id=current_user.id).first()
            if apartment:
                apartment.address = form.address.data
                apartment.title = form.title.data
                apartment.description = form.description.data
                edit_announcement.edit(apartment)
            flash("Объявление успешно обновлено")
            return redirect(url_for("booking_list.my_booking_list"))
        else:
            apartment = session.query(Apartmens).filter_by(id=apartment_id, user_id=current_user.id).first()
            if apartment:
                form.address.data = apartment.address
                form.title.data = apartment.title
                form.description.data = apartment.description
            return render_template(
                "booking_list/edit.html", page_title="Редактирование объявления", apartment=apartment, form=form
            )

    except Exception as err:
        flash(f"Возникла ошибка: {err}")
        return redirect(url_for("booking_list.my_booking_list"))


@blueprint.route("/booking_list/delete/<int:apartment_id>", methods=["POST"])
@login_required
def delete_announcement(apartment_id: int) -> str | Response:

    try:
        delete_announcement = DeleteAnnouncement(user_id=current_user.id)
        delete_announcement.delete(apartment_id)
    except Exception as err:
        flash(f"Возникла ошибка: {err}")
        return redirect(url_for("booking_list.my_booking_list"))

    return redirect(url_for("booking_list.my_booking_list"))
