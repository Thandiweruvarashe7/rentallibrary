from book import Book  
from rental import Rental 
from customer import Customer  

class Library:
    def __init__(self):
        self.books = [] 
        self.rentals = {}  
        self.book_id_counter = 101 
        self.log_file = "library_books_log.txt" 

    def add_book(self, title, author, genre):
        """Add a single book to the library."""
        book_id = self.generate_book_id() 
        book = Book(title, author, genre, book_id) 
        self.books.append(book) 
        self.log_book(f"Book Added: {book}")
        print(f"Book added: {book}") 
    def generate_book_id(self):
        """Generate a unique book ID."""
        new_id = self.book_id_counter
        self.book_id_counter += 1
        return new_id

    def log_book(self, entry):
        """Log book activity to a file."""
        with open(self.log_file, "a") as file:
            file.write(entry + "\n")

    def rent_book(self, customer, book_id, rental_period):
        """Rent a book to a customer."""
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.rent()  
                rental = Rental(customer, book, rental_period)  
                self.rentals[book_id] = rental 
                log_entry = (
                    f"Book Rented: {book} | Renter: {customer.name} | "
                    f"Due: {rental.due_date}"
                )
                self.log_book(log_entry) 
                print(f"{customer.name} rented '{book.title}' for {rental_period} days.")
                return
        print("Book not available for rent.")

    def return_book(self, customer, book_id):
        """Return a rented book."""
        if book_id in self.rentals:
            rental = self.rentals[book_id]
            if rental.customer == customer:
                rental.book.return_book() 
                del self.rentals[book_id]  
                log_entry = f"Book Returned: {rental.book} | Renter: {customer.name}"
                self.log_book(log_entry)  
                print(f"{customer.name} returned '{rental.book.title}'.")
                return
        print("This book was not rented by you or does not exist.")

    def show_inventory(self):
        """Display the available books in the library."""
        print("\nLibrary Inventory:")
        if not self.books:
            print("No books available.")
        for book in self.books:
            status = "Available" if book.is_available else "Rented"
            print(f"{book} - {status}")
   
    def show_rentals(self):
        """Display the current rentals."""
        print("\nCurrent Rentals:")
        if not self.rentals:
            print("No books currently rented.")
        for rental in self.rentals.values():
            print(f"{rental.customer} rented '{rental.book.title}' until {rental.due_date}.")

