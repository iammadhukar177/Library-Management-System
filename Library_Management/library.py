class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[book.isbn] = book

    def view_available_books(self):
        return [book for book in self.books.values() if book.is_available]

    def borrow_book(self, isbn: str):
        if isbn not in self.books or not self.books[isbn].is_available:
            raise ValueError("Book is not available to borrow.")
        self.books[isbn].is_available = False

    def return_book(self, isbn: str):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        self.books[isbn].is_available = True
