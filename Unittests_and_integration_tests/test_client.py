#!/usr/bin/env python3
'''
unit tests for client file
'''
import client
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''
    Class for testing githuborgclient
    '''
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_url, mock_get_json):
        '''
        test org function in client file
        utilize patch, mock, and parameterized for args:
        - self
        - org_url (paramterized options)
        - mock_get_json (stored function call from patch - 
        get_json)
        Method ensures that when a specific org url is given,
        the return value should contain the correct url
        and that the mocked get function is only called once.
        '''
        mock_request = client.GithubOrgClient(org_url)
        mock_return = mock_get_json.return_value
        self.assertEqual(mock_request.org, mock_return)
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
