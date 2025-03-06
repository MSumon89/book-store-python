def validate_book_details(title, author, isbn, genre, price, quantity):
    if not isinstance(title, str) or not title:
        print("The book title must be a non-empty string.")
        return False
    if not isinstance(author, str) or not author:
        print("The book author must be a non-empty string.")
        return False
    if not isinstance(isbn, str) or not isbn:
        print("The book ISBN must be a non-empty string.")
        return False
    if not isinstance(genre, str) or not genre:
        print("The book genre must be a non-empty string.")
        return False
    try:
        price = float(price)
        if price <= 0:
            print("The price must be a positive number.")
            return False
    except ValueError:
        print("The price must be a number.")
        return False
    try:
        quantity = int(quantity)
        if quantity < 0:
            print("The quantity must be a non-negative integer.")
            return False
    except ValueError:
        print("The quantity must be an integer.")
        return False
    return True
