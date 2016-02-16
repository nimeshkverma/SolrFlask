import os
import sys
import json
from mysolr import Solr
from flask import request
from utils import parse_json

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from decorators import raise_exception


@raise_exception("Solr query can't be executed: ")
def query_solr():
    query = json.loads(request.data)
    query_string = parse_json(query)
    solr = Solr(
        'http://52.76.188.127:8983/solr/clickstream_event_shard1_replica1/')
    solr_response = solr.search(q=query_string)

    return json.dumps(solr_response.documents)
