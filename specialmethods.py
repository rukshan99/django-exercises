class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.stars = 0

    def give_stars(self, rating):
        self.stars = rating

    def get_stars(self):
        return self.stars

    def __str__(self):
        return f"{self.title}, written by {self.author}"

    def __len__(self):
        return self.pages

book = Book("Django Book", "Rukshan Jayasekara", 256)

print(book.get_stars())
book.give_stars(5)
print(book.get_stars())
print(book)
print(len(book))

#python specialmethods.py