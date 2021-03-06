import os
import sys
from json_parser import *

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from common_utils import *

def parse_json(json):
	try:
		json_parser = JsonParser(json)
		return json_parser.parse()
	except Exception as e:
		raise Exception(str(e))

			