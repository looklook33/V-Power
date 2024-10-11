from .db import db, environment, SCHEMA, add_prefix_for_prod
# from sqlalchemy.sql import func

class Equipment(db.Model):
    __tablename__ = "equipment"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255))
    describe = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))

    user = db.relationship('User', back_populates='equipment')

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "describe": self.describe,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "userId": self.userId
        }