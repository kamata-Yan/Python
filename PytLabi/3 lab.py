class Library:
    # Атрибут класса для хранения количества созданных объектов
    libraries_quantity = 0

    def __init__(self):
        # Инициализация атрибута экземпляра для хранения книг
        self.books = {}
        Library.libraries_quantity += 1

    def add_book(self, title):
        """Добавляет книгу в библиотеку и устанавливает её доступность."""
        self.books[title] = True  # Книга доступна

    def remove_book(self, title):
        """Удаляет книгу из библиотеки по названию."""
        if title in self.books:
            del self.books[title]

    def find_book(self, title):
        """Проверяет, есть ли книга в библиотеке и доступна ли она."""
        if title in self.books:
            return self.books[title]  # Возвращает True или False
        return None  # Если книги нет в библиотеке

    def show_all_available_books(self):
        """Возвращает список всех доступных книг в библиотеке."""
        available_books = [title for title, available in self.books.items() if available]
        return available_books


# Пример использования класса Library
if __name__ == "__main__":
    my_library = Library()
    
    # Добавление книг
    my_library.add_book("1984")
    my_library.add_book("To Kill a Mockingbird")
    my_library.add_book("The Great Gatsby")

    # Печать всех доступных книг
    print("Доступные книги:", my_library.show_all_available_books())

    # Проверка наличия книги
    print("Наличие '1984':", my_library.find_book("1984"))  # Должно вернуть True

    # Удаление книги
    my_library.remove_book("1984")

    # Проверка наличия книги после удаления
    print("Наличие '1984' после удаления:", my_library.find_book("1984"))  # Должно вернуть None

    # Печать всех доступных книг после удаления
    print("Доступные книги после удаления:", my_library.show_all_available_books())

    # Печать количества созданных библиотек
    print("Количество созданных библиотек:", Library.libraries_quantity)
