'''
test on class. created on oct 30th
'''
global_var = 0

class C:
    class_var = 0
    
    def __init__(self, init_instance_var):
        self.instance_var = init_instance_var
    
    def bump(self, name):
        print(name, 'bumped')
        global global_var
        global_var += 1
        C.class_var += 1
        self.instance_var += 1
    
    def report(self, var):
        print('instance referred to by', var, 
              ':global_var = ', global_var, 
              '/class_var=', C.class_var,
              '/instance_var = ', self.instance_var)
        
x = C(10)
x.report('x')
x.bump('x')
x.report('x')
print()
print('y = x')
y = x
y.bump('y')
x.report('x')
y.report('y')
print()
C.report(x,'x')
type(x).report(x, 'x')
print()
print(C.class_var, x.class_var)
print(x.instance_var)