"""
This file contains the argument parser with all arguments
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    'directory',
    help='directory of the replacement, e.g. "/home/user/rdir/"',
)

parser.add_argument(
    'search_for',
    help='file search string, e.g. "replace_this_string"'
)

parser.add_argument(
    'replace_with',
    help='file replacement string, e.g. "with_that_string"'
)

parser.add_argument(
    '-f',
    '--files-filter',
    metavar='filter',
    help='file or list of files in which to search, e.g. ".txt" or ".xml,.csv"'
)

parser.add_argument(
    '-n',
    '--number-of-replacements',
    metavar='num',
    default=0,
    type=int,
    help='limit the number of replacements per file. use negative numbers to replace backwards'
)

parser.add_argument(
    '-r',
    '--recursive',
    action='store_true',
    help='replace string recursivly also in subdirectories'
)

parser.add_argument(
    '-v',
    '--verbose',
    default=0,
    action='count',
    help='print more details. use -vv for maximum verbosity'
)

parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s 1.0'
)
