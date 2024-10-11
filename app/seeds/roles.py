from app.models import db, Role
from sqlalchemy.sql import text

demo_roles = [
    Role(
        isMember=True,
        isTrainer=False,
        isManager=False,
        describe="Regular gym member",
        userId=1
    ),
    Role(
        isMember=True,
        isTrainer=False,
        isManager=False,
        describe="Regular gym member",
        userId=2
    ),
    Role(
        isMember=True,
        isTrainer=True,
        isManager=False,
        describe="NASM Corrective Exercise Specialist",
        url='https://scdaily.com/images/IOwLJIPJdrHMb8BRZaFjObwVSVxgunlfllntzyrg.jpeg',
        userId=3
    ),
    Role(
        isMember=False,
        isTrainer=False,
        isManager=True,
        describe="Manager at the gym",
        url='https://i.postimg.cc/tJvCNV2b/image2.jpg',
        userId=4
    ),
    Role(
        isMember=False,
        isTrainer=True,
        isManager=False,
        describe="Fitness Nutrition Specialist (ISSA)",
        url='https://i.postimg.cc/tJvCNV2b/image2.jpg',
        userId=5
    ),
]

def seed_roles():
    for role in demo_roles:
        db.session.add(role)
    db.session.commit()

def undo_roles():
    db.session.execute(text("DELETE FROM roles"))
    db.session.commit()