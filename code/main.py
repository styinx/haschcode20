import os
import sys
from os import listdir
from lib.io import Log, log


def absf(d, f):
    return os.path.join(d, f)


def process_all(worker_func, in_path='in', out_path='out'):
    files = listdir(in_path)

    for file in files:
        log(absf(in_path, file))

    for ifile in files:
        ofile = ifile.replace('.in', '.out')
        open(absf(out_path, ofile), 'w').write(worker_func(absf(in_path, ifile)))
        log(absf(out_path, ofile))


def process(file):
    lines = open(file, 'r').read().split('\n')

    for line in lines:
        pass  # smart algorithm

    return ""


if __name__ == '__main__':
    CODE_DIR = os.path.dirname(os.path.realpath(__file__))
    BASE_DIR = CODE_DIR + '/../'
    sys.path.append(CODE_DIR)

    Log.debug = True

    process_all(process, BASE_DIR + 'in', BASE_DIR + 'out')
