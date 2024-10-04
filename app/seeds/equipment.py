from app.models import db, Equipment, environment,SCHEMA
from datetime import datetime

demo_equipment = [
    Equipment(
        type='Treadmill',
        url='https://example.com/treadmill.jpg',
        describe='Top-quality treadmill for cardio',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='Dumbbells',
        url='https://example.com/dumbbells.jpg',
        describe='Full set of dumbbells',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
]

def seed_equipment():
    for equip in demo_equipment:
        db.session.add(equip)
    db.session.commit()

def undo_equipment():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.equipment RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM equipment")
    db.session.commit()