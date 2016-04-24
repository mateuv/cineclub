#!/usr/bin/env python3
import csv
import re
import json

"""
Given pelis.csv this script computes pelis.json
"""

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
			'fqn'           : fqn,
		})

		json.dump(result, open('pelis.json', 'w'), indent=2)
