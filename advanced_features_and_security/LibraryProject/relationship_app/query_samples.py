# relationship_app/query_samples.py
from .models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """Query all books by a specific author using filter."""
    try:
        author = Author.objects.get(name=author_name)
        # REQUIRED LINE: objects.filter(author=author)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")


def list_books_in_library(library_name):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in '{library_name}':")
        for book in library.books.all():
            print(f"  - {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"\nLibrarian for '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")


# Run sample queries
if __name__ == "__main__":
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")