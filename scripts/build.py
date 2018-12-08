#!/usr/local/bin/python3


import csv
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))
docs_path = dir_path + '/../docs'

def reformat(file):

    output = []

    with open(file) as csvfile:
        csv_obj = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(csv_obj):
            if index == 0:
                header = map(lambda x: ' ' + x + ' ', row)
                header_text = '|' + '|'.join(header) + '|'
                alignment = map(lambda x: ' --- ', row)
                alignment_text = '|' + '|'.join(alignment) + '|'
                output.append(header_text)
                output.append(alignment_text)
            else:
                record = map(lambda x: ' ' + x + ' ', row)
                record_text = '|' + '|'.join(record) + '|'
                output.append(record_text)

    return '\n'.join(output)


def write_md(file, input):

    with open(file, 'w+') as mdfile:
        mdfile.write(input)
        mdfile.close()

    with open(file) as mdfile:
        print(mdfile.read())
        mdfile.close()


# Metro Lines
output = reformat(dir_path + '/../data/metro-lines.csv')

header = """# Metro Lines Data File


    This file contains the data we've collected for all the metro lines


"""
write_md(docs_path + '/metro-lines.md', header + output)



# Home
home_md_output = """# Welcome to www.metropedia.org


[Metro Lines](/metro-lines.html)
"""
write_md(docs_path + '/index.md', home_md_output)
