from priorityqueue import PriorityQueue
import unittest, random


# Methods Tested: add, remove, clear, peek, is_empty, size

standard_size = 100

class Test_PQ(unittest.TestCase):
    def setUp(self):
        alist = [i for i in range(standard_size)]
        random.shuffle(alist)
        # puts in numbers 0 to standard_size-1
        # should come out from biggest to smallest
        self.pq  = PriorityQueue(alist)
    
    def test_add(self):
        # Throw out the setUp in this case; start empty
        self.pq = PriorityQueue()
        alist = [i for i in range(standard_size)]
        random.shuffle(alist)
        for i in range(len(alist)):
            self.pq.add(alist[i])
            self.assertEqual(self.pq.size(),i+1)
        # adding should be the same as setUp;    
        self.test_remove()          

    def test_remove(self):
        # values should come out from standard_size-1 down to 0
        for i in reversed(range(self.pq.size())):
            self.assertEqual(self.pq.remove(),i)
        # with nothing left, remove should raise an exception             
        self.assertRaises(AssertionError,PriorityQueue.remove,self.pq)

    def test_clear(self):
        self.pq.clear()
        # size is 0 in a cleared priority queue
        self.assertEqual(self.pq.size(), 0)
 
    def test_peek(self):
        # values should come out from standard_size-1 down to 0
        for i in reversed(range(self.pq.size())):
            self.assertEqual(self.pq.peek(),i)             
            self.pq.remove()             
        # with nothing left, remove should raise an exception             
        self.assertRaises(AssertionError,PriorityQueue.peek,self.pq)

    def test_is_empty(self):
        # not empty until the last value is removed
        for i in reversed(range(self.pq.size())):
            self.assertFalse(self.pq.is_empty())
            self.pq.remove()             
        # should be be empty now; the last value has been removed
        self.assertEqual(self.pq.size(), 0)

    def test_size(self):
        size = self.pq.size()
        # self.pq.size() should get 1 smaller with each remove
        for i in reversed(range(self.pq.size())):
            self.assertEqual(self.pq.size(),size)             
            self.pq.remove() 
            size -= 1            

