from .db import db

schedule_users = db.Table(
    'schedule_users',
    db.Column('schedule_id', db.Integer, db.ForeignKey('schedules.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
)