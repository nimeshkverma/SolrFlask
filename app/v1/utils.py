import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from common_utils import *

def listFieldUtil(field_json, field):
	query_string = []
	for row in field_json:
		
		query_part = field + ':'
		if (type(row) is dict):
			query_part += '['
			if (row['min'] <= row['max']):
				query_part += row['min'] + ' TO ' + row['max']
			else:
				raise Exception(field + ': min value is greater than max value')
			query_part += '] '
		else:
			query_part += row
		
		query_string.append(query_part)

	# create returning string
	resultant_query = ''
	for i in range(1, len(query_string)):	
		resultant_query += ' OR ' + query_string[i] 
	resultant_query = query_string[0] + resultant_query
	return '(' + resultant_query + ')'


def dictFieldUtil(field_json, field):
	raise Exception('Invalid Json Input')


def primaryFieldUtil(field_json, field):
	resultant_query = ''
	resultant_query = field + ': ' + field_json
	return resultant_query


def parse_json(json):
	list_filters = ['filters', 'or', 'not']
	resultant_query = ''

	for key in json.keys():
		if key in list_filters:
			filter_json = json[key]			
			query_string = ''
			for field in filter_json.keys():	# traverse all the fields in each filter
				field_json = filter_json[field]
				if (type(field_json) is list):
					query_string += (listFieldUtil(field_json, field)) + ' AND '
				elif (type(field_json) is dict):
					query_string += (dictFieldUtil(field_json, field)) + ' AND '
				else:
					query_string += (primaryFieldUtil(field_json, field)) + ' AND '


			if (key == 'or'):
				resultant_query += ' OR '
			elif (key == 'not'):
				resultant_query += ' NOT '

			resultant_query += '( ' + query_string[:-5] + ' )'
	
	return resultant_query

			