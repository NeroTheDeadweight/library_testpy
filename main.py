from typing import List
from models import Book
from save_load_json import load_books, save_books

def generate_id(books):
    """Генерация Id для списка книг с 1"""
    return max((book.id for book in books), default=0) + 1

def add_book(title: str | None = None, author: str | None = None, year: int | None= None):
    """Добавление книги"""
    if title is None and author is None and year is None:
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        while True:
            try:
                year = int(input("Введите год издания: "))
                break
            except ValueError:
                print("Некорректный ввод")
    books = load_books()
    new_book = Book(generate_id(books), title, author, year)
    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' добавлена.")

def delete_book(book_id: int|None = None):
    "Удаление книги по id"
    if book_id is None:
        book_id = int(input("Введите ID книги для удаления: "))
    books = load_books()
    books = [book for book in books if book.id != book_id]  # Реализация удлаения книги через перезапись всего списка
    save_books(books)
    print(f"Книга с ID {book_id} удалена.")

def search_book(search_query:str | None= None) -> List[Book]:
    """Поиск книги по атрибуту"""
    if search_query is None:
        search_query = input("Введите id, title, author или year для поиска: ").lower()
    else:
        search_query = search_query.lower()
    books = load_books()
    results = [book for book in books if search_query in ( str(book.id),book.title.lower(), book.author.lower(), str(book.year))]
    for book in results:
        print(book.__dict__)
    return results

def change_status(book_id: int|None = None, new_status: str | None = None):
    """ Изменение статуса наличия книги"""
    if book_id is None:
        book_id = int(input("Введите ID книги для изменения статуса: "))
    if new_status is None:
        print("Введите новый статус ")
        while True:
            print("10. В наличии")
            print("11. Выдана")
            choice = input("Выберите статус: ")
            if choice == "10":
                new_status = "в наличии"
                break
            elif choice == "11":
                new_status = "выдана"
                break
            else:
                print("Некорректный ввод")
    books = load_books()
    for book in books:
        if book.id == book_id:
            book.status = new_status
            save_books(books)
            print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
            return
    print(f"Книга с ID {book_id} не найдена.")

def display_books() -> List[Book] :
    """Вывод в консоль всего списка книг"""
    books = load_books()
    for book in books:
        print(book.__dict__)
    return books

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите операцию: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            change_status()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()