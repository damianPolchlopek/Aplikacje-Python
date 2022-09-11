#!/usr/bin/python

import unittest
from binaryTree import*

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.b1 = BinaryTree()
        self.b1.insert(8)
        self.b1.insert(4)
        self.b1.insert(12)
        self.b1.insert(2)
        self.b1.insert(6)
        self.b1.insert(10)
        self.b1.insert(14)
        self.b1.insert(15)
        self.b1.insert(16)


    def test_depth(self):
        self.assertEqual(self.b1.depth(), 5)

    def test_size(self):
        self.assertEqual(self.b1.size(), 9)

    def test_maximum(self):
        self.assertEqual(self.b1.maximum(), 16)

    def test_minimum(self):
        self.assertEqual(self.b1.minimum(), 2)

    def test_search(self):
        self.assertTrue(self.b1.search(8))
        self.assertTrue(self.b1.search(8))



if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
