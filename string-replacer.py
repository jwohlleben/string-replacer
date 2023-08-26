#!/usr/bin/python3

"""
string-replacer replaces strings in multiple files
"""

import time
import sys
import os

# Ensure, that all modules can be found
sys.path.insert(0, os.path.dirname(__file__))

import modules.mylog as log
from modules.myargparser import parser

def replace_normal(content, args):
    '''Replace search_for with replace_with in content using normal replacement'''
    if args.number_of_replacements == 0:
        return content.replace(args.search_for, args.replace_with)
    elif args.number_of_replacements > 0:
        return content.replace(args.search_for, args.replace_with, args.number_of_replacements)
    else:
        return args.replace_with.join(content.rsplit(args.search_for, abs(args.number_of_replacements)))

def in_filter_normal(element, filter):
    '''Return True, if element matches filter'''
    for f in filter:
        if f in element:
            return True
        
    return False

def run(start_directory, args, replace, in_filter):
    '''Run the replacement and return the number of modified files'''
    modified_count = 0
    for file in os.listdir(start_directory):
        filepath = os.path.join(start_directory, file)

        if os.path.isdir(filepath):
            if args.recursive:
                log.vv(f'Entering directory "{file}"')
                modified_count += run(filepath, args, replace, in_filter)
                log.vv(f'Leaving directory "{file}"')
            continue

        if not in_filter(file, args.files_filter):
            log.vv(f'Skipping "{filepath}"')
            continue

        file_content = ''
        with open(filepath, 'r') as f:
            file_content = f.read()

        replacement = replace(file_content, args)
        
        if (file_content != replacement):
            with open(filepath, 'w') as f:
                f.write(replacement)
                modified_count += 1
                log.v(f'Modified file "{filepath}"')
    
    return modified_count

if __name__ == '__main__':
    args = parser.parse_args()
    log.verbosity = args.verbose
    log.vv(f'Parsed args: {args}')

    if not os.path.isdir(args.directory):
        log.error(f'Could not find given directory "{args.directory}"')
        sys.exit(1)

    modified_count = 0
    start_time = time.time()

    if args.files_filter == None:
        log.vv('No filter found')
        modified_count = run(args.directory, args, replace_normal, lambda e, f: True)
    elif ',' in args.files_filter:
        f = list(args.files_filter.split(','))
        args.files_filter = f
        log.vv(f'Found multiple filters: {args.files_filter}')
        modified_count = run(args.directory, args, replace_normal, in_filter_normal)
    else:
        args.files_filter = [args.files_filter]
        log.vv(f'Found single filter: {args.files_filter}')
        modified_count = run(args.directory, args, replace_normal, in_filter_normal)

    stop_time = time.time()
    time_diff = int(round(stop_time - start_time, 0))

    log.v(f'Modified {modified_count} files in {int(time_diff / 60)}m {time_diff % 60}s')
