fname = 'ДЗ1.csv'

import csv

with open(fname) as f:
	reader = csv.DictReader(f)
	print(reader.fildsnames)
	lines = list(reader)

print(lines[0], ['Код BOT_CONFIG'])

codes = [l['Код BOT_CONFIG'] for l in lines]	