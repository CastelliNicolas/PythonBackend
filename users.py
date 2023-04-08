from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    email: str


users_list = [User(id=1, name="Nicolás", surname="Castelli", age=23, email="gggg@hotmail.com"),
              User(id=2, name="Fabricio", surname="Lopez", age=15, email="FLopez.com"),
              User(id=3, name="Joaquin", surname="Almagro", age=43, email="Almagro@Joa.com")]


@app.get("/users")
async def users():
    return users_list


@app.get("/user/{id}")
async def user(id: int):
    userss = filter(lambda user: user.id == id, users_list)
    try:
        return list(userss)[0]
    except:
        return "{error: Usuario no encontrado}"


@app.get("/userquery/")
async def user(id: int):
    userss = filter(lambda user: user.id == id, users_list)
    try:
        return list(userss)[0]
    except:
        return "{error: Usuario no encontrado}"

