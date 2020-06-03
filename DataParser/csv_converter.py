#!/usr/bin/python3
import re
import json
import main


in_filename = 'my_log.log'
ls_filename = 'my_line_structure.json'
out_filename = "output.csv"

with open(in_filename, 'r') as in_file:
    file_top = in_file.tell()
    with open(ls_filename, 'r') as struct_file:
        data=struct_file.read()
    structure = json.loads(data)
    first_line = in_file.readline()
    separator = structure["separator"]
    my_re = main.make_regex(structure, separator)
    match = re.match(my_re, first_line)
    if not match:
        print("Struct incopatible with file")
        exit()
    headers = list(structure.keys())
    headers.remove('separator')

    in_file.seek(file_top)
    with open(out_filename, 'a') as out_file:
        head_str = ",".join(headers)
        out_file.write(head_str + '\n')
        for line in in_file:
            out_file.write(line.replace(separator, ','))
