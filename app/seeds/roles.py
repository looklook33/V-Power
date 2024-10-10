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
        describe="Trainer Team",
        url='https://scdaily.com/images/IOwLJIPJdrHMb8BRZaFjObwVSVxgunlfllntzyrg.jpeg',
        userId=3
    ),
    Role(
        isMember=False,
        isTrainer=False,
        isManager=True,
        describe="Manager at the gym",
        url='https://photos.onedrive.com/share/788075063AF139E8!s6dd99543416d43cc97977e64e19a49cc?cid=788075063AF139E8&resId=788075063AF139E8!s6dd99543416d43cc97977e64e19a49cc&ithint=photo&migratedtospo=true&redeem=aHR0cHM6Ly8xZHJ2Lm1zL2kvYy83ODgwNzUwNjNhZjEzOWU4L0VVT1YyVzF0UWN4RGw1ZC1aT0dhU2N3Qi16YWRPS29XQXJKZ2RXLUNzdVA0MHc',
        userId=4
    ),
    Role(
        isMember=False,
        isTrainer=True,
        isManager=False,
        describe="Coach Liu",
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