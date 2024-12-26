import unittest
from library_management.library import Book, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("123", "Python 101", "John Doe", 2020)
        self.book2 = Book("456", "Learn Java", "Jane Doe", 2019)

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertIn("123", self.library.books)

        # Test adding a duplicate book
        with self.assertRaises(ValueError):
            self.library.add_book(self.book1)

    def test_view_available_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 2)

    def test_borrow_book(self):
        self.library.add_book(self.book1)
        self.library.borrow_book("123")
        self.assertFalse(self.book1.is_available)

        with self.assertRaises(ValueError):
            self.library.borrow_book("123")  # Already borrowed

    def test_return_book(self):
        self.library.add_book(self.book1)
        self.library.borrow_book("123")
        self.library.return_book("123")
        self.assertTrue(self.book1.is_available)

if __name__ == "__main__":
    unittest.main()
