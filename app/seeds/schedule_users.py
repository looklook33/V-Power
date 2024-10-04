from app.models import db, Schedule, User

# Seed data for schedule_users relationship
def seed_schedule_users():
    # Retrieve existing users and schedules from the database
    user1 = User.query.get(1)  # Assume user1 is a member
    user2 = User.query.get(3)  # Assume user2 is a trainer
    user3 = User.query.get(2)  # Another member
    user4 = User.query.get(4)  # Another trainer

    schedule1 = Schedule.query.get(1)  # First schedule
    schedule2 = Schedule.query.get(2)  # Second schedule

    # Associate schedules with users (trainers and members)
    schedule1.users.append(user1)  # Add user1 (member) to schedule1
    schedule1.users.append(user2)  # Add user2 (trainer) to schedule1

    schedule2.users.append(user3)  # Add user3 (member) to schedule2
    schedule2.users.append(user4)  # Add user4 (trainer) to schedule2

    # Commit the changes to the database
    db.session.commit()


def undo_schedule_users():
    db.session.execute("DELETE FROM schedule_users")
    db.session.commit()