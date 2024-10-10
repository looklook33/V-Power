from app.models import db, Equipment, environment,SCHEMA
from datetime import datetime

demo_equipment = [
    Equipment(
        type='Treadmill',
        url='https://i.postimg.cc/FHqSL3Qb/thumbnail-image5.jpg',
        describe='Top-quality treadmill for cardio',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='Dumbbells',
        url='https://i.postimg.cc/SKMM7RyB/thumbnail-image7.jpg',
        describe='Lat pull down/Low Row machine is a 2 in 1 machine that helps in making your back stronger. Lat Pull down helps to develop upper back, while, Low Row helps to develop mid to lower back',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='Treadmill',
        url='https://i.postimg.cc/jSCN2vBd/thumbnail-image4.jpg',
        describe='This gym machine provides some of the best exercises for both upper and lower body. It a great machine for squats, but it great for chest press too. ',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='Dumbbells',
        url='https://i.postimg.cc/YqrQKt3F/thumbnail-image3.jpg',
        describe='Work your glutes, hamstrings and quads like never before. The leg curl and leg extension dual purpose machine. This two in one machine not only works on multiple muscle groups but also helps in saving cost and space.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
        Equipment(
        type='Dumbbells',
        url='https://i.postimg.cc/X7sdntHz/image8.jpg',
        describe='The goal of Foldable Wall Rack is to create a more space efficient, wall-mounted version of our standard Squat Power Rack; one that can be conveniently folded inward or outward against any wall. It can be used as a squat stand, pull up rig, or power rack take your pick.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='Treadmill',
        url='https://i.postimg.cc/T19mLsRh/image6.jpg',
        describe='The goal of Foldable Wall Rack is to create a more space efficient, wall-mounted version of our standard Squat Power Rack; one that can be conveniently folded inward or outward against any wall. It can be used as a squat stand, pull up rig, or power rack take your pick.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='Dumbbells',
        url='https://i.postimg.cc/SQ7cvnWq/image10.jpg',
        describe='The goal of Foldable Wall Rack is to create a more space efficient, wall-mounted version of our standard Squat Power Rack; one that can be conveniently folded inward or outward against any wall. It can be used as a squat stand, pull up rig, or power rack take your pick.',
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