# kargs example

print('Demonstrating how kargs works in functions')
def f(**kargs):
    # prints dict
    tup = tuple((i, kargs[i]) for i in kargs)
    print(tup)
    print(max(*tup))
    # raises exception
    # equivalent to calling print(a=1,b=2) order of arguments based on dict
    #d = dict(a=1,b=2)
    #print (**d)

#Call successfully (watch what is printed)
f(b=True,d=print)