# Tracking (counting) function calls as decorator class/function

class Track_Calls:
    def __init__(self,f):
        self.f = f
        self.calls = 0
    
    def __call__(self,*args,**kargs):  # bundle arbitrary arguments
        self.calls += 1
        return self.f(*args,**kargs)   # unbundle arbitrary arguments

    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)
    

def track_calls(f):
    def call(*args,**kargs):
        call.calls += 1
        return f(*args,**kargs)

    call.calls = 0
    return call



# Memoizing function calls as decorator class/function

class Memoize:
    def __init__(self,f):
        self.f = f
        self.cache = {}
        
    def __call__(self,*args):
        if args in self.cache:
            return self.cache[args]
        else:
            answer = self.f(*args)
            self.cache[args] = answer
        return answer

    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)


def memoize(f):
    cache = {}
    def wrapper(*args):
        if args in cache: 
            return cache[args]
        else:
            answer = f(*args)
            cache[args] = answer
        return answer
    return wrapper



# Illustrating the recursive structure (calls/returns) of recursive functions

class Illustrate_Recursive:
    def __init__(self,f):
        self.f = f
        self.trace = False
        
    def illustrate(self,*args,**kargs):
        self.indent = 0
        self.trace = True
        answer = self.__call__(*args,**kargs)
        print('answer returned')
        self.trace = False
        return answer
    
    def __call__(self,*args,**kargs):
        if self.trace:
            if self.indent == 0:
                print('Starting recursive illustration'+30*'-')
            print (self.indent*"."+"calling", self.f.__name__+str(args)+str(kargs))
            self.indent += 2
        answer = self.f(*args,**kargs)
        if self.trace:
            self.indent -= 2
            print (self.indent*"."+self.f.__name__+str(args)+str(kargs)+" returns", answer)
            if self.indent == 0:
                print('Ending recursive illustration'+30*'-')
        return answer

    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)

if __name__ == '__main__':
    @Illustrate_Recursive
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    
    print('Illustrating recursive factorial')    
    factorial.illustrate(5)     # For Illustrate_Recursive
    
    
    
    # Use any combination (in any order) of Decorators (see __getattr__)
    
    @Memoize
    @Illustrate_Recursive
    @Track_Calls
    def fib(n):
        assert n>=0, 'fib cannot have negative n('+str(n)+')'
        if    n == 0: return 1
        elif  n == 1: return 1
        else:         return fib(n-1) + fib(n-2)
    
    print('Illustrating recursive fib(onacci)')    
    fib.illustrate(5)           # For Illustrate_Recursive
    print('Tracking calls for recursive fib(onacci)')    
    fib(10)                     # for Track_Calls
    print('Calls for fib(10) is',fib.calls)
    
    
    
    # Examining/manipulating recursion depth
    
    import sys 
    print('Showing manipulation of sys. get/set recurssion limit')
    print('Current recursion limit =',sys.getrecursionlimit())
    sys.setrecursionlimit(5000)
    print('Current recursion limit =',sys.getrecursionlimit())
    
