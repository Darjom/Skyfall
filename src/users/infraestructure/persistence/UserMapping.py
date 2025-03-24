
from apps import db
class UserMapping(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())

    def to_domain(self):
        from src.users.domain.User import User
        return User(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            password=self.password,
            active=self.active
        )

    @classmethod
    def from_domain(cls, user_domain):
        return cls(
            id=user_domain.id,
            first_name=user_domain.first_name,
            last_name=user_domain.last_name,
            email=user_domain.email,
            password=user_domain.password,
            active=user_domain.active
        )