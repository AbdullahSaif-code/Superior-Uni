class Book:
    def __init__(self, title, author, available, genre):
        self.title = title
        self.author = author
        self.available = available
        self.genre = genre

    def borrow(self):
        if self.available:
            self.available = False
            print(f'Borrowing {self.title}')
        else:
            print(f'{self.title} unavailable.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'Returning {self.title}')
        else:
            print(f'{self.title} Borrowed.')

    def display_status(self):
        if self.available:
            status = "Available"
        else:
            status = "Not Available"
        print(f'Book Title: "{self.title}"\nAuthor: "{self.author}"\nAvailable: {status}\nGenre: {self.genre}')

class e_Book(Book):
    def __init__(self, title, author, available, genre, file_size):
        super().__init__(title, author, available, genre)
        self.file_size = file_size

    def display_status(self):        
        super().display_status()
        print(f'File Size: {self.file_size} MB')

class Audio_book(Book):
    def __init__(self, title, author, available, genre, duration):
        super().__init__(title, author, available, genre)
        self.duration = duration

    def display_status(self):     
        super().display_status()
        print(f'Duration: {self.duration} hours')



book1 = Book("Die Twice", "Simon Kernick", True, "Fiction")
ebook1 = e_Book("Python for Data Science", "Jake VanderPlas", True, "Educational", 3.5)
audiobook1 = Audio_book("The Pragmatic Programmer", "Andy Hunt", True, "Technology", 15)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
book1.display_status()
print()
ebook1.display_status()
print()
audiobook1.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
book1.borrow()
book1.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ebook1.borrow()
ebook1.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
audiobook1.return_book()
audiobook1.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
audiobook1.borrow()
audiobook1.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
audiobook1.return_book()
audiobook1.display_status()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")