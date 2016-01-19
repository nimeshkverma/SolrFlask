from flask import jsonify, request
from utils import *


def query_solr():
    return jsonify(request.json)
