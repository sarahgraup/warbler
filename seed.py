"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User, Message, Follows, Like

db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/messages.csv') as messages:
    db.session.bulk_insert_mappings(Message, DictReader(messages))

with open('generator/follows.csv') as follows:
    db.session.bulk_insert_mappings(Follows, DictReader(follows))

# sarah = User(
#     id = 0,
#     email = 'sarah@sarah.com',
#     username = 'sarah',
#     password = 'sarahg'
# )
# db.session.add(sarah)

# sarahs_liked_message = Like(
#     message_id = 909,
#     user_id = 0
# )

# db.session.add(sarahs_liked_message)

db.session.commit()
