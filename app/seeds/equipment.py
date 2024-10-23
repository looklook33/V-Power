from app.models import db, Equipment, environment,SCHEMA
from datetime import datetime

demo_equipment = [
    Equipment(
        type='Treadmill',
        url='https://i.postimg.cc/FHqSL3Qb/thumbnail-image5.jpg',
        describe='Cable Crossover, maximize strength training options. Its design integrates configurable stations including the Adjustable Pulley, Lat Pulldown and Low Row.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='leg',
        url='https://i.postimg.cc/xjzGZ0zm/IMG-4564.jpg',
        describe='Hack Squat Machine. It is primarily used for lower body exercises, particularly targeting the quadriceps, glutes, and hamstrings. ',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='glute',
        url='https://i.postimg.cc/9XZTpJ6t/IMG-4552.jpg',
        describe='Hip Thrust Machine. An efficient way to perform the Hip Thrust exercise without having to set up the bar (and bench to lean on). ',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='legs',
        url='https://i.postimg.cc/nrbmxDDD/IMG-4553.jpg',
        describe='Belt Squat Machine, shifts the weight away from the back and onto the hips and legs, which can help reduce stress on the lower back. This can be especially beneficial for people with back issues or injuries.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
        Equipment(
        type='legs',
        url='https://i.postimg.cc/9fkTxSX1/IMG-4555.jpg',
        describe='Leg Press Machine. Leg presses allow you to focus on specific muscle groups, such as your quadriceps, hamstrings, glutes, and calves',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='legs',
        url='https://i.postimg.cc/q7qyx0rz/IMG-4556.jpg',
        describe='Hack Squat Machine, targets your quads, glutes, and hamstrings directly.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='back',
        url='https://i.postimg.cc/SNG90jNn/IMG-4549.jpg',
        describe='Old Fashion Back Machine. 50 years old Back Machine.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='back',
        url='https://i.postimg.cc/WzGk11Gf/IMG-4550.jpg',
        describe='Pectoral Fly, targets the pectoralis major and minor muscles in the chest, which are used for many daily activities like pushing doors and lifting objects.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='chest',
        url='https://i.postimg.cc/FHD0Sz2M/IMG-4558.jpg',
        describe='Seated Chest Press. Works effectively on the entire chest muscle.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='shoulder',
        url='https://i.postimg.cc/dtR2q4nt/IMG-4559.jpg',
        describe='The shoulder press machine helps isolate the deltoid muscles by removing the need for the core to support you during the exercise.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='back',
        url='https://i.postimg.cc/ZKzPt18M/IMG-4560.jpg',
        describe='Pull-Up Machine.targets your back and biceps, but involves many stabilizing muscles in your core, arms, and shoulders.',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
    Equipment(
        type='back',
        url='https://i.postimg.cc/QC1pKb3m/IMG-4562.jpg',
        describe='Lat-PullDown Machine, works the latissimus dorsi, the largest muscle in the back, as well as your biceps, rear delts, rhomboids and traps. ',
        created_at=datetime.now(),
        updated_at=datetime.now(),
    ),
     Equipment(
        type='back',
        url='https://i.postimg.cc/sXBPszHt/IMG-4563.jpg',
        describe='Bicep Curl Machine, targets the specific muscles located at the front of your arms called; biceps brachii, brachialis and brachioradialis ',
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