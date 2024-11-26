class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """Конвертирует объект книги в словарь для сохранения в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        """Создает объект книги из словаря."""
        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])

