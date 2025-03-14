from simpleapi import Bookstore

class LibraryManager:
    def __init__(self, bookstore):
        self.bookstore = bookstore


    def add_book_to_store(self,id,title,author,year,genre):
        new_book = self.bookstore.add_book(id,title,author,year,genre)
        return new_book


if __name__ == "__main__":
    bs = Bookstore()
    manager = LibraryManager(bs)

    manager.add_book_to_store(3,"Nancy Drew", "J.K.F", 1990, "Fantasy")

    print(bs.get_book_by_id(3))