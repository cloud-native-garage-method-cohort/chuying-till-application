import sys
print(f'{sys.path=}')
sys.path.append('/workspace/source')
import main
from unittest import TestCase

class Models(TestCase):
  def test_greet(self):
    greeting = main.greet('world', 'python')
    assert greeting == f'Hello world! This is python!'
