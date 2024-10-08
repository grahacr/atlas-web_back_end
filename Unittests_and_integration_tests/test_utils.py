#!/usr/bin/env python3
'''
unit tests utils file
'''
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''class for testing nested map
    utilizing parameterized and assertEqual'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        class method takes 4 args:
        -self
        -nested_map
        -path(specific path of nested map)
        -expected (expected output)
        '''
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''
        test nested map exception method. takes 3 args:
        - self
        - nested_map
        - path
        '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    Test class for testing getjson utilizing patch
    and mock so as to not actually make an HTTP get call
    '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''
        method to test get json using mock. takes 3 args:
        -self
        -test_url
        -test_payload
        -mock_get (patched get method)
        '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''
    test case for testing memoize function
    '''
    def test_memoize(self):
        '''
        test_memoize takes only self as arg
        includes testclass
        '''
        class TestClass:
            '''nested class with memoized method'''
            def a_method(self):
                '''method testing for memoization'''
                return 42

            @memoize
            def a_property(self):
                '''memoized method'''
                return self.a_method()
        test_instance = TestClass()

        with patch.object(test_instance, 'a_method',
                          return_value=42) as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            mock_method.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
