from .db import db, environment, SCHEMA, add_prefix_for_prod

schedule_users = db.Table(
    'schedule_users',
    db.Column('schedule_id', db.Integer, db.ForeignKey(add_prefix_for_prod('schedules.id')), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
)

if environment == "production":
    schedule_users.schema = SCHEMA