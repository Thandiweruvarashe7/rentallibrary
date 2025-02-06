class Library:
    def __init__(self):
        self.books = {}
        self.rentals = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def get_book(self, book_id):
        return self.books.get(book_id)

    def rent_book(self, customer, book_id, rental_period):
        book = self.get_book(book_id)
        if book and book.is_available():
            book.rent()
            self.rentals[book_id] = {"customer": customer, "rental_period": rental_period}
            return book
        return None

    def return_book(self, customer, book_id):
        book = self.get_book(book_id)
        if book and not book.is_available():
            book.return_book()
            del self.rentals[book_id]

    def show_inventory(self):
        print("Library Inventory:")
        for book in self.books.values():
            print(f"{book.title} by {book.author} - {'Available' if book.is_available() else 'Rented'}")

    def show_rentals(self):
        print("Library Rentals:")
        for book_id, rental in self.rentals.items():
            book = self.get_book(book_id)
            print(f"{book.title} by {book.author} - Rented by {rental['customer'].name} for {rental['rental_period']} days")