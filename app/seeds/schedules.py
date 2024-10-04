from app.models import db, Schedule, environment,SCHEMA
from datetime import datetime, time

demo_schedules = [
    Schedule(
        describe='Morning Boxing Class',
        startTime=time(9, 0, 0),
        endTime=time(10, 30, 0),
        create_at=datetime.now(),
        updated_at=datetime.now(),
        userId=1
    ),
    Schedule(
        describe='Evening Martial Arts Class',
        startTime=time(18, 0, 0),
        endTime=time(19, 30, 0),
        create_at=datetime.now(),
        updated_at=datetime.now(),
        userId=4,
    ),
]

def seed_schedules():
    for schedule in demo_schedules:
        db.session.add(schedule)
    db.session.commit()

def undo_schedules():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.schedules RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM schedules")
    db.session.commit()