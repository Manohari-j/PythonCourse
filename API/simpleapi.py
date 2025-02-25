class Bookstore:
    def __init__(self):
        self.books=[]

    def add_book(self,id,title,author,year,genre):
        new_book = {
            "id": id,
            "title": title,
            "author": author,
            "year": year,
            "genre": genre
        }
        self.books.append(new_book)
        return new_book

    def get_book_by_id(self,id):
        for book in self.books:
            if book['id'] == id:
                return book
        return None

if __name__ == "__main__":
    bs = Bookstore()

    b1 = bs.add_book(1,"Harry Potter", "J.K.Rowling", 1990, "Fantasy")
    b2 = bs.add_book(2, "Ponniyin Selvan", "Kalki", 1980, "Fantasy")

    print(bs.get_book_by_id(1)["title"])
    print(b2)