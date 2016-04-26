#!/usr/bin/env python3
import csv
import re
import json
import os
import unicodedata

"""
Given pelis.csv this script computes pelis.json
"""

def varify(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

if __name__ == '__main__':
    reader = csv.reader(open('pelis.csv'))

    result = []

    for row in reader:
        match = re.match('([0-9]{2})/([0-9]{2})/([0-9]{4})', row[-1])
        if match:
            date = '%s-%s-%s'%(match.group(3), match.group(2), match.group(1))
        else:
            date = row[-1]

        fqn = "%s (%s) %s %s [%s]"%(row[0], row[1], row[2], row[3], row[4])

        result.append({
            'title'         : row[0],
            'original_title': row[1],
            'director'      : row[2],
            'year'          : row[3],
            'country'       : row[4],
            'date'          : date,
            'fqn'           : varify(fqn),
        })

        json_data = json.dumps(result, indent=2)

        # add padding (jsonp)
        with open('pelis.jsonp', 'w') as jsonp:
            jsonp.write('loadMovieData(')
            jsonp.write(json_data)
            jsonp.write(');')

        dir_name = "%s_%s"%(date, row[0])

        if not os.path.isdir('proyecciones/%s'%dir_name):
            os.mkdir('proyecciones/%s'%dir_name)
