from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class EditApartmentForm(FlaskForm):
    address = StringField("Адрес", validators=[DataRequired()], render_kw={"class": "form-control"})
    title = StringField("Заголовок", validators=[DataRequired()], render_kw={"class": "form-control"})
    description = TextAreaField("Описание", validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField("Сохранить изменения", render_kw={"class": "btn btn-success"})
    submit_back = SubmitField("Назад", render_kw={"class": "btn btn-warning"})
