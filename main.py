import add_book
import view_books
import remove_book
import book_data
import search_book

def main_menu():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book.add_book()
        elif choice == '2':
            view_books.view_books()
        elif choice == '3':
            search_book.search_book()
        elif choice == '4':
            remove_book.remove_book()
        elif choice == '5':
            book_data.save_books()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    book_data.load_books()
    main_menu()
