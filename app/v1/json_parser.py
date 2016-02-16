from config import *

class JsonParser(object):
	''' 
	Class with defined features for parsing json file as described in documentation into solr query
	'''
	def __init__(self, json_file):
		self._json = json_file

	def is_not_or_not(self, _query):
		if _query.get(IS_NOT):
			return _query[IS_NOT][VALUE]

	def get_query_string(self, _field, _field_value):
		try:
			query = ''
			if _field_value.get(TYPE):
				if _field_value[TYPE] == Datatype['ARRAY']:
					for value in _field_value[VALUE]:
						query += '(' + _field + ':' + str(value) + ') OR '
					# remove extra ' OR ' from query
					query = query[:-4]
				elif _field_value[TYPE] == Datatype['DICTIONARY']:
					query += '(' + _field + ':' + '['
					range_parameters = _field_value[VALUE]
					query += str(range_parameters[MIN_VALUE][VALUE]) + ' TO ' + str(range_parameters[MAX_VALUE][VALUE])
					query += '])'
				else:
					query += '(' + _field + ':' + str(_field_value[VALUE]) + ')'
			return query
		except Exception as e:
			raise Exception(str(e) + "\nError occured while creating query string from fields.")

	def get_filters_query(self, _fields):
		try:
			if _fields.get(TYPE):
				if _fields[TYPE] == Datatype['DICTIONARY']:
					query = ''
					for field, field_value in _fields[VALUE].iteritems():
						# create query string for a particular field
						query += '(' + self.get_query_string(field, field_value) + ') AND '
					# remove extra ' AND ' from query
					return query[:-5]
		except Exception as e:
			raise Exception(str(e) + "\nError in recovering query from fields.")

	def parse_filters(self, _filters):
		try:
			if _filters.get(TYPE):
				if (_filters[TYPE] == Datatype['ARRAY']):
					query_string = ''
					# iterate over each query in input filters
					for query in _filters[VALUE]:
						if query.get(TYPE):
							if query[TYPE] == 	Datatype['DICTIONARY']:
								# check if this query needs to be negated
								not_query = self.is_not_or_not(query[VALUE])
								if (not_query == False):
									query_string += ' OR '
								else:
									query_string += ' NOT '

								# get query string out of this particular filter set
								query_string += '(' + self.get_filters_query(query[VALUE][FIELDS]) + ')'
					return query_string[4:]
		except Exception as e:
			raise Exception(str(e)) 

	def parse(self):
		try:
			if (self._json.get(FILTER_KEY)):
				_filters = self._json[FILTER_KEY]				
				self._query_string = self.parse_filters(_filters)
				return self._query_string
		except Exception as e:
			print str(e)
