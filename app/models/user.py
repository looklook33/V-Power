from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .schedule_users import schedule_users
from sqlalchemy import ForeignKey, Integer, Column
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    # created_at = db.Column(db.DateTime, default=db.func.now())
    # updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict_simple(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
    
     # Relationships
    roles = db.relationship('Role', back_populates='user')
    equipment = db.relationship('Equipment', back_populates='user')
    schedules = db.relationship('Schedule', secondary=schedule_users, back_populates='users')
    galleries = db.relationship('Gallery', back_populates='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            "roles": [role.to_dict() for role in self.roles],
            # 'schedules': [schedule.to_dict() for schedule in self.schedules]
        }
    
