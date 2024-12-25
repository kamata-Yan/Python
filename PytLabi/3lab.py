class Library:
    libraries_quantity = 0

    def __init__(self):
        self.books = {}
        Library.libraries_quantity += 1

    def add_book(self, title):
        self.books[title] = True  

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]

    def find_book(self, title):
        if title in self.books:
            return self.books[title] 
        return None  

    def show_all_available_books(self):
        available_books = [title for title, available in self.books.items() if available]
        return available_books



if __name__ == "__main__":
    my_library = Library()
    

    my_library.add_book("1984")
    my_library.add_book("To Kill a Mockingbird")
    my_library.add_book("The Great Gatsby")

    print("Доступные книги:", my_library.show_all_available_books())


    print("Наличие '1984':", my_library.find_book("1984")) 


    my_library.remove_book("1984")

    print("Наличие '1984' после удаления:", my_library.find_book("1984")) 

    print("Доступные книги после удаления:", my_library.show_all_available_books())

    print("Количество созданных библиотек:", Library.libraries_quantity)





