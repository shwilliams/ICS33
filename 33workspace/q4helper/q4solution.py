# primes is used to test code you write below
from predicate import is_prime

def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1 

def peaks(iterable):
    l = []
    it = iter(iterable)
    save = next(it)
    peak = next(it)
    action = ''
    while action != 'quit':
        try:
            temp = next(it)
            if peak > save and peak> temp:
                l.append(peak)
            save = peak
            peak = temp
        except StopIteration:
            action = 'quit'
    return l
 
 
class Permutation:
    def __init__(self,p,start):
        self.l = p
        self.start = start
        
    def __iter__(self):
        class P_iter:
            def __init__(self, p, start):
                self.l = p
                self.start = start
                self.
                self.stop = 
                
            def __next(self):
                if 
                
                
    
class Permutation2:
    def __init__(self,p,start):
        pass
        
    def __iter__(self):
        pass
    
    
def compress(vit,bit):
    pass
            
            
def skipper(iterable,n=0):
    pass

        

if __name__ == '__main__':
    import driver
    from goody import irange
    import traceback
    
    driver.driver() # type quit in driver to return and execute code below
    
    # Test increases; add your own test cases
    print('Testing peaks')
    print(peaks([0,1,-1,3,8,4,3,5,4,3,8]))
    print(peaks([5,2,4,9,6,1,3,8,0,7]))
    print(peaks([1,2,3,4,5]))
    print(peaks([0,1]))
    
    #prints a 1 for every prime preceded/followed by a non prime
    #below 5, 7, 11, 13, 17, 19 have that property the result should be a list of 6 1s
    #[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
    #[0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    print(list(int(is_prime(p)) for p in irange(1,20)))
    print(peaks(int(is_prime(p)) for p in irange(1,20)))
    
    
    # Test Permutation/Permuation2; add your own test cases
    print('\nTesting Permutation')
    for i in Permutation([4,0,3,1,2],0):
        print(i,end='')
    print()
    
    for i in Permutation([4,0,3,1,2],3):
        print(i,end='')
    print()
    
    for i in Permutation([0],0):
        print(i,end='')
    print()
    

    print('\nTesting Permutation2')
    for i in Permutation2([4,0,3,1,2],0):
        print(i,end='')
    print()
    
    for i in Permutation2([4,0,3,1,2],3):
        print(i,end='')
    print()
    
    for i in Permutation2([0],0):
        print(i,end='')
    print()
    

        
    # Test compress; add your own test cases
    print('\nTesting Compress')
    for i in compress('abcdefghijklmnopqrstuvwxyz',
                      [is_prime(i) for i in irange(1,26)]):
        print(i,end='')
    print()
    
    
    print('\nTesting Compress')
    for i in compress('abcdefghijklmnopqrstuvwxyz',
                      (is_prime(i) for i in irange(1,26))):
        print(i,end='')
    print()
    
    
    # Test skipper; add your own test cases
    print('\nTesting skipper')
    for i in skipper('abcdefghijklmnopqrstuvwxyz'):
        print(i,end='')
    print()

    for i in skipper('abcdefghijklmnopqrstuvwxyz',1):
        print(i,end='')
    print()

    for i in skipper('abcdefghijklmnopqrstuvwxyz',2):
        print(i,end='')
    print()

    # Primes 1-50: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
    # Skipping 2 : 2 7 17 29 41 
    for i in skipper(primes(50),2):
        print(i,end=' ')
    print()

