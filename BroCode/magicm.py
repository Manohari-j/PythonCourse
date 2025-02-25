class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa


s1 = Student("Jai", 4.0)
s2 = Student("Subhi", 4.6)
s3 = Student("Madhav", 4.5)

print(s1)
print(s1 == s2)
print(s1 > s2)


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # string representation of an object
    def __str__(self):  # return this instead of obj addr
        return f"'{self.title}' by {self.author}"


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages+other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "num_pages":
            return self.num_pages
        else:
            return f"Key '{item}' was not found"

b1 = Book("Ponniyin Selvan", "Kalki", 600)
b2 = Book("Harry Potter", "J.K.Rowling", 223)
b3 = Book("Wings Of Fire", "T.Sutherland", 300)
b4 = Book("Ponniyin Selvan", "Kalki", 600)
print(b1)
print(b1==b4) # if not customized it gives false
print(b2<b1)
print(b3>b2)

print(b1+b2)

print("Fire" in b3)

print(b1["title"])
print(b2["auth"])
