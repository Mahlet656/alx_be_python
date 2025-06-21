class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return
    def list_available_books(self):
        available_books = [b for b in self._books if not b._is_checked_out]
        for book in available_books:
            print(f"{book.title} by {book.author}")
