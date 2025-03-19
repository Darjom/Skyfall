# apps/oh_sansi/controllers/__init__.py
from flask import Blueprint

def register_controllers(app):
   from apps.oh_sansi.controllers.home.HomeGetWebController import home_blueprint
   app.register_blueprint(home_blueprint)