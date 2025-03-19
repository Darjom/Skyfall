DEBUG=True
SECRET_KEY=S3cr3t_K#Key
DB_ENGINE=postgresql
DB_NAME=tis
DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=postgres
DB_PASS=admin123


OHSANSI_STATIC_FOLDER=apps/oh_sansi/static
OHSANSI_TEMPLATE_FOLDER=apps/oh_sansi/templates
BACKOFFICE_STATIC_FOLDER=apps/backoffice/static
BACKOFFICE_TEMPLATE_FOLDER=apps/backoffice/templates
UPLOAD_FOLDER=apps/uploads

# Flask-Security config
SECURITY_URL_PREFIX="/admin"
SECURITY_PASSWORD_HASH="pbkdf2_sha512"
SECURITY_PASSWORD_SALT="ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL="/admin/login/"
SECURITY_LOGOUT_URL="/admin/logout/"
SECURITY_REGISTER_URL="/admin/register/"

SECURITY_POST_LOGIN_VIEW="/admin/"
SECURITY_POST_LOGOUT_VIEW="/admin/"
SECURITY_POST_REGISTER_VIEW="/admin/"

# Flask-Security features
SECURITY_REGISTERABLE=True
SECURITY_SEND_REGISTER_EMAIL=False
SQLALCHEMY_TRACK_MODIFICATIONS=False