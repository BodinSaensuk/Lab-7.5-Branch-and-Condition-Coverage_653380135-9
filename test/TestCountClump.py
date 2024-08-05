# test_count_clump.py
import unittest
from CountClump import CountClump

class TestCountClump(unittest.TestCase):
    def test_CDC01(self):
        self.assertEqual(CountClump.count_clumps([]), 0)

    def test_CDC02(self):
        self.assertEqual(CountClump.count_clumps([None]), 0)

    def test_CDC03(self):
        self.assertEqual(CountClump.count_clumps([1]), 0)

    def test_CDC04(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 1]), 1)

    def test_CDC05(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 3]), 0)

if __name__ == '__main__':
    unittest.main()