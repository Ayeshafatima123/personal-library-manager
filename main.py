import json
import os

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn
        }

    @staticmethod
    def from_dict(data):
        return Book(data['title'], data['author'], data['year'], data['isbn'])


class LibraryManager:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()

    def search_books(self, keyword):
        return [b for b in self.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]

    def list_books(self):
        return self.books

    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data]

# Example usage
if __name__ == "__main__":
    library = LibraryManager()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. List All Books")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            isbn = input("ISBN: ")
            library.add_book(Book(title, author, year, isbn))
        elif choice == '2':
            isbn = input("Enter ISBN to remove: ")
            library.remove_book(isbn)
        elif choice == '3':
            keyword = input("Enter search keyword: ")
            results = library.search_books(keyword)
            for book in results:
                print(f"{book.title} by {book.author} ({book.year}) - ISBN: {book.isbn}")
        elif choice == '4':
            for book in library.list_books():
                print(f"{book.title} by {book.author} ({book.year}) - ISBN: {book.isbn}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

