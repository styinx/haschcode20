import os
import sys
from os import listdir
from lib.io import Log, log

# Stores id and the value
g_books = {}


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
    lines = open(file, 'r').read().split('\n')

    number_of_books, number_of_libraries, number_of_days = lines[0].split(" ")
    for i, book_value in enumerate(lines[1].split(" ")):
        g_books[i] = book_value

    log("num of books " + number_of_books)
    log("num of libs " + number_of_libraries)
    log("num of days " + number_of_days)
    log("\n")

    for i in range(2, len(lines), 2):
        num_books_in_lib, books_per_day, book_rate = lines[i].split(" ")
        books_in_library = lines[i+1].split(" ")

        log("Library " + str(i - 2))
        log("- number of books  " + num_books_in_lib)
        log("- books per day " + books_per_day)
        log("- book rate " + book_rate)
        log("- books in library " + str(books_in_library))


        # TODO alg

    return ""


if __name__ == '__main__':
    CODE_DIR = os.path.dirname(os.path.realpath(__file__))
    BASE_DIR = CODE_DIR + '/../'
    sys.path.append(CODE_DIR)

    Log.debug = True

    process("../in/a_example.txt")
    # process_all(process, BASE_DIR + 'in', BASE_DIR + 'out')
