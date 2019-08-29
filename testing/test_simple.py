import unittest


class TestSimple(unittest.TestCase):
    def test_simple1(self):

        self.assertEqual(2, 2)

    def test_simple2(self):
        self.assertIn(1, [4, 5])

    def test_simple3(self):
        self.assertLess(8, 9)


if __name__ == '__main__':
    unittest.main()
