class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_publisher(self, publisher):
        self.publisher = publisher

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', publisher='{self.publisher}')"


if __name__ == "__main__":
    my_book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", publisher="Scribner")

    print(my_book)

    print("Title:", my_book.get_title())
    print("Author:", my_book.get_author())
    print("Publisher:", my_book.get_publisher())

    my_book.set_title("New Title")
    my_book.set_author("New Author")
    my_book.set_publisher("New Publisher")

    print(my_book)
    