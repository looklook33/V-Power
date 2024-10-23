from app.models import db, Gallery, environment,SCHEMA
from datetime import datetime

demo_galleries = [
    Gallery(
        type='Workout',
        url='https://i.postimg.cc/1RC3XPSw/thumbnail-image0-1.jpg',
        describe='Girl pull up!',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Workout',
        url='https://i.postimg.cc/SKhy3xLF/thumbnail-image1.jpg',
        describe='Belt squat is good way to reduced stress on the lower back and improved squat form. ',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Workout',
        url='https://i.postimg.cc/TYKYWS2S/thumbnail-image1-1.jpg',
        describe='Chest press!',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Trainer',
        url='https://i.postimg.cc/DyRfQg8z/thumbnail-image0.jpg',
        describe='Sumo Squat, help with overall leg strength, balance, and mobility',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Members',
        url='https://i.postimg.cc/Hk5Y6yy9/image9.jpg',
        describe='try the 50 years old back machine:)',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Honor wall',
        url='https://i.postimg.cc/PqVbgJyW/IMG-4569.jpg',
        describe='Honor Wall',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Honor wall',
        url='https://i.postimg.cc/G2ZFpfZ9/IMG-4570.jpg',
        describe='Honor Wall',
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