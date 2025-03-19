import os
from decouple import config


class Config:
    """Configuración base"""

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Clave secreta de Flask
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='postgresql'),
        config('DB_USERNAME', default='postgres'),
        config('DB_PASS', default='admin123'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=5432),
        config('DB_NAME', default='tis')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    OHSANSI_STATIC_FOLDER = config('OHSANSI_STATIC_FOLDER', default='apps/oh_sansi/static')
    OHSANSI_TEMPLATE_FOLDER = config('OHSANSI_TEMPLATE_FOLDER', default='apps/oh_sansi/templates')

    # Rutas para la app backoffice
    BACKOFFICE_STATIC_FOLDER = config('BACKOFFICE_STATIC_FOLDER', default='apps/backoffice/static')
    BACKOFFICE_TEMPLATE_FOLDER = config('BACKOFFICE_TEMPLATE_FOLDER', default='apps/backoffice/templates')

    UPLOAD_FOLDER = config('UPLOAD_FOLDER', default='apps/uploads')

    # Configuración de Flask-Security
    SECURITY_URL_PREFIX = "/admin"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

    # URLs de Flask-Security, sobreescritos porque no ponen una / al final
    SECURITY_LOGIN_URL = "/admin/login/"
    SECURITY_LOGOUT_URL = "/admin/logout/"
    SECURITY_REGISTER_URL = "/admin/register/"

    SECURITY_POST_LOGIN_VIEW = "/admin/"
    SECURITY_POST_LOGOUT_VIEW = "/admin/"
    SECURITY_POST_REGISTER_VIEW = "/admin/"

    # Características de Flask-Security
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Configuración para Producción"""
    DEBUG = False

class DebugConfig(Config):
    """Configuración para Desarrollo"""
    DEBUG = True


# Diccionario de configuración
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}