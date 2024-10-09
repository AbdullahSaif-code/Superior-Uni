class Book:
    def __init__(self, title, author,available):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available == False
            print(f'Borrowing "{self.title}"')
        else:
            print(f'{self.title} unavailable.')

    def return_book(self):
        if not self.available:
            self.available == True
            print(f'Returning {self.title}')
        else:
            print(f'{self.title} not borrowed.')

    def display_status(self):
        if self.available == True:
            print("Available")
        else:
            print("Not Available")
        print(f'Book Title: "{self.title}"\nAuthor: "{self.author}"\nIs Available: {self.available}')

book1 = Book("A good day to die", "Jim Harrison" , True)
book2 = Book("To Kill a Mockingbird", "Harper Lee" , False)
book3 = Book("Die Twice", "Simon Kernick" , True)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
book1.display_status()
print()
book2.display_status()
print()
book3.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
book1.borrow()
book1.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
book1.return_book()
book1.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
book2.borrow()
book2.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
book3.borrow()
book3.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")