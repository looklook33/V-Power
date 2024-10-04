from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Equipment, db
from datetime import datetime

equipment_routes = Blueprint('equipment', __name__)

# Utility function to check if the current user is a manager
def is_manager():
    return any(role.isManager for role in current_user.roles)


@equipment_routes.route('/', methods=['GET'])
def get_equipment():
    """
    Get all equipment. Accessible to everyone.
    """
    equipment_list = Equipment.query.all()
    return {'equipment': [equipment.to_dict() for equipment in equipment_list]}


@equipment_routes.route('/', methods=['POST'])
@login_required
def create_equipment():
    """
    Create new equipment. Only managers can add equipment.
    """
    if not is_manager():
        return {"error": "Only managers can add equipment"}, 403

    data = request.get_json()

    new_equipment = Equipment(
        type=data.get('type'),
        url=data.get('url'),
        describe=data.get('describe'),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        userId=current_user.id
    )

    db.session.add(new_equipment)
    db.session.commit()
    return new_equipment.to_dict(), 201


@equipment_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_equipment(id):
    """
    Update an existing equipment. Only managers can modify equipment.
    """
    equipment = Equipment.query.get(id)

    if not equipment:
        return {"error": "Equipment not found"}, 404

    if not is_manager():
        return {"error": "Only managers can modify equipment"}, 403

    data = request.get_json()

    equipment.type = data.get('type', equipment.type)
    equipment.url = data.get('url', equipment.url)
    equipment.describe = data.get('describe', equipment.describe)
    equipment.updated_at = datetime.now()

    db.session.commit()
    return equipment.to_dict()


@equipment_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_equipment(id):
    """
    Delete equipment. Only managers can delete equipment.
    """
    equipment = Equipment.query.get(id)

    if not equipment:
        return {"error": "Equipment not found"}, 404

    if not is_manager():
        return {"error": "Only managers can delete equipment"}, 403

    db.session.delete(equipment)
    db.session.commit()
    return {"message": "Equipment deleted successfully"}, 200
