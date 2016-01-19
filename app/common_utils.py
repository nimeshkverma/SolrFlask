from mysolr import Solr


def query_solr(query):
    solr = Solr()
    response = solr.search(q=query)
    documents = response.documents
    return documents
