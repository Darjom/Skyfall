# apps/backoffice/security.py
import uuid

from flask import app
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from apps import db
from src.roles.infrastructure.persistence.RolMapping import RolMapping


# Tabla intermedia
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)



class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship(
        'RolMapping',
        secondary=roles_users,
        backref='user',
    )
    fs_uniquifier = db.Column(
        db.String(255),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )

# Crea el UserDatastore
user_datastore = SQLAlchemyUserDatastore(db, User, RolMapping)
security = Security()