class Book:
    def __init__(self, title, author, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str):
        for book in self.books:
            if book.title == title:
                print(f'Book "{book.title}" found')
                return book
        print(f'Book "{title}" not found')


book1 = Book('Lord of the rings', 'Tolkien', 400)
book2 = Book('Narnia', 'BAI IVAN', 60000)

my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)

my_library.find_book('Lord of the rings')
my_library.find_book('Titanic: Blood and Honour')
my_library.find_book('Narnia')

print(book2.author)
print(book2.pages)
