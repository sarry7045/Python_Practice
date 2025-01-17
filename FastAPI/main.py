from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

connection = MongoClient("mongodb+srv://Pyhthon_Course:Pyhthon_Course@cluster0.jmwcvzq.mongodb.net")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = connection.test.users.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": 1,
            "note": "note"
        })
        print("docs", doc)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}









# To start the server - fastapi dev main.py
# Mongo DB connect with Sarry Email