#!/usr/bin/env python3
'''
unit tests for client file
'''
import client
import unittest
from unittest.mock import patch, Mock, PropertyMock
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

    @patch.object(client.GithubOrgClient, 'org',
                  return_value=({"repos_url":
                                 "https://api.github.com/orgs/google/repos"}))
    def test_public_repos_url(self, mock_org):
        '''
        unit test method for _public_repos_url property of client
        takes 2 args:
        - self
        - mock_org (from patch of "org" method)
        '''
        org_name = "google"
        client_instance = client.GithubOrgClient(org_name)
        expected_url = "https://api.github.com/orgs/google/repos"
        self.assertEqual(client_instance._public_repos_url, expected_url)
        mock_org.assert_called_once()

    @patch('client.get_json')
    @patch.object(client.GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        '''
        method to test public_repos method in client
        patch get_json method and _public_repos_url object
        takes 3 args:
        - self
        - mock_public_repos_url (from patch)
        - mock_get_json (from patch)
        '''

        mock_public_repos_url.return_value = (
            "https://api.github.com/orgs/google/repos")

        mock_get_json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"},
        ]

        client_instance = client.GithubOrgClient("google")
        repos = client_instance.public_repos()
        expected_repos = ["Repo1", "Repo2"]
        self.assertEqual(repos, expected_repos)
        mock_get_json.assert_called_once_with(
            mock_public_repos_url.return_value)
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):

        

if __name__ == "__main__":
    unittest.main()
