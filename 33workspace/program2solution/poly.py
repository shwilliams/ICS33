class Poly:
    def __init__(self,*terms):
        self.terms = {}
        old_p = None
        for c,p in terms:
            assert type(c) in [int,float], 'Poly.__init__: illegal coefficient in term ' + str((c,p))
            assert type(p) is int and p >= 0 and p not in self.terms, 'Poly.__init__: illegal power in term: ' + str((c,p))
            assert old_p == None or old_p > p, 'Poly.__init__: power in term ' + str((c,p)) + ' >=  previous power: ' + str(old_p) 
            if c != 0:
                self.terms[p] = c
            old_p = p
            
    def __repr__(self):
        print([i for i in self])
        return 'Poly'+str(tuple( term for term in self))
    

    def __str__(self):
        def term(c,p,var):
            return (str(c) if abs(c) != 1 or p == 0 else ('' if c == 1 else '-')) +\
                   ('' if p == 0 else var+('^'+str(p) if p != 1 else ''))
        if len(self.terms) == 0:
            return '0'
        else:
            return ' + '.join([term(c,p,'x') for c,p in self]).replace('+ -','- ')
 
  
    def __bool__(self):
        return len(self.terms) != 0
       
 
    def __len__(self):
        if len(self.terms) == 0:
            return 0
        else:
            return max(self.terms)
    

    def __call__(self,arg):
        return sum(self.terms[p] * arg**p for p in self.terms)

    
    def __iter__(self):
        for p,c in sorted(self.terms.items(),reverse=True):
            yield (c,p)

            
    def __getitem__(self,index):
        if type(index) is not int or index < 0:
            raise TypeError('Poly.__getitem__: index('+str(index)+') not int or < 0')
        else:    
            return self.terms.get(index,0) # if index is not a key, returns 0

            
    def __setitem__(self,index,value):
            if type(index) is not int or index < 0:
                raise TypeError('Poly.__setitem__: index('+str(index)+') not int or < 0')
            if value != 0:
                self.terms[index] = value
            elif index in self.terms:
                del self.terms[index]

            
    def __delitem__(self,index):
            if type(index) is not int or index < 0:
                raise TypeError('Poly.__delitem__: index('+str(index)+') not int or < 0')
            if index in self.terms:
                del self.terms[index]

            
    def _add_term(self,c,p):
        if type(c) not in [int,float] or type(p) is not int or p < 0:
            raise TypeError('Poly.___add_terms__: illegal coefficient('+str(c)+') or power ('+str(p)+')')
        if p in self.terms:
            self[p] += c
            if self[p] == 0:
                del self[p]
        elif c != 0:
            self[p] = c

    def __pos__(self):
        return eval(repr(self))
       
    def __neg__(self):
        return Poly(*tuple((-c,p) for c,p in self))
       
    def __abs__(self):
        return Poly(*tuple((abs(c),p) for c,p in self))
    
    def differentiate(self):
        return Poly(*tuple((p*c,p-1) for c,p in self if p != 0))
       
    def integrate(self,c=0):
        result = Poly(*tuple((1/(p+1)*c,p+1) for c,p in self))
        result._add_term(c,0)
        return result
       
    def def_integrate(self,a,b):
        i = self.integrate()
        return i(b) - i(a)
       
    def __add__(self,right):
        result = eval(repr(self))      # Many ways to initialize result to Poly(self)
        if type(right) in [int,float]:
            result._add_term(right,0)
        elif type(right) is Poly:
            for c,p in right:
                result._add_term(c,p)
        else:
            raise TypeError('Poly.__add__: cannot add Poly with '+str(right))
        return result

    
    def __radd__(self,left):
        return self+left  # use commutative property

    
    def __sub__(self,right):
        if type(right) in [int,float,Poly]:
            return self + -right           # Simple, although
        else:
            raise TypeError('Poly.__sub__: cannot add Poly with '+str(right))

    
    def __rsub__(self,left):
        return -self+left  # use commutative property

    
    def __mul__(self,right):
        if type(right) in [int,float]:
            return Poly(*[(c*right,p) for c,p in self])
        elif type(right) is Poly:
            result = Poly()
            for c1,p1 in self:
                for c2,p2 in right:
                    result._add_term(c1*c2,p1+p2)
            return result
        else:
            raise TypeError('Poly.__mul__: cannot multiply Poly by '+str(right))

    
    def __rmul__(self,left):
        return self*left  # use commutative property

    
    def __pow__(self,right):
        if type(right) is not int or right < 0:
            raise TypeError('Poly.__pow__: power('+str(right)+') must be int >= 0')
        result = Poly((1,0))
        for _ in range(right):
            result = result * self
        return result

    
    def __eq__(self,right):
        if type(right) in [int,float]:
            return self == Poly((right,0))
        if type(right) is Poly:
            return self.terms == right.terms
        else:
            raise TypeError('Poly.__eq__: cannot compute equality of Poly and '+str(right))
    
    
    def __ne__(self,right):
        if type(right) in [int,float]:
            return self != Poly((right,0))
        if type(right) is Poly:
            return self.terms != right.terms
        else:
            raise TypeError('Poly.__ne__: cannot compute equality of Poly and '+str(right))
    
    
    def __lt__(self,right):
        if type(right) in [int,float]:
            return self < Poly((right,0))
        if type(right) is Poly:
            p_self  = len(self)
            p_right = len(right)
            return p_self < p_right or (p_self == p_right and self[p_self] < right[p_right])
        else:
            raise TypeError('Poly.__lt__: cannot compute equality of Poly and '+str(right))
    
    
    def __gt__(self,right):
        if type(right) in [int,float]:
            return self > Poly((right,0))
        if type(right) is Poly:
            p_self  = len(self)
            p_right = len(right)
            return p_self > p_right or (p_self == p_right and self[p_self] > right[p_right])
        else:
            raise TypeError('Poly.__gt__: cannot compute equality of Poly and '+str(right))
    
    
    def __le__(self,right):
        return self < right or self == right
    
    def __ge__(self,right):
        return self > right or self == right
    
    def __setattr__(self,a,v):
        assert 'terms' not in self.__dict__, 'Poly.__setattr__ attempted to reset attribute'
        self.__dict__[a] = v
   
   
p = Poly((3,2),(2,1))
print(p.__repr__())
    
'''   
if __name__ == '__main__':
    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3,2),(-2,1), (4,0))
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print('  len(p):',len(p))
    print('  p(2):',p(2))
    print('  list collecting iterator results:',[t for t in p])
    print('  p+p:',p+p)
    print('  p+2:',p+2)
    print('  p*p:',p*p)
    print('  p*2:',p*2)
    print('End simple tests\n')
    
    import driver
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
    '''
