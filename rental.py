import datetime

class Rental:
    def __init__(self, customer, book, rental_period=7):
        self.customer = customer
        self.book = book
        self.rental_date = datetime.date.today()
        self.due_date = self.rental_date + datetime.timedelta(days=rental_period)

    def is_overdue(self):
        return datetime.date.today() > self.due_date

    def return_book(self):
        self.book.return_book()
        return f"{self.book.title} returned by {self.customer.name}."
