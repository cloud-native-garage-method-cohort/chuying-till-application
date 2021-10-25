import logging
import sys
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
logging.info(sys.path)

import main
from unittest import TestCase

class Models(TestCase):
  def test_greet(self):
    greeting = main.greet('world', 'python')
    assert greeting == f'Hello world! This is python'
