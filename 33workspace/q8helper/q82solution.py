from bag import Bag
import unittest   #use unittest.TestCase
import random     #use random.shuffle, random.randint

class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
    
    
    def test_len(self):
        print('Checking for length:',self.alist)
        self.assertEqual(len(self.bag),7, 'Initial length of the self.bag is not 7')
        bag_length = 7
        for l in self.alist:
            self.bag.remove(l)
            bag_length -= 1
            self.assertEqual(len(self.bag),bag_length, 'length of bag object is {lenbag} but it is supposed to be {good}'.format(lenbag = str(len(self.bag)), good = str(bag_length)))
        
        
    def test_unique(self):
        print('Checking for length:',self.alist)
        self.assertEqual(self.bag.unique(), 4, 'Intial unique values in self.bag is not 4')
        alist = self.alist
        for i in range(len(self.alist)):
            self.bag.remove(self.alist[i])
            alist = self.alist[i+1:]
            self.assertEqual(self.bag.unique(),len(set(alist)), 'Number of unique value in bag is {uniqueb} but should be {setlength}'.format(uniqueb = str(self.bag.unique()) ,setlength = str(len(set(alist)))))
            
            
    def test_contains(self):
        print('Checking for contains:',self.alist)       
        for el in ['a', 'b', 'c','d']:
            self.assertTrue(el in self.bag, '{el} is not in self.bag')
        self.assertFalse('x' in self.bag, 'x is in self.bag')
        
    
    def test_count(self):
        print('Checking for counts:',self.alist)
        for num, el in [(1,'a'), (2, 'b'), (1, 'c'), (3, 'd'), (0, 'x')]:
            self.assertEqual(num, self.bag.count(el), 'Initially self.bag contains {num}{el} but it contains {numb}'.format(num = str(num), el = str(el), numb = str(self.bag.count(el))))
        init_sum = 7
        for l in self.alist:
            self.bag.remove(l)
            init_sum -= 1
            bag_sum = sum([self.bag.count(i) for i in ['a','b','c','d']])
            self.assertEqual(init_sum, bag_sum , 'sum of the counts of abcd should {init_sum} but it is {bag_sum}'.format(init_sum = init_sum, bag_sum = bag_sum))
    
    def test_equal(self):
        print('Checking for equal')
        alist = [random.randint(1,10) for i in range(1000)]
        bag1 = Bag(alist)
        random.shuffle(alist)
        bag2 = Bag(alist)
        self.assertEqual(bag1, bag2, 'Two back must be equal initially')
        bag2.remove(alist[0])
        self.assertNotEqual(bag1, bag2, 'Two back must not be equal after removing the first element of bag2')
        
    
    def test_add(self):
        print('Checking for add')
        bag1 = Bag([random.randint(1,10) for i in range(1000)])
        bag2 = Bag()
        for el in iter(bag1):
            bag2.add(el)
        self.assertEqual(bag1,bag2, 'bag1 and bag 2 must be equal after adding all terms')
        
    
    def test_remove(self):
        print('Checking for remove')
        alist = [random.randint(1,10) for i in range(1000)]
        bag1 = Bag(alist)
        self.assertRaises(ValueError, Bag.remove,bag1,32)
        bag2 = Bag(alist)
        
        for el in alist:
            bag2.add(el)
        for el in alist:
            bag2.remove(el)
        
        self.assertEqual(bag1,bag2, 'Two bag must be same after removing elements from bag2')
        
            
            

                  
