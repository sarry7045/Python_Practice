def NoteEntity(item) -> dict:
    return { 
        "id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"]
    }


def NotesEntity(items) -> list:
    return [NoteEntity(items) for item in items]