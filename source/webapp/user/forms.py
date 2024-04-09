from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email address", validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    password = PasswordField("Password", validators=[DataRequired()],
                             render_kw={"class": "form-control"})
    remember_me = BooleanField("Remember me", default=True,
                               render_kw={"class": "form-check-input"})
    submit = SubmitField("Sign in", render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()],
                        render_kw={"class": "form-control"}) 
    last_name = StringField("Last name", validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    phone = StringField("Phone number", validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    email = StringField("Email address", validators=[DataRequired(), Email()],
                        render_kw={"class": "form-control"})
    password = PasswordField("Password", validators=[DataRequired()],
                             render_kw={"class": "form-control"})
    password2 = PasswordField("Repeat password", validators=[DataRequired(), EqualTo("password")],
                             render_kw={"class": "form-control"})
    submit = SubmitField("Sign in", render_kw={"class": "btn btn-primary"})

