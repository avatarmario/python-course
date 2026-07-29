class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is not available.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"{self.name} cannot borrow '{book.title}' because it is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} cannot return '{book.title}' because it was not borrowed.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' has been added to the library.")

    def borrow_book(self, book, user):
        if book in self.books and user in self.users:
            user.borrow_book(book)
        else:
            print("Either the book or the user is not registered in the library.")

    def return_book(self, book, user):
        if book in self.books and user in self.users:
            user.return_book(book)
        else:
            print("Either the book or the user is not registered in the library.")

    def show_available_books(self):
        print("Available books in the library:")
        for book in self.books:
            if book.is_available:
                print(f"- {book.title} by {book.autor}")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

user1 = User("Mario", 1)
user2 = User("Adriana", 2)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_user(user1)
library.add_user(user2)

library.show_available_books()
library.borrow_book(book1, user1)
library.show_available_books()
library.borrow_book(book2, user2)
library.show_available_books()
library.return_book(book1, user1)
library.show_available_books()