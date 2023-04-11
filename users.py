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
    # Una lista vacia se interpreta como False en Python
    if not users_list:
        return {"error": "No existen usuarios"}
    return users_list


# Path (el id es obligatorio)
@app.get("/user/{id}")
async def user(id: int):
    return search_users(id)


# Query
@app.get("/user/")
async def user(id: int):
    return search_users(id)


@app.post("/user/", status_code=201)
async def userAdd(user: User):
    if type(search_users(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return "Se ha agregado:", user


@app.put("/user/")
async def userPut(user: User):
    found = False
    for index, user_found in enumerate(users_list):
        if user_found.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "Usuario no se ha actualizado"}
    else:
        return user


@app.delete("/user/{id}")
async def userDelete(id: int):
    found = False
    for index, user_found in enumerate(users_list):
        if user_found.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "Usuario no se ha borrado"}
    else:
        return {"Se ha borrado el usuario"}


def search_users(id):
    # filter devuelve un objeto iterador <filter object at 0x000001B1C82DA1D0>
    userss = filter(lambda user: user.id == id, users_list)
    try:
        # la funcion list me permite obtener los elementos originales del objeto iterador
        return list(userss)[0]
    except:
        return "{error: Usuario no encontrado}"
