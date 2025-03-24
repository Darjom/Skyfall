# permissions/infrastructure/persistence/PermissionMapping.py

from apps import db



class PermissionMapping(db.Model):
    __tablename__ = 'permission'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

    def to_domain(self):
        from src.permissions.domain.Permission import Permission
        return Permission(name=self.name, description=self.description)

    @classmethod
    def from_domain(cls, permission):
        return cls(name=permission.name, description=permission.description)