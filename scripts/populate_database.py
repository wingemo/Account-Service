# account-services/scripts/populate_database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_database import DATABASE_URL, users

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

test_data = [
    {"username": "john_doe", "email": "john@example.com"},
    {"username": "jane_doe", "email": "jane@example.com"},
    {"username": "alice_smith", "email": "alice@example.com"},
    {"username": "bob_jones", "email": "bob@example.com"},
    {"username": "charlie_brown", "email": "charlie@example.com"},
    # Lägg till mer testdata om det behövs
]

for data in test_data:
    session.execute(users.insert().values(data))

session.commit()

print("Database populated with data.")
