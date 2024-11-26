import json
import os
from typing import List
from models import Book

DATA_FILE = "library.json"


def load_books() -> List[Book]:
    """Загружает книги из JSON-файла."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [Book.from_dict(book) for book in data]


def save_books(books: List[Book]) -> None:
    """Сохраняет список книг в JSON-файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([book.to_dict() for book in books], file, ensure_ascii=False, indent=4)