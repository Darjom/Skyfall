# apps/backoffice/__init__.py
import os

from flask import Flask
from decouple import config as decouple_config
from config import config_dict
from apps import db
from apps.backoffice.config.security import security, user_datastore
from apps.backoffice.config.admin import admin
from src import import_all_models


def create_backoffice_app():

    app = Flask("backoffice")

    config_mode = decouple_config('FLASK_ENV', default='Debug')
    app.config.from_object(config_dict[config_mode])

    # Definir carpeta estática para el backoffice (si deseas override)
    app.static_folder = app.config["BACKOFFICE_STATIC_FOLDER"]
    app.template_folder = app.config["BACKOFFICE_TEMPLATE_FOLDER"]

    # Guardar archivos dinámicos en la carpeta apps/uploads (por defecto)
    app.config["UPLOAD_FOLDER"] = app.config["UPLOAD_FOLDER"]

    # Inicializar db
    db.init_app(app)
    import_all_models()

    # Inicializar Flask-Security (usa user_datastore, importado arriba)
    security.init_app(app, user_datastore)

    # Inicializar Flask-Admin
    admin.init_app(app)

    return app