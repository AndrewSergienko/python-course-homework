import Reader
import Book


class Library:
    def __init__(self):
        self.readers = []
        self.books = []
        self.taken_books = []

    def add_reader(self, reader: Reader):
        self.readers.append(reader)

    def remove_reader(self, reader: Reader):
        if reader in self.readers:
            self.readers.remove(reader)
        else:
            print("Такого читача немає в списку.")

    def give_book(self, book: Book, reader: Reader):
        if reader in self.readers and book in self.books:
            if book.minimum_age < reader.age:
                self.taken_books.append([book, reader])
                self.books.remove(book)
            else:
                print("Читач не відповідає віковому обмеженню книги.")
        else:
            print("Такого читача немає в списку або книги немає в наявності.")

    def return_book(self, book, reader):
        if [book, reader] in self.taken_books:
            self.books.append(book)
            self.taken_books.remove([book, reader])
        else:
            print("Такого читача немає в списку або він не брав таку книгу.")

    def return_all_books(self, reader):
        for taken_book in self.taken_books:
            if reader in taken_book:
                self.books.append(taken_book)
                self.taken_books.remove([taken_book, reader])
