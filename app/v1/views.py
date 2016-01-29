from flask import jsonify, request
from utils import *
import json
from mysolr import Solr

def query_solr():
	j = json.loads(request.data)
	query_string = parse_json(j)
	print query_string

	solr = Solr('http://52.76.188.127:8983/solr/clickstream_event_shard1_replica1/')
	solr_response = solr.search(q=query_string)

	return json.dumps(solr_response.documents)


				
