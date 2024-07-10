from flask_wtf import FlaskForm
from webapp.lib.models import ApartmensTypeChoice, PaymensTypeChoice
from wtforms import BooleanField, FileField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddApartmensForm(FlaskForm):
    country = StringField(
        "Страна",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    city = StringField(
        "Город",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    address = StringField(
        "Адрес",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    title = StringField(
        "Заголовок",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    description = TextAreaField(
        "Описание",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    rent_type = SelectField(
        "Тип жилья",
        choices=[choice.value for choice in ApartmensTypeChoice],
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    payment_type = SelectField(
        "Тип оплаты",
        choices=[choice.value for choice in PaymensTypeChoice],
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    floor = StringField(
        "Этаж",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    apartment_number = StringField(
        "Номер апартаментов",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    number_of_beds = StringField(
        "Количество кроватей",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    number_of_guests = StringField(
        "Количество гостей",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    room_area = StringField(
        "Площадь аренды",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    # Форма для Файла
    image = FileField(
        "Фотографии",
        # validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    # Формы для switches (Propertie, Comfort)
    wi_fi = BooleanField(
        "Wi-Fi",
        render_kw={"class": "form-check-input"},
    )
    hair_dryer = BooleanField(
        "Фен",
        render_kw={"class": "form-check-input"},
    )
    towels = BooleanField(
        "Полотенца",
        render_kw={"class": "form-check-input"},
    )
    balcony = BooleanField(
        "Лоджия",
        render_kw={"class": "form-check-input"},
    )
    air_conditioner = BooleanField(
        "Кондиционер",
        render_kw={"class": "form-check-input"},
    )
    tv = BooleanField(
        "TV",
        render_kw={"class": "form-check-input"},
    )
    no_children = BooleanField(
        "Без детей",
        render_kw={"class": "form-check-input"},
    )
    no_parties = BooleanField(
        "Без тусовок",
        render_kw={"class": "form-check-input"},
    )
    no_smoking = BooleanField(
        "Не курить",
        render_kw={"class": "form-check-input"},
    )
    no_pets = BooleanField(
        "Без животных",
        render_kw={"class": "form-check-input"},
    )
    submit = SubmitField(
        "Загрузить объявление",
        render_kw={"class": "btn btn-primary"},
    )
