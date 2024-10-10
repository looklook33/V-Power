from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import User
from app.models import Role
from sqlalchemy.orm import joinedload

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/by-role', methods=['GET'])
def users_by_role():
    """
    Query for users by role type (isMember, isTrainer, isManager)
    Request query parameter 'role' can be 'member', 'trainer', or 'manager'
    """
    role_type = request.args.get('role')

    if role_type == 'member':
        users = User.query.join(Role).filter(Role.isMember == True).all()
    elif role_type == 'trainer':
        users = User.query.join(Role).filter(Role.isTrainer == True).all()
    elif role_type == 'manager':
        users = User.query.join(Role).filter(Role.isManager == True).all()
    else:
        return {"error": "Invalid role type"}, 400

    return {'users': [user.to_dict() for user in users]}
