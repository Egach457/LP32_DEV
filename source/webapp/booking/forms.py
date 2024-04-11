from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddApartmensForm(FlaskForm):
    country = StringField("Country", validators=[DataRequired()],
                          render_kw={"class": "form-control"})
    city= StringField("City", validators=[DataRequired()],
                      render_kw={"class": "form-control"})
    address = StringField("Address", validators=[DataRequired()],
                          render_kw={"class": "form-control"})
    title = StringField("Title", validators=[DataRequired()],
                        render_kw={"class": "form-control"})
    description = TextAreaField("Description", validators=[DataRequired()],
                                render_kw={"class": "form-control"})
    rent_type = StringField("Rent type", validators=[DataRequired()],
                            render_kw={"class": "form-control"})
    payment_type = StringField("Payment type", validators=[DataRequired()],
                               render_kw={"class": "form-control"})
    submit = SubmitField("Edite", validators=[DataRequired()],
                         render_kw={"class": "btn btn-primary"})
