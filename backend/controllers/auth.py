from dotenv import load_dotenv
from fastapi_jwt_auth2.auth_jwt import AuthJWT
from typing import List
import base64
import sys
from database import engine

sys.path.append("../../relative_face_recognition_app")
from models.user import User
import requests
from datetime import timedelta
import os

load_dotenv()

# Get the environment variables and check if they are not None
access_token_expires_in_str = os.getenv("ACCESS_TOKEN_EXPIRES_IN")
refresh_token_expires_in_str = os.getenv("REFRESH_TOKEN_EXPIRES_IN")

if access_token_expires_in_str is None:
    raise ValueError("ACCESS_TOKEN_EXPIRES_IN environment variable is not set.")
if refresh_token_expires_in_str is None:
    raise ValueError("REFRESH_TOKEN_EXPIRES_IN environment variable is not set.")

# Convert the values to integers
ACCESS_TOKEN_EXPIRES_IN = int(access_token_expires_in_str)
REFRESH_TOKEN_EXPIRES_IN = int(refresh_token_expires_in_str)


class UserAuth:
    URL = "http://localhost:8080/users/1"

    def __init__(self, user):
        self.user = user

    def log_in(self, provided_username, provided_password):
        data = requests.get(url=self.URL)
        json_data = data.json()
        api_username = json_data["username"]
        api_password = json_data["password"]

        if (provided_username == api_username) and (provided_password == api_password):
            access_token = AuthJWT.create_access_token(
                subject=str(self.user.id),
                expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN),
            )
            refresh_token = AuthJWT.create_refresh_token(
                subject=str(self.user.id),
                expires_time=timedelta(minutes=REFRESH_TOKEN_EXPIRES_IN),
            )
            return {"status": 200, "access_token": access_token}
        else:
            return {"status": 400, "message": "Username or password is not correct !!!"}

    def register(self, provided_username, provided_email, provided_password):
        new_user_data = {
            "username": provided_username,
            "email": provided_email,
            "password": provided_password,
        }

        # Assuming you have an API endpoint to register a new user
        register_url = "http://localhost:8080/users/register"

        response = requests.post(register_url, json=new_user_data)

        if response.status_code == 200:
            return {"status": 200, "message": "User registered successfully !!!"}
        else:
            return {
                "status": response.status_code,
                "message": "Failed to register user.",
            }
