import os
from flask import Flask, jsonify
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler, SMTPHandler

app = Flask(__name__)


from app.solr_app.urls import solr_app

SUBAPP_OBJECT_MAPPING = {
    'SolrApp': solr_app,
}


def register_subapp():
    for sub_app_prefix, sub_app_obj in SUBAPP_OBJECT_MAPPING.iteritems():
        app.register_blueprint(
            sub_app_obj, url_prefix="/"+sub_app_prefix)


def configure_app(app):
    environ_type = os.environ.get('APP_ENVIRONMENT')
    if environ_type:
        app.config.from_object(environ_type)
        FILE_LOGGER_CONFIG = app.config.get('FILE_LOGGER', {})
        file_handler = TimedRotatingFileHandler(FILE_LOGGER_CONFIG.get(
            'location'), when=FILE_LOGGER_CONFIG.get('duration'), backupCount=FILE_LOGGER_CONFIG.get('backup'))
        file_handler.setLevel(FILE_LOGGER_CONFIG.get('level'))
        file_handler.setFormatter(
            Formatter(FILE_LOGGER_CONFIG.get('format')))
        app.logger.addHandler(file_handler)

        # if environ_type == 'ProductionConfig':
        #     email_handler = SMTPHandler(app.config.get('EMAIL_LOGGER_SERVER'), app.config.get(
        #         'EMAIL_LOGGER_SENDER'), app.config.get('EMAIL_LOGGER_RECIPIENTS'), app.config.get('EMAIL_LOGGER_SUBJECT'))
        #     email_handler.setLevel(app.config.get('EMAIL_LOGGER_LEVEL'))
        #     email_handler.setFormatter(
        #         Formatter(app.config.get('EMAIL_LOGGER_FORMAT')))
        #     app.logger.addHandler(email_handler)
    else:
        print "Please setup the 'APP_ENVIRONMENT' variable "


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Message": "URL not supported"}), 404
