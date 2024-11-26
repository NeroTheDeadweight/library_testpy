import unittest
import os
from models import Book
from save_load_json import load_books, save_books, DATA_FILE
import json

import unittest
import os

from main import add_book, delete_book, search_book, change_status, display_books

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        """Создание тестовых данных перед каждым тестом."""
        self.test_data = [
            {"id": 1, "title": "Book One", "author": "Author One", "year": 2001, "status": "в наличии"},
            {"id": 2, "title": "Book Two", "author": "Author Two", "year": 2002, "status": "выдана"}
        ]
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.test_data, f)

    def tearDown(self):
        """Удаление тестовых данных после каждого теста."""
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)

    def test_add_book(self):
        """Тест добавления книги."""
        add_book("Book Three", "Author Three", 2003)
        books = load_books()
        self.assertEqual(len(books), 3)
        self.assertEqual(books[-1].title, "Book Three")

    def test_delete_book(self):
        """Тест удаления книги."""
        delete_book(1)
        books = load_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].id, 2)

    def test_search_book(self):
        """Тест поиска книги."""
        result = search_book("Book One")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].author, "Author One")

    def test_change_status(self):
        """Тест изменения статуса книги."""
        change_status(1, "выдана")
        books = load_books()
        self.assertEqual(books[0].status, "выдана")

    def test_display_books(self):
        """Тест отображения всех книг."""
        books = display_books()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "Book One")

if __name__ == '__main__':
    unittest.main()