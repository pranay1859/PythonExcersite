import test
import unittest

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        resulte = test.do_stuff(test_param)
        self.assertEqual(resulte, 15)
    d