import book_data
import error_handling

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    genre = input("Enter book genre: ")
    price = input("Enter book price: ")
    quantity = input("Enter book quantity: ")

    if error_handling.validate_book_details(title, author, isbn, genre, price, quantity):
        book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "genre": genre,
            "price": float(price),
            "quantity": int(quantity)
        }
        if book_data.add_book(book):
            print("Book added successfully!")
        else:
            print("Book with this ISBN already exists.")
    else:
        print("Invalid book details. Please try again.")
