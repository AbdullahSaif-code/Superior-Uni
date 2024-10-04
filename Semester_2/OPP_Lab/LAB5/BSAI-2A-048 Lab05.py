class item:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")

class book(item):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    
    def additional_info(self):
        print(f"Pages: {self.pages}")

class magazine(item):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    
    def additional_info(self):
        print(f"Issue-Number: {self.issue_number}")

book = book("A GOOD DAY TO DIE", "Jim Harrison", "Pg-1973")
magazine = magazine("A GOOD DAY TO DIE", "Jim Harrison", "Mg-1973")

print("Book info:")
print ("-------------")
book.display_info()
book.additional_info()
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Magazine info:")
print ("-------------")
magazine.display_info()
magazine.additional_info()