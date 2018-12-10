#!/usr/local/bin/python3


import csv
import os 


www = 'https://www.metropedia.org'
ga = """

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-130550808-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-130550808-1');
</script>
"""
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


##############################################################################################
# Metro Lines
##############################################################################################

output = reformat(dir_path + '/../data/metro-lines.csv')

header = """# Metro Line Data File


    This file contains the data we've collected for all the metro lines


"""
write_md(docs_path + '/metro-lines.md', header + output + ga)

##############################################################################################
# Metro Stations
##############################################################################################

output = reformat(dir_path + '/../data/metro-stations.csv')

header = """# Metro Station Data File


    This file contains the data we've collected for all the metro stations


"""
write_md(docs_path + '/metro-stations.md', header + output + ga)

##############################################################################################
# Home
##############################################################################################

home_md_output = """# Welcome to www.metropedia.org


* [Metro Lines]({www}/metro-lines.html)
* [Metro Stations]({www}/metro-stations.html)
""".format(www=www)
write_md(docs_path + '/index.md', home_md_output + ga)
