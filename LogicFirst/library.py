class Library:
    def __init__(self, b_list):
        self.books_list = b_list
        self.available_books_list = b_list[:] # to have a separate copy
        self.books_lent = {}  # key: book value: username

    def display_available_books(self):
        for b in self.available_books_list:
            print(b)

    def display_all_books(self):
        for b in self.books_list:
            print(b)

    def borrow_a_book(self, name, book):
        if book not in self.books_list:
            print("Incorrect book name. Please check book list")
            return
        elif book in self.available_books_list:
            self.books_lent.update({book: name})
            self.available_books_list.remove(book)
            print("You can take the book")
        else:
            print(book + " currently not available, taken by " + self.books_lent[book])
            return

    def return_a_book(self, book):
        del self.books_lent[book]
        self.available_books_list.append(book)


# if run directly from this file/module then execute this

if __name__ == "__main__":
    lib = Library(["The Life Divine", "Da Vinci Code", "Harry Potter", "Wings Of Fire", "Nancy Drew"])
    print("Welcome to Library. Enter an option. ")
    while True:
        print("1.Display available books")
        print("2.Display all books")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.Quit")

        choice = int(input())

        if choice == 1:
            lib.display_available_books()
        elif choice == 2:
            lib.display_all_books()
        elif choice == 3:
            name = input("Enter User Name: ")
            book = input("Enter Book Name: ")
            lib.borrow_a_book(name, book)
        elif choice == 4:
            book = input("Enter Book Name: ")
            lib.return_a_book(book)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
