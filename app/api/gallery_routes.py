from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Gallery, db
from datetime import datetime

gallery_routes = Blueprint('galleries', __name__)

# Utility function to check if the current user is a manager
def is_manager():
    return any(role.isManager for role in current_user.roles)


@gallery_routes.route('/', methods=['GET'])
def get_galleries():
    """
    Get all galleries. Accessible to everyone.
    """
    galleries = Gallery.query.all()
    return {'galleries': [gallery.to_dict() for gallery in galleries]}


@gallery_routes.route('/', methods=['POST'])
@login_required
def create_gallery():
    """
    Create a new gallery. Only managers can add galleries.
    """
    if not is_manager():
        return {"error": "Only managers can add galleries"}, 403

    data = request.get_json()

    new_gallery = Gallery(
        type=data.get('type'),
        url=data.get('url'),
        describe=data.get('describe'),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        userId=current_user.id
    )

    db.session.add(new_gallery)
    db.session.commit()
    return new_gallery.to_dict(), 201


@gallery_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_gallery(id):
    """
    Update an existing gallery. Only managers can modify galleries.
    """
    gallery = Gallery.query.get(id)

    if not gallery:
        return {"error": "Gallery not found"}, 404

    if not is_manager():
        return {"error": "Only managers can modify galleries"}, 403

    data = request.get_json()

    gallery.type = data.get('type', gallery.type)
    gallery.url = data.get('url', gallery.url)
    gallery.describe = data.get('describe', gallery.describe)
    gallery.updated_at = datetime.now()

    db.session.commit()
    return gallery.to_dict()


@gallery_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_gallery(id):
    """
    Delete a gallery. Only managers can delete galleries.
    """
    gallery = Gallery.query.get(id)

    if not gallery:
        return {"error": "Gallery not found"}, 404

    if not is_manager():
        return {"error": "Only managers can delete galleries"}, 403

    db.session.delete(gallery)
    db.session.commit()
    return {"message": "Gallery deleted successfully"}, 200
