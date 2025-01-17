from fastapi import APIRouter
from typing import Union
from models.note import Note
from config.db import connection
from schemas.schemas import NoteEntity, NotesEntity
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
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


@note.post("//")
def add_note(note: Note):
    inserted_note = connection.test.users.insert_one(dict(note))
    return NoteEntity(inserted_note)


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    note = connection.test.users(dict(form)) 
    return {"Succcess": True}
