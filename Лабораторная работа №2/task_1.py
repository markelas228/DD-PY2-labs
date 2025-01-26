class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'\u041a\u043d\u0438\u0433\u0430 "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("\u041a\u043d\u0438\u0433\u0438 \u0441 \u0437\u0430\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0435\u043c\u044b\u043c id \u043d\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442")

# Пример использования
if __name__ == "__main__":
    # Создаем книги
    book1 = Book(1, "Война и мир", 1225)
    book2 = Book(2, "Преступление и наказание", 671)

    # Создаем библиотеку
    library = Library([book1, book2])

    # Выводим следующего ID для новой книги
    print(library.get_next_book_id())  # Ожидается 3

    # Получаем индекс книги по ID
    print(library.get_index_by_book_id(1))  # Ожидается 0

    # Пробуем вызвать ошибку, запрашивая несуществующий ID
    try:
        library.get_index_by_book_id(3)
    except ValueError as e:
        print(e)  # "Книги с запрашиваемым id не существует"