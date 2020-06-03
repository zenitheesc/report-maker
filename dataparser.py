#!/usr/bin/python3
'''

    Support library used in the Report Maker on the data parsing stage
    
    Author: Leonardo Celente (@leocelente)
    Org: Zenith Aerospace

'''

import re

class DataParser:

    def __init__(self, structure):
        self._structure = structure
        self._regex_str = ""
        self.__make_regex()

    def parse_file(self, filename):
        with open(filename, 'r') as log_file:
            dict_of_lists = dict.fromkeys(self._structure.keys())
            for key in dict_of_lists.keys():
                dict_of_lists[key] = []
            for line in log_file:
                line_dict = self.parse_line(line)
                if not line_dict:
                    print("Failed to parse line\n\t-->"+line)
                    continue
                for field in line_dict.keys():
                    dict_of_lists[field].append(line_dict[field])
        del dict_of_lists['separator']
        return dict_of_lists

    def parse_line(self, line):
        if self._regex_str == "":
            return None

        match = re.match(self._regex_str, line)
        if match:
            return self.__cast(match.groupdict())
        
        else:
            return None

    def get_structure(self):
        return self._structure

    def get_regex(self):
        return self._regex_str

    def make_csv(self):
        pass

    def __make_regex(self):
        regex = ""
        for key in self._structure:
            if key == "separator":
                continue

            # uses Python Named Group RegEx Extension: ?P<group name>
            regex = regex + \
                (r"(?P<" + key + ">{" +
                    self._structure[key] +
                 "})") + \
                self._structure["separator"]

        self._regex_str = self.__regex_replace_data_types(regex)

    def __regex_replace_data_types(self, regex):
        date_re = r"[\d]{1,2}\-[\d]{1,2}\-[\d]{4}"      # DD-MM-YYYY format date
        integer_re = r"[\-]?[\d]+"                      # signed integer
        float_re = r"[\-]?[\d]+\.[\d]+"                  # signed float
        str_re = r"[\w]+"                               # string
        regex = regex.replace(r"{date}", date_re)
        regex = regex.replace(r"{integer}", integer_re)
        regex = regex.replace(r"{float}", float_re)
        regex = regex.replace(r"{str}", str_re)
        return regex[0:-1] + r'$'                       # replace last separator with EOL

    def __scast(self, var, to_type):
        if(self._structure[to_type] == "integer"):
            return int(var)
        elif(self._structure[to_type] == "float"):
            return float(var)
        else:
            return var

    def __cast(self, g_dict):
        new_dict = dict.copy(g_dict)
        for field in g_dict.keys():
            new_dict[field] = self.__scast(g_dict[field], field)
        return new_dict
                        
                
