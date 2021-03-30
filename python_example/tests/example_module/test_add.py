import unittest
from python_example.example_module import add


class TestAdd(unittest.TestCase):

    def setUp(self):
        pass # code executed before each test

    def test_add(self):
        assert add(1, 2) == 3, 'Test for adding numbers failed'

    def tearDown(self):
        pass # code executed after each test
