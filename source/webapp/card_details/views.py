from flask import Blueprint, render_template
from webapp.lib.models import Apartmens, Comfort, Propertie


blueprint = Blueprint("card_details", __name__)


@blueprint.route("/card_details/<int:card_id>")
def index(card_id):
    title = "EasyNest"
    apartment = Apartmens.query.get_or_404(card_id)
    f_propers = Propertie.query.get_or_404(card_id)
    f_comforts = Comfort.query.get_or_404(card_id)
    propers = f_propers.to_dict()
    comforts = f_comforts.to_dict()
    return render_template(
        "card_details/index.html",
        page_title=title,
        apartment=apartment,
        propers=propers,
        comforts=comforts,
    )
