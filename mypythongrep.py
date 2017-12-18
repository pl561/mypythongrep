#! /usr/bin/env python
# -*-coding:utf-8 -*

__author__ = "pl561"
__copyright__ = ""
__credits__ = [__author__]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = __author__
__email__ = ""
__status__ = ""

import sys
import os
import glob
from termcolor import colored

def search_fromfilename(fname, keywords):
    lines = get_lines(fname)
    find_keywords(lines, fname, keywords, linerange=3)
    

def get_lines(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    return lines

def find_keywords(lines, fname, keywords, linerange=1):
    number_of_lines = len(lines)
    for lineno, line in enumerate(lines):
        for keyword in keywords:
            if keyword in line:
                sys.stdout.write(colored('FILENAME: {}'.format(fname), 'white'))
                for ln in xrange(lineno-linerange, lineno+linerange+1):
                    if 0 <= ln < number_of_lines:
                        current_line = lines[ln]
                        inrange_line = current_line[:-1]
                        if ln == lineno:
                            indicator = '>'
                            colored_line = colored(inrange_line, 'red')
                        else:
                            indicator = ' '
                            colored_line = colored(inrange_line, 'yellow')
                        line_indication = str(ln+1).zfill(len(str(number_of_lines)))
                        s = '{}{}: {}'.format(indicator*2, line_indication, colored_line)
                        sys.stdout.write(s)
                sys.stdout.write('\n\n'),

def get_filenames(directory='.', extension='*.py'):
    if directory == '.':
        path = os.getcwd()
        globbed = glob.glob(extension)
    else:
        globbed = glob.glob(os.path.join(directory, extension))

    return sorted(globbed)

def mygrep():
    # default behavior is ti search in current directory *.py files
    kwds = sys.argv[1:]
    sys.stdout.write('Searching in .py files the following keywords:\n{}'.format(kwds))
    filenames = get_filenames()
    for fname in filenames:
        search_fromfilename(fname, kwds)


def main():
    mygrep()



if __name__ == '__main__':
    sys.exit(main())
    
