from goody import type_as_str
import inspect


class Check_All_OK:
    """
    Check_All_OK implements __check_annotation__ by checking whether every
      annotations passed to its constructor are OK; the first one that
      fails (raises AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (raise AssertionError) this classes raises AssertionError and prints its
      failure, along with a list of all annotations tried followed by the check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self.checking_on = True
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        def formated_message(a,v,p, message='wrong type'):
            if message == 'wrong type':
                return '{param} failed annotation check({message}): value = {value} was type {value_type} ...should be type {annot_type}'.format(message = message, param = str(format_str(p)), value = str(format_str(v)), value_type = str(type(v)), annot_type = str(a))    
            elif message == 'wrong number of elements':
                return '{param} failed annotation check({message}): value = {value} annotation had {numel} elements {annot}'.format(message = message, numel = str(len(a)), param = str(format_str(p)), value = str(v), annot = str(a))
            elif message == 'annotation inconsistency':
                return '{param} {message}: {annot_type} should have 1 item but had {numel} annotation = {annot}'.format(message = message, numel = str(len(a)), annot_type = str(type(a)), annot = a, param = str(format_str(p)))
        
        def format_str(x):
            return "'"+x+"'" if type(x) == str else x
        if annot == None:
            pass       
        elif annot == int:
            assert isinstance(value, int), formated_message(annot, value, param)
        elif annot == str:
            assert isinstance(value, str), formated_message(annot, value, param)
        elif annot == float:
            assert isinstance(value, float), formated_message(annot, value, param)
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #listcase
        elif annot == list:    
            assert isinstance(value, list), formated_message(annot, value, param)
        elif type(annot) == list: 
            assert isinstance(value, list), formated_message(list,value, param) 
            if len(annot) == 1:
                for val in value:
                    self.check(param, annot[0], val)
            elif len(annot) >1:
                assert len(annot) == len(value), formated_message(annot,value,param, message='wrong number of elements')
                for i in range(len(annot)):
                    self.check(param, annot[i], value[i])
        
        #tuplecase
        elif annot == tuple:
            assert isinstance(value, tuple), formated_message(annot,value,param)
        elif type(annot) == tuple:
            assert isinstance(value, tuple), formated_message(tuple, value, param)
            if len(annot) == 1:
                for val in value:
                    self.check(param, annot[0], val)
            elif len(annot) >1:
                assert len(annot) == len(value), formated_message(annot,value,param, message='wrong number of elements')
                for i in range(len(annot)):
                    self.check(param, annot[i], value[i])
        #dictionarycase
        elif annot == dict:
            assert isinstance(value, dict), formated_message(annot, value, param)
        elif type(annot) == dict:
            assert isinstance(value, dict), formated_message(dict, value, param)
            assert len(annot.keys())<=1 ,formated_message(annot,value,param, message='annotation inconsistency') 
            ke, it = list(annot.items())[0]
            for k,v in value.items():
                self.check(param, ke, k)
                self.check(param, it, v)
        #setcase
        elif annot == set:
            assert isinstance(value, set), formated_message(annot, value, param)
        elif type(annot) == set:
            assert isinstance(value, set), formated_message(set, value, param)
            assert len(annot) <=1, formated_message(annot,value,param, message='annotation inconsistency')
            checker = annot.pop()
            for i in value:
                self.check(param, checker, i)
        
        #frozensetcase
        elif annot == frozenset:
            assert isinstance(value, frozenset), formated_message(annot, value, param)
        elif type(annot) == frozenset:
            assert isinstance(value, frozenset), formated_message(frozenset, value, param)
            assert len(annot) <=1, formated_message(annot,value,param, message='annotation inconsistency')
            checker = next(iter(annot))
            for i in value:
                self.check(param, checker, i)
                
        #lambdacase
        elif inspect.isfunction(annot):
            assert len(annot.__code__.co_varnames) == 1,'{param} annotation inconsistency: predicate should have 1 parameter but had {numel} predicate = {annot}'.format(param = format_str(param), numel = str(len(annot.__code__.co_varnames)), annot = str(annot))
            try:
                a = annot(value)
            except Exception as exe:
                raise AssertionError('{param} annotation predicate({annot}) raised exception = {error_type}: {err_message})'.format(param = format_str(param), annot = str(annot), error_type = (str(type(exe))), err_message = str(exe)))
            assert a, '{param} failed annotation check: value = {value} predicate = {annot}'.format(param = str(format_str(param)), value = str(value), annot = str(annot))
            
        else:
            try:
                annot.__check_annotation__(self.check, param, value, check_history)
            except AttributeError:
                raise AssertionError('{param} annotation undecipherable: {annot}'.format(param = str(format_str(param)), annot = str(annot)))
            except AssertionError as exx:
                raise exx
            except Exception as exxe:
                raise AssertionError('{param} annotation predicate({annot}) raised exception = {error_type}: {err_message})'.format(param = format_str(param), annot = str(annot), error_type = (str(type(exxe))), err_message = str(exxe)))
            
            
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Decode annotation and check it  
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs): 
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if self.checking_on == False or Check_Annotation.checking_on == False:
            answer = self._f(*args,**kargs)
            return answer
        
        annot_dict = self._f.__annotations__
        value_dict = param_arg_bindings()
        try:
            # Check the annotation for every parameter (if there is one)
            for keys in annot_dict.keys():
                if keys != 'return':
                    self.check(keys, annot_dict[keys],value_dict[keys])
            # Compute/remember the value of the decorated function
            answer = self._f(*args, **kargs)
            # If 'return' is in the annotation, check it
            if 'return' in annot_dict:
                value_dict['_return'] = answer
                self.check('return', annot_dict['return'],answer)
            # Return the decorated answer
            return answer
            #remove after adding real code in try/except
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError as ex:
            #print(80*'-')
            #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
             #   print(l.rstrip())
            #print(80*'-')
            raise ex
        



 
if __name__ == '__main__':   
    #from bag import Bag  
    # an example of testing a simple annotation  
    #def f(x : int) -> str: return 0
    #f = Check_Annotation(f)
    #f(2)
    
    import driver
    driver.default_show_comment           = True
    driver.default_show_traceback         = True
    driver.default_show_exception         = True
    driver.default_show_exception_message = True
    driver.driver()
    