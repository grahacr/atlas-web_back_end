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

    @patch.object(client.GithubOrgClient, 'org', return_value={"repos_url": "https://api.github.com/orgs/google/repos"})
    def test_public_repos_url(self, mock_org):
        '''
        '''
        org_name = "google"
        client_instance = client.GithubOrgClient(org_name)
        expected_url = "https://api.github.com/orgs/google/repos"
        self.assertEqual(client_instance._public_repos_url, expected_url)
        mock_org.assert_called_once()

if __name__ == "__main__":
    unittest.main()
