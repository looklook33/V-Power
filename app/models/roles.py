from .db import db  

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    isMember = db.Column(db.Boolean, default=False)
    isTrainer = db.Column(db.Boolean, default=False)
    isManager = db.Column(db.Boolean, default=False)
    describe = db.Column(db.String(255))
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    url = db.Column(db.String, nullable=True)  

    user = db.relationship('User', back_populates='roles')

    def to_dict(self):
        return {
            "id": self.id,
            "isMember": self.isMember,
            "isTrainer": self.isTrainer,
            "isManager": self.isManager,
            "describe": self.describe,
            "url": self.url  
        }
