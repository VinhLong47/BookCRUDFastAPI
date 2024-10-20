from fastapi import FastAPI, APIRouter, HTTPException
from database.models import Book
from database.schemas import all_book_data, individual_book_data
from config import collection
from bson.objectid import ObjectId
from datetime import datetime


app = FastAPI()
router = APIRouter()


@router.get("/")
async def get_all_books():
    data = collection.find({"is_deleted": False})
    return all_book_data(data)


@router.post("/")
async def create_book(new_book: Book):
    try:
        resp = collection.insert_one(new_book.dict())
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=400, detail="Something went wrong")


@router.put("/{book_id}")
async def update_book(book_id: str, updated_book: Book):
    try:
        id = ObjectId(book_id)
        existing_book = collection.find_one({"_id": id, "is_deleted": False})
        if not existing_book:
            raise HTTPException(status_code=404, detail="Book does not exist")
        updated_book.updated = datetime.timestamp(datetime.now())
        resp = collection.update_one({"_id": id}, {"$set": updated_book.dict()})
        return {"status_code": 200, "message": "Book updated successfully"}
    except Exception as e:
        return HTTPException(status_code=400, detail="Something went wrong")


@router.delete("/{book_id}")
async def delete_book(book_id:str):
    try:
        id = ObjectId(book_id)
        existing_book = collection.find_one({"_id": id, "is_deleted": False})
        if not existing_book:
            raise HTTPException(status_code=404, detail="Book does not exist")
        resp = collection.update_one({"_id": id}, {"$set": {"is_deleted": True}})
        return {"status_code": 200, "message": "Book Deleted successfully"}
    except Exception as e:
        return HTTPException(status_code=400, detail="Something went wrong")

app.include_router(router)
