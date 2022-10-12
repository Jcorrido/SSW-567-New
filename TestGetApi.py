import unittest
from GetApi import getRepoCommits

class TestApi(unittest.TestCase):
    def testDataNotEmpty(self):
        self.assertNotEqual(len(getRepoCommits("richkempinski")), 0, "dictionary should not be empty")

    def testDataHasRepositortNames(self):
        dict1 = getRepoCommits("richkempinski")
        self.assertNotEqual(dict1["hellogitworld"], None, "repository 'hellogitworld' should be in dictionary")

    def testCommitCount(self):
        dict1 = getRepoCommits("richkempinski")
        self.assertNotEqual(len(dict1), 0, "dictionary should not be empty")
        if len(dict1) == 0:
            return
        self.assertEqual(dict1["hellogitworld"], 30, "repository 'hellogitworld' should have 30 commits")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    