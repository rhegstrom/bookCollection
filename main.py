# -*- coding: utf-8 -*-
"""
Roger Hegstrom(rhegstrom@avc.edu)

Set up a Class Object that keeps track of you books:
    book title,
    book author,
    book length
    genre (can be added)
    how books in each genre
    book set 
"""

class Book:
    def __init__(self, **kwargs):
        self.title  = 'None'
        self.author = 'None'
        self.length = 0
        self.genre  = 'None'
        self.set    = 'None'
        
        for arg in kwargs:
            if arg == 'title':
                self.title = kwargs['title']
            elif arg == 'author':
                self.author = kwargs['author']
            elif arg == 'length':
                self.length = kwargs['length']
            elif arg == 'genre':
                self.genre = kwargs['genre']
            elif arg == 'set':
                self.set = kwargs['set']
    
    def setTitle(self, title):
        self.title = title
        
    def getTitle(self):
        return self.title
    
    def setAuthor(self, author):
        self.author = author
    
    def getAuthor(self):
        return self.author
    
    def setLength(self, length):
        self.length = length
        
    def setGenre(self, genre):
        self.genre = genre
        
    def getGenre(self, genre):
        return self.genre
    
    def setSet(self, s):
        self.set = s
        
    def getSet(self):
        return self.set
    
    def __str__(self):
        return f"Title={self.title}, Author={self.author}, Pages={self.length}, " \
            f"Genre={self.genre}, Bookset={self.set}"


class Books:
    def __init__(self):
        self.books = []
    
    def addBook(self, **kwargs):
        b = Book(**kwargs)
        self.books.append(b)
        
    def printBooks(self):
        for book in self.books:
            print(book)
            
    def getBookByTitle(self, title):
        return [ book for book in self.books if book.title == title ]

    def getBookByGenre(self, genre):
        return [ book for book in self.books if book.genre == genre ]    



if __name__ == '__main__':   
    books = Books()   # Initialize books catalog object
    
    books.addBook(title = 'Goosebumps - Welcome to dead house', author = 'RL Stein', length = 30, genre = 'Horror')
    books.addBook(title = 'Goosebumps - One day in horror land', author = 'RL Stein', length = 45, genre = 'Horror')
    books.addBook(title = 'Goosebumps - Night of the living dummy', author = 'RL Stein', length = 60, genre = 'Horror')
    books.addBook(title = 'Goosebumps - Welcome to camp nightmare', author = 'RL Stein', length = 49, genre = 'Horror')
    
    books.addBook(title = 'Harry Potter and the Order of the Phoenix', author = 'JK Rowling', length = 100, genre = 'Kids')
    books.addBook(title = 'Harry Potter and the Sorcerers Stone', author = 'JK Rowling', length = 104, genre = 'Kids')
    books.addBook(title = 'Harry Potter and the Goblet of Fire', author = 'JK Rowling', length = 120, genre = 'Kids')
    
    print('Printing out books in collection:')
    print('-----------------------------------------------------------------------------------------')
    books.printBooks()
    
    print("\n\nListing books in the Horror genre:")
    print('-----------------------------------------------------------------------------------------')
    
    for book in books.getBookByGenre('Horror'):
        print(book)
