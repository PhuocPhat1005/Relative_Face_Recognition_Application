import sys

from models.user import User

sys.path.append("../../relative_face_recognition_app")
from database.engine import engine
from models import *
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

# [{
#     "city_name": "New York",
#     "districs": [("Manhattan", 1), ("Brooklyn", 2), ("Queens", 3), ("Bronx", 4), ("Staten Island", 5)]
# }]


@app.get("/users/{user_id}", response_model=user.User)
def read_user(user_id: int):
    with Session(engine) as session:
        found_user = session.get(user.User, user_id)
        if not found_user:
            raise HTTPException(status_code=404, detail="User not found")
        return found_user


# Define a helper function to get a user by username
def get_user_by_username(username: str, session: Session):
    statement = select(User).where(User.username == username)
    result = session.exec(statement)
    return result.first()


# Login endpoint
@app.post("/auth/login")
def login(username: str, password: str):
    with Session(engine) as session:
        user = get_user_by_username(username, session)
        if user and user.password == password:
            return {"status": 200, "message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")


# Register endpoint
@app.post("/auth/register")
def register(username: str, email: str, password: str):
    with Session(engine) as session:
        # Check if the username already exists
        existing_user = get_user_by_username(username, session)
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        # Create a new user
        new_user = User(username=username, email=email, password=password)
        session.add(new_user)
        session.commit()

        return {"status": 200, "message": "User registered successfully"}
