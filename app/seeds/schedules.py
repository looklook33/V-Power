from app.models import db, Schedule, environment,SCHEMA
from datetime import datetime, time,date

demo_schedules = [
    Schedule(
        describe='Morning Yoga Session',
        date=date(2024, 10, 8),  # Year, Month, Day
        startTime=time(7, 0, 0),  # Hour, Minute, Second (7:00 AM)
        endTime=time(8, 0, 0),    # Hour, Minute, Second (8:00 AM)
        userId=1
    ),
    Schedule(
        describe='Strength Training',
        date=date(2024, 10, 11),  # Year, Month, Day
        startTime=time(9, 30, 0),  # 9:30 AM
        endTime=time(10, 30, 0),   # 10:30 AM
        userId=2
    ),
    Schedule(
        describe='Evening Cardio',
        date=date(2024, 10, 12),  # Year, Month, Day
        startTime=time(17, 0, 0),  # 5:00 PM
        endTime=time(18, 0, 0),    # 6:00 PM
        userId=1
    ),
    Schedule(
        describe='Pilates Class',
        date=date(2024, 10, 13),  # Year, Month, Day
        startTime=time(11, 0, 0),  # 11:00 AM
        endTime=time(12, 0, 0),    # 12:00 PM
        userId=2
    )
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