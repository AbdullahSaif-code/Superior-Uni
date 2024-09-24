class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.year}"
book = Book("A GOOD DAY TO DIE", "Jim Harrison", 1973)
print(book)
