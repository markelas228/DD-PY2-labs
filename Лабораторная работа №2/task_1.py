class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        # Если books не передан, инициализируем пустым списком
        self.books = books if books is not None else []

    def get_next_book_id(self):
        if not self.books:  # Если книг нет, возвращаем id = 1
            return 1
        # Возвращаем id последней книги + 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):  # Используем enumerate для индексации
            if book.id == book_id:
                return index
        # Если книга с заданным id не найдена, вызываем ValueError
        raise ValueError("Книги с запрашиваемым id не существует")

# Пример использования
if __name__ == "__main__":
    # Создаем несколько книг
    book1 = Book(id_=1, name='Война и мир', pages=1225)
    book2 = Book(id_=2, name='Преступление и наказание', pages=671)

    # Создаем библиотеку
    library = Library(books=[book1, book2])

    # Добавляем новую книгу с автоматическим id
    next_id = library.get_next_book_id()
    new_book = Book(id_=next_id, name='Мастер и Маргарита', pages=470)
    library.books.append(new_book)

    # Выводим книги
    print(library.books)  # [Book(id_=1, name='Война и мир', pages=1225), ...]

    # Получаем индекс книги по id
    index = library.get_index_by_book_id(2)
    print(f"Индекс книги с id 2: {index}")

    # Пример обработки ошибки
    try:
        library.get_index_by_book_id(10)  # Книга с id 10 не существует
    except ValueError as e:
        print(e)
        