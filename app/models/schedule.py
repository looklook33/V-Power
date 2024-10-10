from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import date, time
from sqlalchemy.sql import func
from .schedule_users import schedule_users

class Schedule(db.Model):
    __tablename__ = "schedules"

    id = db.Column(db.Integer, primary_key=True)
    describe = db.Column(db.String(255))
    date = db.Column(db.Date, nullable=False) 
    startTime = db.Column(db.Time, nullable=False)
    endTime = db.Column(db.Time, nullable=False)
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),onupdate=func.now())
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('User', secondary=schedule_users, back_populates='schedules')

    def to_dict(self):
        return {
            "id": self.id,
            "describe": self.describe,
            "date": self.date.isoformat(),
            "startTime": str(self.startTime),
            "endTime": str(self.endTime),
            # "created_at": self.create_at,
            # "updated_at": self.updated_at,
            'users': [user.to_dict() for user in self.users],
        }