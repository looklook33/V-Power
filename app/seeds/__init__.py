from flask.cli import AppGroup
from .users import seed_users, undo_users
from .equipment import seed_equipment, undo_equipment
from .galleries import seed_galleries, undo_galleries
from .schedules import seed_schedules, undo_schedules
from .roles import seed_roles, undo_roles
from .schedule_users import seed_schedule_users, undo_schedule_users
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
    seed_users()
    seed_equipment()
    seed_galleries()
    seed_schedules()
    seed_roles()
    seed_schedule_users()


    
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_schedule_users() # Remove schedule_users associations
    undo_equipment()
    undo_schedules()
    undo_galleries()
    undo_roles()
    undo_users()

    # Add other undo functions here
