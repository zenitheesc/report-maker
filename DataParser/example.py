#!/usr/bin/python3
from dataparser import DataParser
import statistics

structure = {
    "my_date": "date",
    "my_int": "integer",
    "my_float": "float",
    "my_str": "str",
    "separator": ";"
}

parser = DataParser(structure)


## LINE PARSING
line = "1-12-2021;123;-123.456;xa"
x = parser.parse_line(line)
print("Single Line:\n" + str(x))

## FILE PARSING
all_data = parser.parse_file('my_log.log')
print("\nFull File: \n" + str(all_data))

##GENERATE STATISTICS
g =statistics.generate_data_x_data(all_data['my_int'], all_data['my_float'], "my_int", "my_float")
print(g)
