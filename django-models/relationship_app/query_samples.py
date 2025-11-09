from django.db.models import Q
from .models import Author, Book, Library, Librarian

def run_queries():
    print("=== Query Samples ===\n")

    # 1. Query all books by a specific author
    print("1. All books by 'J.K. Rowling':")
    try:
        author = Author.objects.get(name="J.K. Rowling")
        books = author.books.all()
        for book in books:
            print(f"   - {book.title}")
    except Author.DoesNotExist:
        print("   Author 'J.K. Rowling' not found.")
    print()

    # 2. List all books in a library
    print("2. All books in 'Central Library':")
    try:
        library = Library.objects.get(name="Central Library")
        books_in_library = library.books.all()
        for book in books_in_library:
            print(f"   - {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print("   Library 'Central Library' not found.")
    print()

    # 3. Retrieve the librarian for a library
    print("3. Librarian for 'Downtown Library':")
    try:
        library = Library.objects.get(name="Downtown Library")
        librarian = library.librarian
        print(f"   Librarian: {librarian.name}")
    except Library.DoesNotExist:
        print("   Library 'Downtown Library' not found.")
    except Librarian.DoesNotExist:
        print("   No librarian assigned to this library.")
    print()

if __name__ == "__main__":
    run_queries()