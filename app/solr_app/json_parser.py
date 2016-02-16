from config import *
# import config and then use config.


class JsonParser(object):

    """
            Class for parsing the JSON as per as the rules specified in
            the Documentation.
    """

    def __init__(self, input_json):
        self._json = input_json

    def is_not_or_not(self, _query):
        if _query.get(IS_NOT):
            return _query[IS_NOT][VALUE]

    def get_query_string(self, _field, _field_value):
        try:
            query = ''
            if _field_value.get(TYPE):
                if _field_value[TYPE] == Datatype['ARRAY']:
                        # Plaese check the type of the value
                    for value in _field_value[VALUE]:
                        query += '(' + _field + ':' + str(value) + ') OR '
                    # remove extra ' OR ' from query
                    query = query[:-4]
                elif _field_value[TYPE] == Datatype['DICTIONARY']:
                    query += '(' + _field + ':' + '['
                    range_parameters = _field_value[VALUE]
                    query += str(range_parameters[MIN_VALUE][VALUE]) + \
                        ' TO ' + str(range_parameters[MAX_VALUE][VALUE])
                    query += '])'
                else:
                    query += '(' + _field + ':' + \
                        str(_field_value[VALUE]) + ')'
            return query
        except Exception as e:
            raise Exception(
                str(e) + "\nError occured while creating query string from fields.")

    def get_filters_query(self, _fields):
        try:
            if _fields.get(TYPE):
                if _fields[TYPE] == Datatype['DICTIONARY']:
                    query = ''
                    for field, field_value in _fields[VALUE].iteritems():
                        # create query string for a particular field
                        query += '(' + self.get_query_string(field,
                                                             field_value) + ') AND '
                    # remove extra ' AND ' from query
                    return query[:-5]
        except Exception as e:
            raise Exception(
                str(e) + "\nError in recovering query from fields.")

    def parse_filters(self, _filters):
        try:
            # please add the else statement with a raise
            if _filters.get(TYPE):
                # please add the else statement with a raise

                if (_filters[TYPE] == Datatype['ARRAY']):
                    query_string = ''
                    # iterate over each query in input filters
                    for query in _filters[VALUE]:
                        # please add the else statement with a raise

                        if query.get(TYPE):
                                 # please add the else statement with a raise

                            if query[TYPE] == Datatype['DICTIONARY']:
                                # please add the else statement with a raise

                                # check if this query needs to be negated
                                not_query = self.is_not_or_not(query[VALUE])
                                if (not_query == False):
                                    query_string += ' OR '
                                else:
                                    query_string += ' NOT '

                                # get query string out of this particular
                                # filter set
                                query_string += '(' + \
                                    self.get_filters_query(
                                        query[VALUE][FIELDS]) + ')'
                    return query_string[4:]
        except Exception as e:
            raise Exception(str(e))

    def parse(self):
        try:
                # please add the else statement with a raise
                # change the below condition in according to FILTER_KEY as list
            if (self._json.get(FILTER_KEY)):
                _filters = self._json[FILTER_KEY]
                query_string = self.parse_filters(_filters)
                return query_string
        except Exception as e:
            print str(e)
