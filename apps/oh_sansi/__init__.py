
# apps/oh_sansi/__init__.py
from flask import Flask
from decouple import config as decouple_config
from config import config_dict
from apps import db
from apps.oh_sansi.controllers import register_controllers

def create_oh_sansi_app():
    """
    Crea la aplicación Flask para oh_sansi (frontend).
    """
    app = Flask("oh_sansi")

    config_mode = decouple_config('FLASK_ENV', default='Debug')
    app.config.from_object(config_dict[config_mode])
    app.static_folder = app.config["OHSANSI_STATIC_FOLDER"]
    app.template_folder = app.config["OHSANSI_TEMPLATE_FOLDER"]

    # Guardar archivos dinámicos en la carpeta apps/uploads (por defecto)
    app.config["UPLOAD_FOLDER"] = app.config["UPLOAD_FOLDER"]
    # Establecer carpeta estática (opcional)
    # app.static_folder = os.path.join(app.root_path, "static")

    db.init_app(app)

    register_controllers(app)

    with app.app_context():
        db.create_all()

    return app