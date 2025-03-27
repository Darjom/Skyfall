# apps/backoffice/security.py
import uuid

from flask import app
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from apps import db
from src.roles.infrastructure.persistence.RolMapping import RolMapping
from src.users.infrastructure.persistence.UserMapping import UserMapping

# Crea el UserDatastore
user_datastore = SQLAlchemyUserDatastore(db, UserMapping, RolMapping)
security = Security()