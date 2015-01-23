from functools import reduce # for code_metric
from predicate import is_less_than
from lib2to3.pgen2.token import LESS, GREATER


def separate(p,l):
    truelist = []
    falselist = []
    if l == []:
        return (truelist,falselist)
    else:
        truelist, falselist = separate(p, l[1:])
        if p(l[0]):
            truelist = [l[0]]+truelist
        else:
            falselist = [l[0]]+falselist
        return (truelist,falselist)
        

def is_sorted(s):
    if s == []:
        return True
    if len(s) == 1:
        return True
    else:
        return s[0]<s[1] and is_sorted(s[1:])   

  
def sort(l):
    sorted_list = []
    
    def leq(i):
        def leeq(x): 
            return x<=i
        return leeq
    
    current_node = l.pop(0)
    sorted_list.append(current_node)
    les, gre = separate(leq(current_node), l)
    
    if len(les) == 0 and len(gre) == 0:
        return les+sorted_list+gre
    else:
        return sorted(les)+sorted_list+sorted(gre)
        
        
def compare(a,b):
    if a == '' and b == '':
        return '='
    elif a == '' and b!= '':
        return '<'
    elif a != '' and b == '':
        return '>'
    else:
        if a[0] > b[0]:
            return '>'
        elif a[0] < b[0]:
            return '<'
        else:
            return compare(a[1:], b[1:])
    

def code_metric(file):
    f = open(file, 'r')
    l = map(lambda x: (1,x), filter(lambda x: x !=0 ,map(lambda x:len(x.rstrip()), f))) 
    return reduce(lambda x,y: (x[0]+y[0],x[1]+y[1]), l)





if __name__=="__main__":
    import predicate,random,driver
    from goody import irange
    
    driver.driver() # type quit in driver to return and execute code below

    print('Testing separate')
    print(separate(predicate.is_positive,[]))
    print(separate(predicate.is_positive,[1, -3, -2, 4, 0, -1, 8]))
    print(separate(predicate.is_prime,[i for i in irange(2,20)]))
    print(separate(lambda x : len(x) <= 3,'to be or not to be that is the question'.split(' ')))
    
    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))
    
    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = [i+1 for i in range(30)]
    random.shuffle(l)
    print(l)
    print(sort(l))
    
    print('\nTesting sort')
    
    print('\nTesting compare')
    print(compare('','abc'))
    print(compare('abc',''))
    print(compare('',''))
    print(compare('abc','abc'))
    print(compare('bc','abc'))
    print(compare('abc','bc'))
    print(compare('aaaxc','aaabc'))
    print(compare('aaabc','aaaxc'))
    
    print('\nTesting code_metric')
    print(code_metric('cmtest.py'))
    print(code_metric('collatz.py'))
    print(code_metric('q5solution.py'))  # A function analyzing the file it is in
