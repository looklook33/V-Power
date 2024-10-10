from flask import Blueprint,request
from app.models import User, Role, db

trainer_routes = Blueprint('trainers', __name__)

@trainer_routes.route('/', methods=['GET'])
def get_all_trainers():
    """
    Get all users who have the trainer role (isTrainer = True).
    This route is accessible to everyone.
    """
    trainers = User.query.join(Role).filter(Role.isTrainer == True).all()
    
    if not trainers:
        return {"message": "No trainers found"}, 404

    return {"trainers": [trainer.to_dict() for trainer in trainers]}, 200

@trainer_routes.route('/<int:id>', methods=['GET'])
def get_trainer_by_id(id):
    """
    Get a specific trainer by their ID.
    """
    trainer = User.query.join(Role).filter(User.id == id, Role.isTrainer == True).first()

    if not trainer:
        return {"message": "Trainer not found"}, 404

    return {"trainer": trainer.to_dict()}, 200


# POST - Create a new trainer
@trainer_routes.route('/', methods=['POST'])
def create_trainer():
    """
    Create a new trainer. Accessible by a manager.
    """
    data = request.get_json()

    # Retrieve necessary data from the request
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    description = data.get('description')
    url=data.get('url')
    # Ensure required data is present
    if not username or not email or not password:
        return {"message": "Missing required fields"}, 400

    # Check if a user with the same email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {"message": "User with this email already exists"}, 400

    # Create the new trainer
    new_user = User(
        username=username,
        email=email,
        password=password,  # Assuming password is hashed during user creation
        roles=[Role(isTrainer=True, describe=description, url=url)]
    )

    # Add the new trainer to the database
    db.session.add(new_user)
    db.session.commit()

    return {"message": "Trainer created successfully", "trainer": new_user.to_dict()}, 201

# PUT - Edit an existing trainer's information
@trainer_routes.route('/<int:id>', methods=['PUT'])
def edit_trainer(id):
    """
    Edit a trainer's information. Accessible by a manager.
    """
    data = request.get_json()

    # Find the trainer by ID
    trainer = User.query.get(id)
    if not trainer or not any(role.isTrainer for role in trainer.roles):
        return {"message": "Trainer not found"}, 404

    # Update trainer details
    trainer.username = data.get('username', trainer.username)
    trainer.email = data.get('email', trainer.email)
    trainer.roles[0].url = data.get('url', trainer.roles[0].url)
    trainer.roles[0].describe = data.get('description', trainer.roles[0].describe)

    db.session.commit()

    return {"message": "Trainer updated successfully", "trainer": trainer.to_dict()}, 200

# DELETE - Remove a trainer
@trainer_routes.route('/<int:id>', methods=['DELETE'])
def delete_trainer(id):
    """
    Delete a trainer by ID. Accessible by a manager.
    """
    trainer = User.query.get(id)

    # Check if the user is a trainer
    if not trainer or not any(role.isTrainer for role in trainer.roles):
        return {"message": "Trainer not found"}, 404

    db.session.delete(trainer)
    db.session.commit()

    return {"message": "Trainer deleted successfully"}, 200