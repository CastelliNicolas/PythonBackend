from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    email: str


users_list = [User(id=1, name="Nicolás", surname="Castelli", age=23, email="gggg@hotmail.com"),
              User(id=2, name="Fabricio", surname="Lopez", age=15, email="FLopez.com"),
              User(id=3, name="Joaquin", surname="Almagro", age=43, email="Almagro@Joa.com")]


@router.get("/users", status_code=200)
async def users():
    # Una lista vacia se interpreta como False en Python
    if not users_list:
        raise HTTPException(status_code=204)
    return users_list


# Path (el id es obligatorio)
@router.get("/user/{id}", response_model=User, status_code=200)
async def user(id: int):
    return search_users(id)


# Query
@router.get("/user/", response_model=User, status_code=200)
async def user(id: int):
    return search_users(id)


@router.post("/user/", response_model=User, status_code=201)
async def userAdd(user: User):
    for existing_user in users_list:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    users_list.append(user)
    return user


@router.put("/user/", response_model=User, status_code=200)
async def userPut(user: User):
    found = False
    for index, user_found in enumerate(users_list):
        if user_found.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    else:
        return user


@router.delete("/user/{id}", status_code=200)
async def userDelete(id: int):
    found = False
    for index, user_found in enumerate(users_list):
        if user_found.id == id:
            del users_list[index]
            found = True
    if not found:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    else:
        return {"Se ha borrado el usuario"}


def search_users(id):
    # filter devuelve un objeto iterador <filter object at 0x000001B1C82DA1D0>
    userss = filter(lambda user: user.id == id, users_list)
    try:
        # la funcion list me permite obtener los elementos originales del objeto iterador
        return list(userss)[0]
    except:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
