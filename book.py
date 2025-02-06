class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self.is_rented = False

    def is_available(self):
        return not self.is_rented

    def rent(self):
        self.is_rented = True

    def return_book(self):
        self.is_rented = False