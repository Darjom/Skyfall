# src/roles/infrastructure/persistence/RoleMapping.py

from apps import db

class RolMapping(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def to_domain(self):
        from src.roles.domain.Rol import Rol
        return Rol(name=self.name, description=self.description)

    @classmethod
    def from_domain(cls, role_domain):
        return cls(name=role_domain.name, description=role_domain.description)