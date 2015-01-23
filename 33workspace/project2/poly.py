# Submitter: bohyunk(Kim, Bohyun)

from collections import defaultdict


class Poly:
    
    def __init__(self, *args):
        self.terms = defaultdict(int)
        self.power = []
        for val, key in args:
            assert type(val) in [int, float], 'Poly.__init__: illegal coefficient in term, coefficient must be int or float: {tup}'.format(tup = (val, key))
            assert type(key) == int, 'Poly.__init__: illegal power in term, power must be int: {tup}'.format(tup = (val, key))
            assert key >= 0, 'Poly.__init__: illegal power in term, power must be >=0 : {tup}'.format(tup = (val, key))
            self.power.append(key)
            if val!=0:
                self.terms[key] = val
        assert [self.power[i] > self.power[i+1] for i in range(len(self.power)-1)] == [True]*(len(self.power)-1), 'Poly.__init__: illegal power in term, Powers must appear in decreasing order : {arg}'.format(arg = args)
        self.initial = args
        
    def __repr__(self):
        return 'Poly('+', '.join(str(c) for c in self.initial)+')'
    
    def __str__(self):
        if self.terms == {}:
            return '0'
        
        
    
    

c = Poly((-3, 2), (-1, 1), (4, 0))
print(repr(c))
print(c.terms)
#x = eval(repr(c))
#print(type(x), x)
#print(str(c))
            