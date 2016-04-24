#!/usr/bin/env python3
import json
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
	item['fqn'] = "%s (%s) %s %s [%s]"%(item['title'], item['original_title'], item['director'], item['year'], item['country'])

	data = json.load(open('pelis.json'))

	data.insert(0, item)

	json.dump(data, open('pelis.json', 'w'), indent=2)

	dir_name = 'proyecciones/%s_%s'%(item['date'], item['title'])

	os.mkdir('proyecciones/%s_%s'%(item['date'], item['title']))

	print('Ahora puedes poner los archivos en "%s"'%dir_name)
