class Book:
    def __init__(self, numpages, year, title):
        self.numpages = numpages
        self.year = year
        self.title = title

    def rate(self):
        self.Book += 1

    def displayDetails(self):
      print(f"Book: {self.title}\nAuthor: {self.author}") #original Function
    

class Novel(Book):
    def __init__(self, genre):
        super().__init__(self, self.numpages, self.title, self.year)
        self.genre = genre

    def displayDetails(self): 
        print(f"{self.title} by {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Chapters: {self.numChapters}") #Polymorphism function



class Magazine(Book):
    def __init__(self):
        super().__init__(self, self.numpages, self.title, self.year)


mag1 = Magazine(12,"Daniel", 445)
nov1 = Novel(1000000000, "John the book", 2026)

