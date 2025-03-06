import json

BOOKS_FILE = "books.json"
books = []

def load_books():
    global books
    try:
        with open(BOOKS_FILE, 'r') as file:
            books = json.load(file)
    except FileNotFoundError:
        print("No existing book data found. Starting fresh.")

def save_books():
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file)

def add_book(book):
    for b in books:
        if b['isbn'] == book['isbn']:
            return False
    books.append(book)
    save_books()
    return True

def get_books():
    return books

def search_book(search_key):
    search_words = search_key.lower().split()
    matching_books = []
    for book in books:
        if search_key == book['isbn']:
            matching_books.append(book)
        title_words = book['title'].lower().split()
        author_words = book['author'].lower().split()
        if any(word in title_words for word in search_words) or any(word in author_words for word in search_words):
            matching_books.append(book)
    return matching_books

def remove_book(isbn):
    global books
    for book in books:
        if book['isbn'] == isbn:
            books.remove(book)
            save_books()
            return True
    return False
