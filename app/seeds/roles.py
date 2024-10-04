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
        describe="Trainer and Manager at the gym",
        userId=3
    ),
    Role(
        isMember=True,
        isTrainer=True,
        isManager=True,
        describe="Trainer, Manager and Member at the gym",
        userId=4
    )
]

def seed_roles():
    for role in demo_roles:
        db.session.add(role)
    db.session.commit()

def undo_roles():
    db.session.execute(text("DELETE FROM roles"))
    db.session.commit()