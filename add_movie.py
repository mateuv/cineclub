#!/usr/bin/env python3
import json
import csv
import os

if __name__ == '__main__':
	attributes = [
		'title',
		'original_title',
		'director',
		'year',
		'country',
		'date',
	]
	item = {}
	for attr in attributes:
		item[attr] = input('%s: '%attr)
	item['fqn'] = ("%s (%s) %s %s [%s]"%(item['title'], item['original_title'], item['director'], item['year'], item['country'])).lower()

	with open('pelis.jsonp') as json_file:
		data = json.loads(json_file.read()[14:-2])

	data.insert(0, item)

	with open('pelis.jsonp', 'w') as jsonp:
		jsonp.write('mvm.loadItems(')
		jsonp.write(json.dumps(data, indent=2))
		jsonp.write(');')

	csv_data = list(csv.reader(open('pelis.csv', 'r')))

	csv_data.insert(0, [
		item['title'],
		item['original_title'],
		item['director'],
		item['year'],
		item['country'],
		item['date'],
	])

	csv_save = csv.writer(open('pelis.csv', 'w'))
	csv_save.writerows(csv_data)

	dir_name = 'proyecciones/%s_%s'%(item['date'], item['title'])

	if not os.path.isfile('proyecciones/%s_%s'%(item['date'], item['title'])):
		os.mkdir('proyecciones/%s_%s'%(item['date'], item['title']))

	print('Ahora puedes poner los archivos en "%s"'%dir_name)
