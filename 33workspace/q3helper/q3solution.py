import prompt,re
import math
from goody import type_as_str
from tkinter.constants import RIGHT

def expand_re(pat_dict:{str:str}):
    begin = [p for p,v in pat_dict.items() if not re.compile('#').search(v)][0]
    explored = [p for p in pat_dict.keys() if p != begin]
    
    while explored:
        for el in explored:
            if re.compile('#{}#'.format(begin)).search(pat_dict[el]):
                pat_dict[el] = re.compile('#{}#'.format(begin)).sub('({})'.format(pat_dict[begin]), pat_dict[el])
                begin = el
                explored.remove(el)
        
     
class Point:
    
    def __init__(self,x,y):
        if (type(x) != int or type(y) != int):
            raise AssertionError('Point.__init__(self, x, y) requires integer arguments')
        self.coords = (x, y)

    def __repr__(self):
        return 'Point({x},{y})'.format(x = self.coords[0], y = self.coords[1])


    def __str__(self):
        return '(x={x},y={y})'.format(x = self.coords[0], y = self.coords[1])

    
    def __bool__(self):
        if self.coords == (0, 0):
            return False
        else:
            return True
        

    def __add__(self,right):
        if type(right) != Point:
            raise TypeError('Point.__add__(self, right) requires Point object' )
        return Point(self.coords[0]+right.coords[0], self.coords[1]+right.coords[1])


    def __mul__(self,right):        
        if type(right) != int:
            raise TypeError('Point.__mul__(self, right) requires integer object' )
        return Point(self.coords[0]*right, self.coords[1]*right)

        
    def __rmul__(self,left):
        if type(left) != int:
            raise TypeError('Point.__rmul__(self, left) requires integer object' )
        return Point(self.coords[0]*left, self.coords[1]*left)
             
        
    def __lt__(self,right):
        if type(right) not in [int, float, Point]:
            raise TypeError('Point.__lt__(self, right) requires integer, float, or point object')
        distance = math.sqrt((self.coords[0]**2)+(self.coords[1]**2))
        if type(right) == Point:
            return distance < math.sqrt((right.coords[0]**2)+ (right.coords[1]**2))
        else:
            return distance < right
        

    def __getitem__(self,index):
        if type(index) not in [str, int] or index not in [0,1,'x','y']:
            raise IndexError('Point.__getitem__(self, index) requires 0, 1, {x}, {y}'.format(x ='x', y = 'y'))
        elif index in [0, 'x']:
            return self.coords[0]
        else:
            return self.coords[1]
        
        
    def __call__(self,x,y):
        if (type(x) != int or type(y) != int):
            raise AssertionError('Point.__call__(self, x, y) requires integer arguments')
        self.coords = (x, y)
        



from collections import defaultdict
class History:
    def __init__(self):
        self._history = defaultdict(list)
    
    def __getattr__(self,name):
        key = name[0:name.find('_prev')]
        if key not in self.__dict__:
            raise NameError('History.__getattr__(self, name) the name does not exist in dictionary')
        count = name.count('_prev')
        if count >= len(self._history[key]):
            return None
        return self._history[key][-count-1]
            

       
    def __setattr__(self,name,value):
        if name.find('_prev') >-1:
            raise NameError('History.__setattr__(self, name, value) the name argument cannot contain \'_prev\'')
        if '_history' in self.__dict__:
            self._history[name].append(value)
        self.__dict__[name] = value
     

    def __getitem__(self,name):
        if name > 0:
            raise IndexError('History.__getitem__(self,name) must have a non-positive name')
        return {key: (self._history[key][name-1] if -name < len(self._history[key]) else None) for key in self._history.keys()}



if __name__ == '__main__':
    
    if prompt.for_bool('Test expand?',True):
        pd = dict(digit=r'\d', integer=r'[=-]?#digit##digit#*')
        expand_re(pd)
        print('result =',pd)
        # produces and prints the dictionary {'digit': '\\d', 'integer': '[=-]?(\\d)(\\d)*'}
        
        pd = dict(integer       =r'[+-]?\d+',
                  integer_range =r'#integer#(..#integer#)?',
                  integer_list  =r'#integer_range#(?,#integer_range#)*',
                  integer_set   =r'{#integer_list#?}')
        expand_re(pd)
        print('result =',pd)
        # produces and prints the dictionary 
        # {'integer'      : '[+-]?\\d+',
        #  'integer_range': '([+-]?\\d+)(..([+-]?\\d+))?',
        #  'integer_list' : '(([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*',   
        #  'integer_set'  : '{((([+-]?\\d+)(..([+-]?\\d+))?)(?,(([+-]?\\d+)(..([+-]?\\d+))?))*)?}'
        # }
        
        pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
        expand_re(pd)
        print('result =',pd)
        # produces/prints the dictionary 
        # {'d': '(((correct)))',
        #  'c': '((correct))',
        #  'b': '(correct)',
        #  'a': 'correct',
        #  'g': '((((((correct))))))',
        #  'f': '(((((correct)))))',
        #  'e': '((((correct))))'
        # }
    
    import driver
    driver.driver()
