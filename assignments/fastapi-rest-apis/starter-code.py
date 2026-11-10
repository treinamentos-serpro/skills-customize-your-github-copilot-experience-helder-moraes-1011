from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books in the catalog.
    return []


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # TODO: Assign an ID, save the book, and return it.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the book or raise HTTPException with status 404.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    # TODO: Replace the book data or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Remove the book or raise HTTPException with status 404.
    raise NotImplementedError