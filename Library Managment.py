class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def register_patron(self, name):
        self.patrons.append(Patron(name))

    def borrow_book(self, patron_name, book_title):
        patron = None
        for p in self.patrons:
            if p.name == patron_name:
                patron = p
                break

        if patron is None:
            print("Patron not found!")
            return

        for book in self.books:
            if book.title == book_title:
                if book.available:
                    book.available = False
                    patron.borrowed_books.append(book)
                    print("Book borrowed successfully.")
                else:
                    print("Book is already borrowed.")
                return

        print("Book not found!")

    def return_book(self, patron_name, book_title):
        patron = None
        for p in self.patrons:
            if p.name == patron_name:
                patron = p
                break

        if patron is None:
            print("Patron not found!")
            return

        for book in patron.borrowed_books:
            if book.title == book_title:
                book.available = True
                patron.borrowed_books.remove(book)
                print("Book returned successfully.")
                return

        print("Book not borrowed by this patron.")

    def display_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")


# Main Program
library = Library()

# Add Books
n = int(input("How many books do you want to add? "))
for i in range(n):
    print(f"\nBook {i+1}")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    library.add_book(title, author)

# Register Patrons
m = int(input("\nHow many patrons do you want to register? "))
for i in range(m):
    name = input(f"Enter patron {i+1} name: ")
    library.register_patron(name)

# Menu
while True:
    print("\n----- Library Menu -----")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.display_books()

    elif choice == 2:
        patron = input("Enter patron name: ")
        book = input("Enter book title: ")
        library.borrow_book(patron, book)

    elif choice == 3:
        patron = input("Enter patron name: ")
        book = input("Enter book title: ")
        library.return_book(patron, book)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
