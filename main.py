# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1400x1000")

Font = ("Roboto", 24)

frame = customtkinter.CTkFrame(master=root)

class Book:
    def __init__(self, numpages, year, title):
        self.numpages = numpages
        self.year = year
        self.title = title

    def rate(self):
        self.Book += 1

class Novel(Book):
    def __init__(self, genre):
        super().__init__(self, self.numpages, self.title, self.year)
        self.genre = genre

class Magazine(Book):
    def __init__(self):
        super().__init__(self, self.numpages, self.title, self.year)


mag1 = Magazine(12,"Daniel", 445)
nov1 = Novel(1000000000, "John the book", 2026)


compoundbutton = customtkinter.CTkButton(master=root, text="Submit", font=Font, width=50, height=20)
compoundbutton.pack(pady=16, padx=10)


frame.pack(fill="both", expand=True)

root.mainloop()