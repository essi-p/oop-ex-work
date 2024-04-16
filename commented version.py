# file: bookstore.py
# authors: Essi Peltola, Iida Kärkkäinen, Jonna Lundell
# descriptions: A simple online bookstore system with classes for managing books, customers, orders, and different types of books.

# Define the Book class
# Classes define the properties and the behaviour of the objects used
class Book:
    # Constructor to initialize a book object with title, author, and price
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

# Define the Customer class
class Customer:
    # Constructor to initialize a customer object with name and email
    def __init__(self, name, email):
        self.name = name
        self.email = email 

# Define the Order class
class Order:
    # Constructor to initialize an order object with a customer and an empty list of books
    def __init__(self, customer):
        self.customer = customer
        self.books = []

    # Method to add a book to the order
    def add_book(self, book):
        self.books.append(book)

#Example of polymorphism and inheritance:
# Define the Fiction subclass of Book
class Fiction(Book):
    # Constructor to initialize a fiction book with title, author, price, and genre
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre 

    # Method to apply discount for fiction books
    def apply_discount(self):
        self.price *= 0.8  # 20% discount for fiction books

# Polymorphism in this case: same method name is used in both subclasses, but each of them provides its own specific implementation of the method

# Define the NonFiction subclass of Book
class NonFiction(Book):
    # Constructor to initialize a non-fiction book with title, author, price, and subject
    def __init__(self, title, author, price, subject):
        super().__init__(title, author, price)
        self.subject = subject

    # Method to apply discount for non-fiction books
    def apply_discount(self):
        self.price *= 0.9  # 10% discount for non-fiction books

# Function to process the order, example of objects passed as functions
def process_order(customer, books):
    order = Order(customer) # Here, an instance of the Customer class is passed as an argument
    for book in books: # Here, each book object from the list 'books' is passed as an argument
        order.add_book(book) #  Here, each book object is passed as an argument to the 'add_book' method of the Order class
    return order

# Function to display available books and let the user choose
# Integration of data structures, list and dictionary
def select_books(books):
    # Display available books
    print("Available Books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.title} by {book.author} - {book.price}€")
    
    # Prompt user to select books
    choices = input("Enter the numbers of books you want to purchase (separated by commas): ").split(',')
    selected_books = []
    for choice in choices:
        choice = int(choice.strip()) - 1
        if choice >= 0 and choice < len(books):
            selected_books.append(books[choice])
    return selected_books

# Sample books
books = [
    Fiction("The Great Gatsby", "F. Scott Fitzgerald", 15.99, "Classic"),
    NonFiction("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 19.99, "History"),
    Fiction("To Kill a Mockingbird", "Harper Lee", 12.99, "Classic"),
    NonFiction("Educated: A Memoir", "Tara Westover", 14.99, "Memoir")
]

# Welcome message and input customer details
print("Welcome to the Online Bookstore!")
customer_name = input("Enter your name: ")
customer_email = input("Enter your email: ")
customer = Customer(customer_name, customer_email)

# Let the customer select books
selected_books = select_books(books)

# Process the order
order = process_order(customer, selected_books)

# Display order summary
print("\nOrder Summary:")
print("Customer:", order.customer.name)
print("Books:")
for book in order.books:
    print("-", book.title)
total_price = sum(book.price for book in order.books)
print("Total Price:", total_price, "€")



