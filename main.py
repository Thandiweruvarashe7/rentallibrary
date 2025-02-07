from book import Book
from customer import Customer
from library import Library
from rental import Rental

class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self.is_available = True
        self.rented_by = None

    def is_rented_by(self, customer):
        return self.rented_by == customer

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Rental:
    def __init__(self, customer, book, rental_period):
        self.customer = customer
        self.book = book
        self.rental_period = rental_period
        self.rental_date = None
        self.return_date = None

class Library:
    def __init__(self):
        self.books = []
        self.rentals = []

    def add_book(self, book):
        self.books.append(book)

    def get_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def rent_book(self, customer, book_id, rental_period):
        book = self.get_book(book_id)
        if book and book.is_available:
            book.is_available = False
            book.rented_by = customer
            rental = Rental(customer, book, rental_period)
            self.rentals.append(rental)
            return rental
        return None

    def return_book(self, customer, book_id):
        book = self.get_book(book_id)
        if book and book.is_rented_by(customer):
            book.is_available = True
            book.rented_by = None
            self.rentals = [rental for rental in self.rentals if rental.book != book]

    def show_inventory(self):
        print("Book Inventory:")
        for book in self.books:
            print(f"{book.title} by {book.author} - {'Available' if book.is_available else 'Rented'}")

    def show_rentals(self):
        print("Book Rentals:")
        for rental in self.rentals:
            print(f"{rental.book.title} by {rental.book.author} - Rented by {rental.customer.name}")

def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Rent a book")
        print("3. Return a book")
        print("4. Show inventory")
        print("5. Show rentals")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            genre = input("Enter the book genre: ")
            book_id = int(input("Enter the book ID: "))
            book = Book(title, author, genre, book_id)
            library.add_book(book)
            print(f"{book.title} by {book.author} added successfully.")

        elif choice == "2":
            book_id = int(input("Enter the book ID: "))
            customer_name = input("Enter your name: ")
            customer_email = input("Enter your email: ")
            rental_period = int(input("Enter the rental period (in days): "))
            customer = Customer(customer_name, customer_email)
            rental = library.rent_book(customer, book_id, rental_period)
            if rental:
                print(f"{rental.book.title} by {rental.book.author} rented successfully.")
            else:
                print("Book not available for rent.")

        elif choice == "3":
            book_id = int(input("Enter the book ID: "))
            customer_name = input("Enter your name: ")
            customer_email = input("Enter your email: ")
            customer = Customer(customer_name, customer_email)

            book = library.get_book(book_id)
            if book and book.is_rented_by(customer):
                library.return_book(customer, book_id)
                print(f"{book.title} by {book.author} returned successfully.")
            else:
                print("Book not found or not rented by you.")

        elif choice == "4":
            library.show_inventory()

        elif choice == "5":
            library.show_rentals()

        elif choice == "6":
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


           
