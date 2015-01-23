import random
import unittest

class Sorting(unittest.TestCase):
    def setUp(self):
        self.alist  = [4, 3, 1, 2, 0]
        self.sorted = [0, 1, 2, 3, 4]
        list.sort(self.alist)
    
    def test_order(self):
        self.assertTrue(self._is_ordered(), 'List is not in order')
    
    def test_permutation(self):
        print('Checking for permutation:',self.alist,'vs',self.sorted)
        self.assertCountEqual(self.alist,self.sorted,
                              'List is not a permutation of the original')
    
    def _is_ordered(self):
        for i in range(len(self.alist)-1):
            if self.alist[i] > self.alist[i+1]:
                return False
        return True 
