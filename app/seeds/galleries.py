from app.models import db, Gallery, environment,SCHEMA
from datetime import datetime

demo_galleries = [
    Gallery(
        type='Workout',
        url='https://i.postimg.cc/1RC3XPSw/thumbnail-image0-1.jpg',
        describe='Dumbbell rows are a compound upper body exercise that can help with a number of things',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Workout',
        url='https://i.postimg.cc/SKhy3xLF/thumbnail-image1.jpg',
        describe='Deadlifts are a fantastic full body exercise for shape, size and overall strength. ',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Workout',
        url='https://i.postimg.cc/TYKYWS2S/thumbnail-image1-1.jpg',
        describe='Dumbbell squats target major lower body muscles like the glutes, quads, hamstrings, and calves. The added weight from the dumbbells activates your posterior chain muscles, which includes your hamstrings and glutes',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Trainer',
        url='https://i.postimg.cc/DyRfQg8z/thumbnail-image0.jpg',
        describe='Trainer',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Gallery(
        type='Members',
        url='https://i.postimg.cc/Hk5Y6yy9/image9.jpg',
        describe='Member',
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