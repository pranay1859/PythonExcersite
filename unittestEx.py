import unittest
import umain


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp before every test')

    def test_do_stuff(self):
        '''Test that do_stuff returns a number +  5'''
        test_param = 10
        resulte = umain.do_stuff(test_param)
        self.assertEqual(resulte, 15)

    def test_do_stuff_2(self):
        test_param = 'test some srting '
        resulte = umain.do_stuff(test_param)
        self.assertIsInstance(resulte, ValueError)

    def test_do_stuff_3(self):
        test_param = None
        resulte = umain.do_stuff(test_param)
        self.assertIsInstance(resulte, ValueError)
    
    def tearDown(self) -> None:
        print('tearDown after every test')

if __name__ == '__main__':
    unittest.main()
