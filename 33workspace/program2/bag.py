from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self, l=None):
        self.bag = defaultdict(int)
        if l!= None:
            for el in l:
                self.bag[el] +=1
        self.initial = l
    
    def __repr__(self):
        if self.bag == {}:
            return 'Bag()'
        else:
            return 'Bag('+str([k for k in self.bag for i in range(self.bag[k])])+')'
            
    def __str__(self):
        if self.bag == {}:
            return 'Bag()'
        else:
            return 'Bag('+''.join (i for i in[str(k)+str([self.bag[k]]) for k in self.bag])+')'
        
    def __len__(self):
        return sum([i for i in self.bag.values()])
    
    
    def unique(self):
        return len({i for i in self.bag.keys()})
    
    
    def __contains__(self, el):
        return el in self.bag
    
    def count(self, el):
        if el not in self:
            return 0
        else:
            return self.bag[el]
        
    def add(self, el):
        if el not in self:
            self.bag[el] = 1
        else:
            self.bag[el] +=1
            
    
    def remove(self,el):
        if el not in self:
            raise ValueError('Bag.remove: illegal argument, the argument is not in bag')
        self.bag[el] -= 1
        self.bag = {k: self.bag[k] for k in self.bag if self.bag[k]>0}
        
    def __eq__(self, right):
        if type(right) !=Bag:
            raise TypeError('Bag.__eq__: illegal argument type, the type of the argument must be Bag')
        return self.bag == right.bag
    
    def __ne__(self, right):
        if type(right) !=Bag:
            raise TypeError('Bag.__ne__: illegal argument type, the type of the argument must be Bag')
        return self.bag != right.bag
    
    def __iter__(self):
        elbag = [k for k in self.bag for i in range(self.bag[k])]
        def bag_element(max, l):
            p = 0
            while p<= max-1:
                yield l[p]
                p+=1
        return bag_element(len(elbag), elbag)
            
        
        
    
    
        
#b = Bag(['d','a','b','d','c','b','d'])
#print(b.count('d'))
#print(b.add('d'))
#print(b.bag)
#print(str(b))
    
if __name__ == '__main__':
    import driver
    driver.driver()   
