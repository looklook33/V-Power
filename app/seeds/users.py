from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password')
    min = User(
        username='min', email='min@aa.io', password='password')
    liu = User(
        username='liu', email='coachliu@aa.io', password='password')
    couchXu = User(
        username='coachXu', email='coach1@aa.io', password='password')
    couchZhang= User(
        username='coachZhang', email='coach2@aa.io', password='password')
    couchWang = User(
        username='coachWang', email='coach3@aa.io', password='password')
    couchZhao = User(
        username='couchZhao', email='coach4@aa.io', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(min)
    db.session.add(liu)
    db.session.add(couchXu)
    db.session.add(couchZhang)
    db.session.add(couchWang)
    db.session.add(couchZhao)
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
