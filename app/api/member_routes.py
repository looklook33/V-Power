from flask import Blueprint
from app.models import User, Role

member_routes = Blueprint('members', __name__)

@member_routes.route('/', methods=['GET'])
def get_all_members():
    """
    Get all users who have the member role (isMember = True).
    This route is accessible to everyone.
    """
    members = User.query.join(Role).filter(Role.isMember == True).all()
    
    if not members:
        return {"message": "No members found"}, 404

    return {"members": [member.to_dict() for member in members]}, 200