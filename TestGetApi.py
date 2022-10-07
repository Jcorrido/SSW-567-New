import unittest
from GetApi import getRepoCommits

class TestApi(unittest.TestCase):
    def testDataNotEmpty(self):
        self.assertNotEqual(len(getRepoCommits("richkempinski")), 0, "dictionary should not be empty")

    def testDataHasRepositortNames(self):
        dict = getRepoCommits("richkempinski")
        self.assertNotEqual(dict["hellogitworld"], None, "repository 'Complexity' should be in dictionary")

    def testCommitCountCorrect(self):
        dict = getRepoCommits("richkempinski")
        self.assertNotEqual(len(dict), 0, "dictionary should not be empty")
        if len(dict) == 0:
            return
        self.assertEqual(dict["hellogitworld"], 29, "repository 'hellogitworld' should have 29 commits")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()