class Book():

    def __init__(self, bookName, writer, pages):
        print("Book object is created...")
        self.bookName = bookName
        self.writer = writer
        self.pages = pages

# __str__
    def __str__(self):
         return "Book Name: {} \nWriter: {} \nPages: {}\n".format(self.bookName,
                                                              self.writer,
                                                              self.pages)

# __len__
    def __len__(self):
        return self.pages

# __del__
    def __del__(self):
        print("Book object is deleted....")

book1 = Book("Learning Java", "Bob Larry", 500)
#print(book1)
#print(len(book1))
del book1

print(book1)




