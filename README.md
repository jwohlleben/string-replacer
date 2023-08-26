# string-replacer
A simple python script for replacing strings in multiple files

## Prerequisites
In order to use string-replacer, please install python3

## Usage
```
usage: string-replacer.py [-h] [-f filter] [-n num] [-r] [-v] [--version] directory search_for replace_with

positional arguments:
  directory             directory of the replacement, e.g. "/home/user/rdir/"
  search_for            file search string, e.g. "replace_this_string"
  replace_with          file replacement string, e.g. "with_that_string"

options:
  -h, --help            show this help message and exit
  -f filter, --files-filter filter
                        file or list of files in which to search, e.g. ".txt" or ".xml,.csv"
  -n num, --number-of-replacements num
                        limit the number of replacements per file. use negative numbers to replace backwards
  -r, --recursive       replace string recursivly also in subdirectories
  -v, --verbose         print more details. use -vv for maximum verbosity
  --version             show program's version number and exit
```

## Examples
Replace the word "Shinx" with "Luxio" in all files in the directory "/home/user/pokemon/":<br>
`./string-replacer.py "/home/user/pokemon/" "Shinx" "Luxio"`

Replace the word "Chimchar" with "Monferno" in all files and all (sub)directories in "/home/user/pokemon/":<br>
`./string-replacer.py -r "/home/user/pokemon/" "Chimchar" "Monferno"`

Replace the word "Feebas" with "Milotic" in all files, that include ".dex" or ".pkm" in the directory "/home/user/pokemon/":<br>
`./string-replacer.py -f ".dex,.pkm" "/home/user/pokemon/" "Feebas" "Milotic"`

Replace the word "Gible" with "Gabite" no more than three times backwards in all files in the directory "/home/user/pokemon/":<br>
`./string-replacer.py -n -3 "/home/user/pokemon/" "Gible" "Gabite"`
