
import datetime

class Rental:
    def __init__(self, customer, book, rental_date, due_date):
        self.customer = customer
        self.book = book
        self.rental_date = rental_date
        self.due_date = due_date