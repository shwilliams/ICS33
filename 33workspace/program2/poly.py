#Submitter: bohyunk(Kim, Bohyun)


from collections import defaultdict


class Poly:
        
    def __init__(self, *args):
        self.terms = defaultdict(int)
        power = []
        for val, key in args:
            assert type(val) in [int, float], 'Poly.__init__: illegal coefficient in term, coefficient must be int or float: {tup}'.format(tup = (val, key))
            assert type(key) == int, 'Poly.__init__: illegal power in term, power must be int: {tup}'.format(tup = (val, key))
            assert key >= 0, 'Poly.__init__: illegal power in term, power must be >=0 : {tup}'.format(tup = (val, key))
            power.append(key)
            if val!=0:
                self.terms[key] = val
        assert [power[i] > power[i+1] for i in range(len(power)-1)] == [True]*(len(power)-1), 'Poly.__init__: illegal power in term, Powers must appear in decreasing order : {arg}'.format(arg = args)

    
        
    def __repr__(self):
        return 'Poly('+', '.join(str(c) for c in sorted([(self.terms[k], k) for k in self.terms], key = lambda x: x[1], reverse = True))+')'
        
    
    def conversion(self, pow, coe, first):
        if first == False:
            sign = '+' if coe >0 else '-'
        else:
            sign = ''if coe >0 else '-'
        if pow >= 1:
            if coe == 1 or coe == -1:
                coe = ''
            else:
                coe = (abs(coe))
        space = ' '*(lambda x: x == False)(first)
        if pow == 1:
            return space+sign+space+str(coe)+'x'
        elif pow == 0:
            return space+sign+space+str(abs(coe))
        else:
            return space+sign+space+str(coe)+'x^{}'.format(str(pow))
    
    
    def __str__(self):
        if self.terms == {}:
            return '0'
        else:
            strpoly = ''
            copp = sorted([(self.terms[key], key) for key in self.terms.keys()], key = lambda x: x[1], reverse = True)
            fcoe, fpower = copp.pop(0)
            strpoly += self.conversion(fpower, fcoe, True)
            for fcoe,fpower in copp:
                strpoly+= self.conversion(fpower, fcoe, False)
                
            return strpoly
        
        
    def __bool__(self):
        return str(self) != '0'
        
        
    def __len__(self):
        return 0 if self.terms == {} else max(self.terms.keys())
               
    
    def __call__(self, num):
        return sum([((num)**(key))*self.terms[key] for key in self.terms.keys()])


    def __iter__(self):
        class prange_iter:
            def __init__(self, d, index):
                self.it = sorted([(d[k],k) for k in d], key = lambda x: x[1], reverse = True)+[(0,0)]
                self.index = index
                self.n = self.it[0]
                
            def __next__(self):
                if self.index == len(self.it)-1:
                    raise StopIteration
                else: 
                    save = self.n
                    self.index += 1
                    self.n = self.it[self.index]
                    return save
        return prange_iter(self.terms, 0)        

    
    def __getitem__(self, p):
        if type(p) != int or p <0:
            raise TypeError('Poly.__getitem__:illegal power in argument, the power must be int or >=0')
        return 0 if p not in self.terms.keys() else self.terms[p]
    
    
    def __setitem__(self, p, coe):
        if type(p) != int or p <0:
            raise TypeError('Poly.__setitem__:illegal power in argument, the power must be int or >=0')
        self.terms[p] = coe
        if coe == 0:
            del self.terms[p]
    
        
    def __delitem__(self, pow):
        if type(pow) != int or pow <0:
            raise TypeError('Poly.__delitem__:illegal power in argument, the power must be int or >=0')
        if pow in self.terms:
            del self.terms[pow]
    
    
    def _add_term(self, coe, pow):
        if type(pow) != int or pow <0:
            raise TypeError('Poly._add_term:illegal power in argument, the power must be int or >=0')
        if type(coe) not in [int, float]:
            raise TypeError('Poly._add_term:illegal coefficient in argument, the power must be int or float')
        if pow not in self.terms:
            self.terms[pow] = coe
        else:
            self.terms[pow] = self.terms[pow] + coe
        for k,v in list(self.terms.items()):
            if v == 0:
                del self.terms[k]
        
    
    def __pos__(self):
        return Poly(*(sorted(((self.terms[pow],pow) for pow in self.terms), key = lambda x: x[1], reverse = True)))    
   
   
    def __neg__(self):
        return Poly(*(sorted(((-self.terms[pow],pow) for pow in self.terms), key = lambda x: x[1], reverse = True)))    
   
    
    def __abs__(self):
        return Poly(*(sorted(((abs(self.terms[pow]),pow) for pow in self.terms), key = lambda x: x[1], reverse = True)))    
   
    
    def differentiate(self):
        return Poly(*(sorted(((pow*self.terms[pow], pow-1) for pow in self.terms if pow >0), key = lambda x: x[1], reverse = True)))


    def integrate(self, num=0):
        return Poly(*(sorted(list((self.terms[pow]/(pow+1), pow+1) for pow in self.terms)+[(num,0)], key = lambda x: x[1], reverse = True)))
    
    def def_integrate(self, num1, num2):
        return self.integrate(0)(num2) - self.integrate(0)(num1)  
         
         
    def __radd__(self, right):
        subpol = self.__pos__()
        if type(right) not in [int, float, Poly]:
            raise TypeError('Poly.__radd__:illegal argument type, the argument must be int, float, or Poly')
        if type(right) in [int, float]:
            subpol.terms[0] = subpol.terms[0]+right
        else:
            for p in right.terms:
                subpol._add_term(right.terms[p],p)
        return Poly(*sorted(((subpol.terms[po],po) for po in subpol.terms),key = lambda x: x[1], reverse = True))

    def __add__(self, left):
        subpol = self.__pos__()
        if type(left) not in [int, float, Poly]:
            raise TypeError('Poly.__add__:illegal argument type, the argument must be int, float, or Poly')
        if type(left) in [int, float]:
            subpol.terms[0] = subpol.terms[0]+left
        else:
            for p in left.terms:
                subpol._add_term(left.terms[p],p)
        return Poly(*sorted(((subpol.terms[po],po) for po in subpol.terms),key = lambda x: x[1], reverse = True))

    
    def __rsub__(self, left):
        subright = self.__neg__()
        if type(left) not in [int, float, Poly]:
            raise TypeError('Poly.__rsub__:illegal argument type, the argument must be int, float, or Poly')
        if type(left) in [int, float]:
            subright.terms[0] = left+subright.terms[0]
        else:
            subleft = left.__pos__()
            for p in subleft.terms:
                subright._add_term(subleft.terms[p],p)
        return Poly(*(sorted(((subright.terms[po],po) for po in subright.terms), key = lambda x: x[1], reverse = True)))    
    
    
    def __sub__(self, right):
        subleft = self.__pos__()
        if type(right) not in [int, float, Poly]:
            raise TypeError('Poly.__sub__:illegal argument type, the argument must be int, float, or Poly')
        if type(right) in [int, float]:
            subleft.terms[0] = subleft.terms[0]-right
        else:
            subright = right.__neg__()
            for p in subright.terms:
                subleft._add_term(subright.terms[p],p)
        return Poly(*(sorted(((subleft.terms[po],po) for po in subleft.terms), key = lambda x: x[1], reverse = True)))    
    
    def __mul__(self,right):
        subleft = self.__pos__()
        if type(right) not in [int, float, Poly]:
            raise TypeError('Poly.__mul__:illegal argument type, the argument must be int, float, or Poly')
        if type(right) in [int, float]:
            for k in subleft.terms:
                subleft.terms[k] = subleft.terms[k]*right
            return Poly(*(sorted(((subleft.terms[po],po) for po in subleft.terms), key = lambda x: x[1], reverse = True)))
        if str(right) == '0' or right.terms == 0:
            return 0
         
        else:
            subright = right.__pos__()
            subpoly = [Poly((subright.terms[p]*subleft.terms[q], p+q))for p in subright.terms for q in subleft.terms]
            npol = subpoly.pop(0)
            for pol in subpoly:
                for k in pol.terms:
                    npol._add_term(pol.terms[k],k)
            return Poly(*(sorted(((npol.terms[po],po) for po in npol.terms), key = lambda x: x[1], reverse = True)))    
        
    def __rmul__(self,left):
        subright = self.__pos__()
        if type(left) not in [int, float, Poly]:
            raise TypeError('Poly.__rmul__:illegal argument type, the argument must be int, float, or Poly')
        if type(left) in [int, float]:
            for k in subright.terms:
                subright.terms[k] = subright.terms[k]*left
            return Poly(*(sorted(((subright.terms[po],po) for po in subright.terms), key = lambda x: x[1], reverse = True)))
        if str(left) == '0' or left.terms == 0:
            return 0
         
        else:
            subleft = left.__pos__()
            subpoly = [Poly((subright.terms[p]*subleft.terms[q], p+q))for p in subleft.terms for q in subright.terms]
            npol = subpoly.pop(0)
            for pol in subpoly:
                for k in pol.terms:
                    npol._add_term(pol.terms[k],k)
            return Poly(*(sorted(((npol.terms[po],po) for po in npol.terms), key = lambda x: x[1], reverse = True)))    

    def __pow__(self, right):
        subleft = self.__pos__()
        if type(right) != int or right<0:
            raise TypeError('Poly.__pow__:illegal argument type, the argument must be nonnegative int')
        if right == 0:
            return 1
        elif right == 1:
            return self
        else: 
            count = right -2
            npol = subleft*subleft
            while count != 0:
                npol = npol*subleft
                count -=1
            return npol

    def __eq__(self, pol):
        if type(pol) not in [Poly, int, float]:
            raise TypeError('Poly.__eq__:illegal argument type, the argument must be Poly')
        return str(self) == str(pol)

    
    def __lt__(self,right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__eq__:illegal argument type, the argument must be Poly')
        lefttup = sorted([(k, self.terms[k]) for k in self.terms], key = lambda x:x[0], reverse = True).pop(0)
        righttup = sorted([(k, right.terms[k]) for k in right.terms], key = lambda x:x[0], reverse = True).pop(0)
        return lefttup < righttup
    
    def __le__(self, right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__le__:illegal argument type, the argument must be Poly')
        lefttup = sorted([(k, self.terms[k]) for k in self.terms], key = lambda x:x[0], reverse = True).pop(0)
        righttup = sorted([(k, right.terms[k]) for k in right.terms], key = lambda x:x[0], reverse = True).pop(0)
        return lefttup <= righttup
    
    def __gt__(self, right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__gt__:illegal argument type, the argument must be Poly')
        return right<self
    
    def __ge__(self, right):
        if type(right) not in [Poly, int, float]:
            raise TypeError('Poly.__ge__:illegal argument type, the argument must be Poly')
        return right <= self
    
    
    def __setattr__(self, name, val):
        assert name == 'terms', 'Poly.__setattr__: illegal argument, you cannot reassign attributes'
        assert val != None, 'Poly.__setattr__: illegal argument, val cannot be None'
        self.__dict__[name] = val

if __name__ == '__main__':

    # Some simple tests; you can comment them out and/or add your own before
    # the driver is called.
    print('Start simple tests')
    p = Poly((3, 2), (-1, 1), (4, 0))
    print('  For Polynomial: 3x^2 - 2x + 4')
    print('  str(p):',p)
    print('  repr(p):',repr(p))
    print(' bool(p):', bool())
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
    