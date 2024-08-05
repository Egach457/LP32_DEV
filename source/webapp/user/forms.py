from flask_wtf import FlaskForm
from webapp.lib.models import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField(
        "Email address",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField("Remember me", default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField("Sign in", render_kw={"class": "btn btn-primary"})
    register_submit = SubmitField("Registration", render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()], render_kw={"class": "form-control"})
    last_name = StringField("Last name", validators=[DataRequired()], render_kw={"class": "form-control"})
    phone = StringField("Phone number", validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField(
        "Email address",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"},
    )
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField(
        "Repeat password",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField("Send", render_kw={"class": "btn btn-primary"})

    def validate_useraname(self, first_name: StringField, last_name: StringField) -> None:
        user_count = User.query.filter_by(first_name=first_name.data, last_name=last_name.data).count()
        if user_count > 0:
            raise ValidationError("Такой пользователь зарегистрирован")

    def validate_email(self, email: StringField) -> None:
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError("Пользовател с такой электронной почтой уже зарегистрирован")
