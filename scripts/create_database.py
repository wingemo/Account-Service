# account-services/scripts/create_database.py
from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table

DATABASE_URL = "sqlite:///./database/test.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String, index=True),
    Column("email", String),
)

metadata.create_all(bind=engine)

print("Database created.")
