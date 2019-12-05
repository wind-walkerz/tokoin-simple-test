import unittest
import re
import utils


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_match_mix(self):
        """ Tests is_match() for 1 integers and 1 string"""
        actual = utils.is_match(1, "1")
        expected = True

        self.assertEqual(actual, expected)

    def test_is_match_bool(self):
        """ Tests is_match() for 1 string and 1 bool"""
        actual = utils.is_match("true", True)
        expected = True

        self.assertEqual(actual, expected)

    def test_is_match_same(self):
        """ Tests is_match() for 2 string"""

        actual = utils.is_match('1', "1")
        expected = True

        self.assertEqual(actual, expected)

    def test_capitalize(self):
        """ Tests test_capitalize() """
        actual = bool(re.search("^[A-Z]{1}", utils.capitalize('string')))
        expected = True
        self.assertEqual(actual, expected)
