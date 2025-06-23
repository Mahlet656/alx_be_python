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
            # The isinstance order is important. Check for derived classes first.
            if isinstance(book, EBook):
                # The corrected line below no longer adds "KB"
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                # This handles the base Book class
                print(f"Book: {book.title} by {book.author}")
