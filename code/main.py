import os
import sys
from os import listdir
from lib.io import Log, log
from collections import OrderedDict
from operator import itemgetter

# Stores id and the value
g_books = {}
g_libraries = OrderedDict()
g_books_scheduled = []


class Library:

    def __init__(self, id, setup, book_rate, books):
        self.id = int(id)
        self.setup = int(setup)
        self.book_rate = int(book_rate)
        self.books = books

    @property
    def efficiency(self):
        if len(self.books) > 0:
            sum_score = 0
            for book in self.books:
                sum_score += book.score
            return ((sum_score / len(self.books)) * self.book_rate) / ((len(self.books) / self.book_rate) + self.setup)

        else:
            return 0

    def print(self):
        log("id " + str(self.id))
        log("setup " + str(self.setup))
        log("book rate " + str(self.book_rate))
        log("efficiency " + str(self.efficiency))

        for book in self.books:
            book.print()

class Book:
    def __init__(self, id, score):
        self.id = int(id)
        self.score = int(score)

    def print(self):
        log("- id " + str(self.id))
        log("- score " + str(self.score))


def absf(d, f):
    return os.path.join(d, f)


def process_all(worker_func, in_path='in', out_path='out'):
    files = listdir(in_path)

    for file in files:
        log(absf(in_path, file))

    for ifile in files:
        ofile = ifile.replace('.in.txt', '.out.txt')
        open(absf(out_path, ofile), 'w').write(worker_func(absf(in_path, ifile)))
        log(absf(out_path, ofile))


def process(file):
    global g_books, g_libraries, g_books_scheduled

    lines = open(file, 'r').read().split('\n')

    number_of_books, number_of_libraries, number_of_days = lines[0].split(" ")

    g_books_scheduled = [False] * int(number_of_books)

    for i, book_value in enumerate(lines[1].split(" ")):
        g_books[i] = int(book_value)

    libs = []
    lib_index = 0
    for i in range(2, len(lines) - 1, 2):
        try:
            num_books_in_lib, setup, book_rate = lines[i].split(" ")

            books = []
            for book_id in lines[i+1].split(" "):
                books.append(Book(book_id, g_books[int(book_id)]))
            lib = Library(lib_index, setup, book_rate, books)
            lib.efficiency
            libs.append(lib)

            lib_index += 1

            #lib.print()
        except Exception:
            print(lines[i])

    libs = sorted(libs, key=lambda x: x.efficiency)

    result = str(len(libs)) + "\n"
    while len(libs) > 0:
        # TODO remove scheduled books

        most_efficient = libs.pop()

        book_ids = ""
        for book in most_efficient.books:
            book_ids += str(book.id) + " "

        result += str(most_efficient.id) + " " + str(len(most_efficient.books)) + "\n" + book_ids + "\n"

    return result


if __name__ == '__main__':
    CODE_DIR = os.path.dirname(os.path.realpath(__file__))
    BASE_DIR = CODE_DIR + '/../'
    sys.path.append(CODE_DIR)

    Log.debug = True

    log("\n")
    log("\n")

    f = sys.argv[1]

    open("../out/" + f +".txt", "w+").write(process("../in/" + f + ".txt"))
