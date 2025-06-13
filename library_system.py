from library import Library 
from book import Book
from rental import Rental
from customer import Customer

class LibrarySystem:
    def __init__(self):
        self.library = Library()

    def main_menu(self):
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
                self.library.add_book(title, author, genre)
            
            elif choice == "2":
                self.rent_book_process()
            elif choice == "3":
                self.return_book_process()
            elif choice == "4":
                self.library.show_inventory()
            elif choice == "5":
                self.library.show_rentals()
            elif choice == "6":
                print("Exiting the library system.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def rent_book_process(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        customer = Customer(name, email)
        book_id = int(input("Enter the book ID: "))
        rental_period = int(input("Enter the rental period (in days): "))
        self.library.rent_book(customer, book_id, rental_period)

    def return_book_process(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        customer = Customer(name, email)
        book_id = int(input("Enter the book ID: "))
        self.library.return_book(customer, book_id)








