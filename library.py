from book import Book  
from rental import Rental 
from customer import Customer  
import pickle

class Library:
    def __init__(self):
        self.books = [] 
        self.rentals = {}  
        self.book_id_counter = 101 
        self.log_file = "library_books_log.txt"
        self.data_file = "library_data.pkl"
        self.load_data()  # load books and rentals if previously saved

    def add_book(self, title, author, genre):
        book_id = self.generate_book_id() 
        book = Book(title, author, genre, book_id) 
        self.books.append(book) 
        self.log_book(f"Book Added: {book}")
        print(f"Book added: {book}")
        self.save_data()  # save after adding book

    def generate_book_id(self):
        new_id = self.book_id_counter
        self.book_id_counter += 1
        return new_id

    def log_book(self, entry):
        with open(self.log_file, "a") as file:
            file.write(entry + "\n")

    def rent_book(self, customer, book_id, rental_period):
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
                self.save_data()  # save after renting
                return
        print("Book not available for rent.")

    def return_book(self, customer, book_id):
        if book_id in self.rentals:
            rental = self.rentals[book_id]
            if rental.customer == customer:
                rental.book.return_book() 
                del self.rentals[book_id]  
                log_entry = f"Book Returned: {rental.book} | Renter: {customer.name}"
                self.log_book(log_entry)  
                print(f"{customer.name} returned '{rental.book.title}'.")
                self.save_data()  # save after return
                return
        print("This book was not rented by you or does not exist.")

    def show_inventory(self):
        print("\nLibrary Inventory:")
        if not self.books:
            print("No books available.")
        for book in self.books:
            status = "Available" if book.is_available else "Rented"
            print(f"{book} - {status}")
   
    def show_rentals(self):
        print("\nCurrent Rentals:")
        if not self.rentals:
            print("No books currently rented.")
        for rental in self.rentals.values():
            print(f"{rental.customer} rented '{rental.book.title}' until {rental.due_date}.")

    def save_data(self):
        with open(self.data_file, "wb") as f:
            pickle.dump((self.books, self.rentals, self.book_id_counter), f)

    def load_data(self):
        try:
            with open(self.data_file, "rb") as f:
                self.books, self.rentals, self.book_id_counter = pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            pass  # Start fresh if file doesn't exist or is corrupted




