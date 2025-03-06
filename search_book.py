import book_data

def search_book():
    search_key = input("Enter title, author, or ISBN to search: ")
    matching_books = book_data.search_book(search_key)
    if matching_books:
        print("Books found:")
        for book in matching_books:            
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Genre: {book['genre']}, Price: {book['price']}, Quantity: {book['quantity']}")
    else:
        print("No book found with the given search key.")