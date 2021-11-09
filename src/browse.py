# Module for browsing the book list
import json
from utils import cli_cleaner


class Booklist:
    def __init__(self):
        with open('./assets/books.json', 'r') as booklist:
            self.__books = json.load(booklist)
        self.collection_length = len(self.__books)
        self.__printPos = 0

        if self.collection_length <= 10:
            self.__lastPage = True
        else:
            self.__lastPage = False

    def __printPage(self):
        cli_cleaner()
        print('{:<6} {:<15} {:<10} {:<15} {:<15} {:<7}'.format('ID', 'Title', 'Author', 'Publisher',
                                                               'Publish Date', 'Booked'))

        if ( ( self.__printPos + 1 ) * 10 - 1) > self.collection_length:
            topIndex = self.collection_length - 1
        else:
            topIndex = (self.__printPos + 1) * 10 - 1
            self.__lastPage = True

        for i in range(self.__printPos*10, topIndex):
            Title, Author, Publisher, Publish_date, Booked = list(self.__books[i].keys())
            print('{:<6} {:<15} {:<10} {:<15} {:<15} {:<7}'.format(i, self.__books[i][Title], self.__books[i][Author],
                                                                   self.__books[i][Publisher],
                                                                   self.__books[i][Publish_date],
                                                                   self.__books[i][Booked]))

        if self.__printPos == 0 & self.__lastPage:
            print('(Q)uit')
        elif self.__printPos == 0:
            print('(N)ext\t(Q)uit')
        elif self.__lastPage:
            print('(P)revious\t(Q)uit')
        else:
            print('(P)revious\t(N)ext\t(Q)uit')

    def browse(self):
        self.__printPage()
        while True:
            action = input()
            if action not in ('P', 'N', 'Q') or ( action == 'P' and self.__printPos == 0) or \
                    ( action == 'N' and self.__lastPage):
                self.__printPage()
                print('Please input a valid option')
            elif action == 'P':
                self.__printPos -= 1
                self.__printPage()
            elif action == 'N':
                self.__printPos += 1
                self.__printPage()
            else:
                break
