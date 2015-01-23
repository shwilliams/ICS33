'''
Created on Nov 17, 2014

@author: bohyunkim
'''
class Triple1:  
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._fields = ['a', 'b', 'c']
        self._mutable = False

    def __repr__(self):
        return 'Triple1(a={a},b={b},c={c})'.format(a=self.a,b=self.b,c=self.c)
    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def __getitem__(self, p):
        field_index = [self.a,self.b,self.c]
        if p in list(range(len(field_index))):
            return field_index[p]
        elif p in self._fields:
            return field_index[self._fields.index(p)]
        else:
            raise IndexError('Triple1.__getitem__(self, p): p is out of bounds int or a string that does not name a field.')

    def __eq__(self, right):
        if type(right) != Triple1:
            return False
        else:
            return False if False in [self.__getitem__(i) == right.__getitem__(i) for i in self._fields] else True
            
    def _replace(self, **kargs):
        if self._mutable:
            for i in kargs.items():
                if i[0] in self.__dict__:
                    self.__dict__[i[0]] = i[1]
        else:
            for i in self._fields:
                if i not in kargs:
                    kargs[i] = self.__dict__[i]
            return Triple1(a=kargs['a'], b=kargs['b'], c=kargs['c'])
    
t1 = Triple1(a=1,b=2,c=3)
print(t1.__dict__)
t2 =t1._replace(a=2)
print(t2.__dict__)