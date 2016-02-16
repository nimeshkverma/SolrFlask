from flask import Blueprint
from views import query_solr

solr_app = Blueprint('solr_app', __name__)

solr_app.add_url_rule('/query_solr', view_func=query_solr, methods=['POST'])
