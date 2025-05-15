# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.

class Book:
    def __init__(self, numpages, year, title):
        self.numpages = numpages
        self.year = year
        self.title = title


class Novel(Book):
    def __init__(self, genre):
        super().__init__(self, self.numpages, self.title, self.year)
        self.genre = genre

class Magazine(Book):
    def __init__(self):
        super().__init__(self, self.numpages, self.title, self.year)






