from app.models import db, Schedule, User

def seed_schedule_users():
    # Retrieve existing users and schedules from the database
    user1 = User.query.get(1)  
    user2 = User.query.get(2)  
    user3 = User.query.get(3)  
    user4 = User.query.get(4)  

    schedule1 = Schedule.query.get(1)  
    schedule2 = Schedule.query.get(2) 
    schedule3 = Schedule.query.get(3)  
    schedule4 = Schedule.query.get(4)  

    # Associate schedules with users (trainers and members)
    schedule1.users.append(user1)  # Add user1 (member) to schedule1
    schedule1.users.append(user4)  # Add user2 (trainer) to schedule1

    schedule2.users.append(user2)  # Add user3 (member) to schedule2
    schedule2.users.append(user4)  # Add user4 (trainer) to schedule2

    schedule3.users.append(user1)  # Add user3 (member) to schedule2
    schedule3.users.append(user3)  # Add user4 (trainer) to schedule2

    schedule4.users.append(user2)  # Add user3 (member) to schedule2
    schedule4.users.append(user3)  # Add user4 (trainer) to schedule2

    # Commit the changes to the database
    db.session.commit()


def undo_schedule_users():
    db.session.execute("DELETE FROM schedule_users")
    db.session.commit()