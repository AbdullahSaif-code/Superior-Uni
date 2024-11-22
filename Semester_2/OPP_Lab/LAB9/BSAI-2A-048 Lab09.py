import csv
import os
# Main parent class
class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")
# Book child class for hard form book        
class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}\nPages: {self.pages}")
# Article child for soft form book
class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        super().display_info()
        print(f"Journal: {self.journal}\nDOI: {self.doi}")


# Save data to a CSV file
def save_to_file(filename, data, headers):
    with open(filename, 'a', newline='') as file:  # Use 'a' for appending
        writer = csv.writer(file)
        if os.stat(filename).st_size == 0:  # Add headers only if the file is empty
            writer.writerow(headers)
        writer.writerow(data)
    print(f"Data saved to {filename}")

# Read data from a CSV file
def read_from_file(filename):
    filepath = os.path.abspath(filename)
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [row for row in reader if row]
        return headers, data

# Menu for 
def menu():
    while True:
        print(f"\nChoose from the Following:")
        print("1 for Book")
        print("2 for Article")
        print("3 to View Books")
        print("4 to View Articles")
        print("5 to Exit")
        user_input = input("Waiting for input: ")
        
        if user_input == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            genre = input("Enter the book genre: ")
            pages = input("Enter the number of pages: ")
            book = [title, author, genre or None, pages or None]
            save_to_file("books.csv", book, ["Title", "Author", "Genre", "Pages"])
        
        elif user_input == "2":
            title = input("Enter the article title: ")
            author = input("Enter the article author: ")
            journal = input("Enter the journal name: ")
            doi = input("Enter the DOI: ")
            article = [title, author, journal or None, doi or None]
            save_to_file("articles.csv", article, ["Title", "Author", "Journal", "DOI"])
        
        elif user_input == "3":
            csv_file_name = "books.csv"
            if os.path.exists(csv_file_name):
                print(f"Opening {csv_file_name}")
                os.startfile(csv_file_name)
            else:
                print("No CSV file found.")
        
        elif user_input == "4":
            csv_file_name = "articles.csv"
            if os.path.exists(csv_file_name):
                print(f"Opening {csv_file_name}")
                os.startfile(csv_file_name)
            else:
                print("No CSV file found.")
        
        elif user_input == "5":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Incorrect user input. Please try again.")

# Run the menu
menu()
