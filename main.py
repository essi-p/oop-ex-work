# Define the Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

# Define the Customer class
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email 

# Define the Order class (g)
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.books = []

    def add_book(self, book):
        self.books.append(book)

# Define the Fiction subclass of Book (h)
class Fiction(Book):
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre 

    def apply_discount(self):
        self.price *= 0.8  # 20% discount for fiction books (k)

# Define the NonFiction subclass of Book (h)
class NonFiction(Book):
    def __init__(self, title, author, price, subject):
        super().__init__(title, author, price)
        self.subject = subject

    def apply_discount(self):
        self.price *= 0.9  # 10% discount for non-fiction books (k)

# Function to process the order (i)
def process_order(customer, books):
    order = Order(customer)
    for book in books:
        order.add_book(book)
    return order

# Function to display available books and let the user choose (j, i)
def select_books(books):
    print("Available Books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.title} by {book.author} - ${book.price}")
    
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

# Welcome message and input customer details (i)
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
print("Total Price: $", total_price)
