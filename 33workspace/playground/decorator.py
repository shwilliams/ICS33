class Trace:
    def __init__(self,f,f_name):
        self.f = f
        self.f_name = f_name
        
    def __call__(self,*args,**kargs):
        result = self.f(*args,**kargs)
        print(self.f_name+'called: '+str(result))
        return result

