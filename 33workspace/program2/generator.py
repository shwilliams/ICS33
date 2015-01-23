# A generator for iterating through any iterable (mostly used to
#  iterate through the letters in a string).
# It is present and called to ensure that your generator code works on
#   general iterable parameters (not just on a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(lets(string)), so the generator functions you write should not
#   call len on their parameters

def lets(string):
    for i in range(len(string)):
        yield string[i]

def transform(iterable,f):
    for i in iterable:
        yield f(i)


def running_count(iterable,p):
    count = 0
    for i in iterable:
        if p(i):
            count += 1
        yield count

        
def n_with_pad(iterable ,n ,pad = None):
    iterat = iter(iterable)
    for i in range(n):
        try:
            yield next(iterat)
        except StopIteration:
            yield pad
            
        
def sequence(*args):
    for iterable in args:
        for i in iterable:
            yield i


def alternate(*args):
    it = []
    count = 0
    for i in args:
        it.append(iter(i))
        count+= 1
    subcount = 0
    while subcount < count:
        subcount = 0
        for i in it:
            try:
                yield next(i)
            except StopIteration:
                subcount +=1
                    


                
                
if __name__ == '__main__':
    import driver
    driver.driver()
