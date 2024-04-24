from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, AnyOf


from webapp.lib.models import ApartmensTypeChoice, PaymensTypeChoice


class AddApartmensForm(FlaskForm):
    country = StringField(
        "Country",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    city = StringField(
        "City",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    address = StringField(
        "Address",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    title = StringField(
        "Title",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    description = TextAreaField(
        "Description",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    rent_type = SelectField(
        "Rent type",
        choices=[(choice.name, choice.value) for choice in ApartmensTypeChoice],
        validators=[
            InputRequired(),
            AnyOf([choice.name for choice in ApartmensTypeChoice]),
        ],
        render_kw={"class": "form-control"},
    )
    payment_type = SelectField(
        "Payment type",
        choices=[(choice.name, choice.value) for choice in PaymensTypeChoice],
        validators=[
            InputRequired(),
            AnyOf([choice.name for choice in PaymensTypeChoice]),
        ],
        render_kw={"class": "form-control"},
    )
    floor = StringField(
        "Floor",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    apartment_number = StringField(
        "Apartment number",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    number_of_beds = StringField(
        "Number of beds",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    number_of_guests = StringField(
        "Number of guests",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    room_area = StringField(
        "Room area",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    # Формы для switches (Propertie, Comfort)
    wi_fi = BooleanField(
        "Wi-Fi",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    hair_dryer = BooleanField(
        "Hair dryer",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    towels = BooleanField(
        "Towels",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    balcony = BooleanField(
        "Balcony",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    air_conditioner = BooleanField(
        "Air conditioner",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    tv = BooleanField(
        "TV",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    no_children = BooleanField(
        "No children",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    no_parties = BooleanField(
        "No parties",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    no_smoking = BooleanField(
        "No smoking",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    no_pets = BooleanField(
        "No pets",
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"},
    )
    submit = SubmitField(
        "Edite",
        validators=[DataRequired()],
        render_kw={"class": "btn btn-primary"},
    )
