import book_data

def remove_book():
    isbn = input("Enter the ISBN of the book to remove: ")
    if book_data.remove_book(isbn):
        print("Book removed successfully!")
    else:
        print("Book not found.")
