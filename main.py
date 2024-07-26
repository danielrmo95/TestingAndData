from fastapi import FastAPI
from routes.user import get_users, create_user, get_user_by_id
from schema.user import User
from models.user import UserModel
app= FastAPI()


@app.get("/getusers")
def read_users():
    return get_users()


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    return get_user_by_id(user_id)


@app.post("/postusers", response_model=dict)
def create_user_route(new_user: User):
    return create_user(new_user)


@app.get("/prueba")
def get_prueba():
    return "Hello world"


