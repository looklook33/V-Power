from app.models import db, Gallery, environment,SCHEMA
from datetime import datetime

demo_galleries = [
    Gallery(
        type='Gym Interior',
        url='https://example.com/gallery1.jpg',
        describe='A view of the gym interior',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Fitness Equipment',
        url='https://example.com/gallery2.jpg',
        describe='State-of-the-art equipment',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
]

def seed_galleries():
    for gallery in demo_galleries:
        db.session.add(gallery)
    db.session.commit()

def undo_galleries():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.galleries RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM galleries")
    db.session.commit()