class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.genre}) - ID: {self.book_id}"

    def rent(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True



