
import os, pkgutil, importlib

def import_all_models():

    base_dir = os.path.abspath(os.path.dirname(__file__))  # Directorio 'src'
    package_prefix = "src."

    for loader, module_name, is_pkg in pkgutil.walk_packages([base_dir], package_prefix):
        if "infrastructure.persistence" in module_name:
            importlib.import_module(module_name)
