import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_print(self):
        printable = BaseModel.__str__
        assert printable is not None
