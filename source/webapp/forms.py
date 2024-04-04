from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email address", validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    password = PasswordField("Password", validators=[DataRequired()],
                             render_kw={"class": "form-control"})
    remember_me = BooleanField("Remember me", default=True,
                               render_kw={"class": "form-check-input"})
    submit = SubmitField("Sign in", render_kw={"class": "btn btn-primary"})

