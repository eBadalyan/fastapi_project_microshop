from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel, EmailStr

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {
        "message": "Hello index1!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.title().strip()
    return {"message": f"Hello {name}"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@app.get("/items/{items_id}/")
def get_item_by_id(items_id: int):
    return {
        "item": {
            "id": items_id,
        },
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
