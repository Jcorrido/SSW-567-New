import unittest
from unittest import mock
from unittest.mock import Mock, patch
import GetApi

class TestApi(unittest.TestCase):

    @patch('GetApi.getRepoCommits')
    def testDataNotEmpty(self, mock_commits):
        dict = {'hellogitworld': 30}
        mock_commits.return_value = dict

        self.assertNotEqual(len(GetApi.getRepoCommits("richkempinski")), 0, "dictionary should not be empty")

    @patch('GetApi.getRepoCommits')
    def testDataHasRepositortNames(self, mock_commits):
        dict = {'hellogitworld': 30}
        mock_commits.return_value = dict

        self.assertNotEqual(dict["hellogitworld"], None, "repository 'hellogitworld' should be in dictionary")

    @patch('GetApi.getRepoCommits')
    def testCommitCount(self, mock_commits):
        dict = {'hellogitworld': 30}
        mock_commits.return_value = dict

        dict = GetApi.getRepoCommits("richkempinski")
        self.assertNotEqual(len(dict), 0, "dictionary should not be empty")
        if len(dict) == 0:
            return
        self.assertEqual(dict["hellogitworld"], 30, "repository 'hellogitworld' should have 30 commits")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    