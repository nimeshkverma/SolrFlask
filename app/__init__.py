import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from app_config import configure_app, register_subapp, app

configure_app(app)
register_subapp()
