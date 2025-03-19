from flask import render_template, request, Blueprint
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

home_blueprint = Blueprint("oh_sansi_home", __name__, url_prefix='')


@home_blueprint.route('/',)
def index():
    lista_paises = {
        "Estados Unidos": "Estados Unidos es una nación ubicada en América del Norte...",
        "Francia": "Francia es un país europeo famoso por su rica historia...",
        "Japón": "Japón es una nación insular en el este de Asia...",
        "Brasil": "Brasil es el país más grande de América del Sur y es conocido por su selva tropical...",
        "España": "España es un país en el suroeste de Europa conocido por su rica cultura...",
        "Australia": "Australia es un país insular en Oceanía famoso por su vida silvestre única...",
        "Canadá": "Canadá es un país en América del Norte conocido por su vasto territorio y belleza natural..."
    }

    return render_template(
        'home/index.html',
        segment='index', paises=lista_paises,
        url_atracciones='/',
        urlA='/')

