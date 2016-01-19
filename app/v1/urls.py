from flask import Blueprint
from views import query_solr

v1 = Blueprint('v1', __name__)

v1.add_url_rule('/query_solr', view_func=query_solr, methods=['POST'])
