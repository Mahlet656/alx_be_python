class Book:
    """A base class for a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    """A class for an electronic book, inheriting from Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """A class for a physical book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """A class representing a library that holds a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book object to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Lists the details of all books in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
