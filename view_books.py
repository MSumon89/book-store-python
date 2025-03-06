import book_data

def view_books():
    books = book_data.get_books()
    if books:
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Genre: {book['genre']}, Price: {book['price']}, Quantity: {book['quantity']}")
    else:
        print("No books available.")
