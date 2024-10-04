from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Schedule, Role, db,User
from datetime import datetime

schedule_routes = Blueprint('schedules', __name__)

# check if the current user is a manager
def is_manager():
    if hasattr(current_user, 'roles') and isinstance(current_user.roles, list):
        return any(role.isManager for role in current_user.roles if hasattr(role, 'isManager'))
    return False

# check if the current user is a member
def is_member():
    if hasattr(current_user, 'roles') and isinstance(current_user.roles, list):
        return any(role.isMember for role in current_user.roles if hasattr(role, 'isMember'))
    return False

def is_trainer():
    if hasattr(current_user, 'roles') and isinstance(current_user.roles, list):
        return any(role.isMember for role in current_user.roles if hasattr(role, 'isTrainer'))
    return False

# Manager: Query all members' schedules
@schedule_routes.route('/')
@login_required
def all_schedules():
    """
    Query for all schedules. Only managers can see all members' schedules.
    """
    # user = current_user.to_dict()
    # is_manager = user['roles'][0]['isManager']
    # print(f"\n\n\n\n\n{user}\n\n\n\n\n")
    # print(f'\n\n\n\n\n{is_manager}')
    # schedules = Schedule.query.all()
    # schedules = Schedule.query.filter(Schedule.userId == user['id']).all()
    # return {'schedules': [schedule.to_dict() for schedule in schedules]}
    if is_manager():
        schedules = Schedule.query.all()
    # elif not is_manager:
    #     schedules = Schedule.query.filter(Schedule.userId == user['id']).all()

        return {'schedules': [schedule.to_dict() for schedule in schedules]}

   
    return {"error": "Unauthorized access"}, 403

# Member: Query his own schedules
@schedule_routes.route('/my')
@login_required
def my_schedules():
    """
    Query for the current user's schedules.
    Members can only view their own schedules.
    """
    if is_member():
        schedules = Schedule.query.filter_by(userId=current_user.id).all()
        return {'schedules': [schedule.to_dict() for schedule in schedules]}
    return {"error": "Unauthorized access"}, 403


@schedule_routes.route('/', methods=['POST'])
@login_required
def create_schedule():
    """
    Create a new schedule.
    Members must choose a trainer, and trainers must choose a member.
    Managers can create schedules for any combination of users.
    """
    data = request.get_json()

    member_id = data.get('member_id')
    trainer_id = data.get('trainer_id')
    describe = data.get('describe')
    start_time_str = data.get('startTime')
    end_time_str = data.get('endTime')

    # Check if both member and trainer IDs are provided
    if not member_id or not trainer_id:
        return {"error": "Both a member and a trainer are required for a schedule"}, 400

    # Convert time strings to Python time objects
    try:
        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        end_time = datetime.strptime(end_time_str, '%H:%M').time()
    except ValueError:
        return {"error": "Invalid time format. Use 'HH:MM' format"}, 400

    # Query the users based on the provided IDs
    member = User.query.filter_by(id=member_id).first()
    trainer = User.query.filter_by(id=trainer_id).first()

    # Check if the selected users have the correct roles
    if not (member and any(role.isMember for role in member.roles)):
        return {"error": "Invalid member selected"}, 400

    if not (trainer and any(role.isTrainer for role in trainer.roles)):
        return {"error": "Invalid trainer selected"}, 400

    # Check if the current user is allowed to create this schedule
    if is_manager():
        # Managers can create schedules for any combination
        pass
    elif is_member():
        if current_user.id != member_id:
            return {"error": "Members can only create schedules for themselves"}, 403
    elif is_trainer():
        if current_user.id != trainer_id:
            return {"error": "Trainers can only create schedules for themselves"}, 403
    else:
        return {"error": "Permission denied"}, 403

    # Create the new schedule
    new_schedule = Schedule(
        describe=describe,
        startTime=start_time,
        endTime=end_time,
        create_at=datetime.now(),
        updated_at=datetime.now(),
        userId = current_user.id
    )
    new_schedule.users.append(member)
    new_schedule.users.append(trainer)

    db.session.add(new_schedule)
    db.session.commit()

    return new_schedule.to_dict(), 201

# Manager: Edit any schedule
# Member: Edit their own schedule
@schedule_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_schedule(id):
    """
    Edit a schedule by its ID.
    Members and trainers can only edit their own schedules.
    Managers can edit any schedule.
    """
    schedule = Schedule.query.get(id)
    data = request.get_json()

    # Convert startTime and endTime from strings to time objects if provided
    start_time_str = data.get('startTime')
    end_time_str = data.get('endTime')

    try:
        if start_time_str:
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
        else:
            start_time = schedule.startTime

        if end_time_str:
            end_time = datetime.strptime(end_time_str, '%H:%M').time()
        else:
            end_time = schedule.endTime
    except ValueError:
        return {"error": "Invalid time format. Use 'HH:MM' format"}, 400

    # Check if the current user is allowed to edit this schedule
    is_schedule_user = any(user.id == current_user.id for user in schedule.users)

    if is_manager():
        # Managers can edit any schedule
        pass
    elif is_member() or is_trainer():
        # Members and trainers can only edit schedules they are a part of
        if not is_schedule_user:
            return {"error": "You are not authorized to edit this schedule"}, 403
    else:
        return {"error": "Permission denied"}, 403

    # Update the schedule
    schedule.describe = data.get('describe', schedule.describe)
    schedule.startTime = start_time
    schedule.endTime = end_time
    schedule.updated_at = datetime.now()

    db.session.commit()
    return schedule.to_dict(), 200

# Manager: Delete any schedule
# Member: Delete their own schedule
@schedule_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_schedule(id):
    """
    Delete a schedule by its ID.
    Members can only delete their own schedules.
    Managers can delete any schedule.
    """
    schedule = Schedule.query.get(id)

    if is_manager() or (is_member() and schedule.userId == current_user.id):
        db.session.delete(schedule)
        db.session.commit()
        return {"message": "Schedule deleted successfully"}
    
    return {"error": "Unauthorized access"}, 403