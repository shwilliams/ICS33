import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i,l in enumerate(s.split('\n'),1):
            print('{num: >3} {text}'.format(num = i, text = l.rstrip()))
    
    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    
    def _is_legal_name(s):
        if type(s) != str:
            'not string'
            return False
        if not re.match(r'^([a-zA-Z])([\w_]*)$', s):
            'do not match'
            return False
        if s in keyword.kwlist:
            return False
        else:
            return True
    
    
    if not _is_legal_name(type_name):
        raise SyntaxError('pnamedtuple(type_name, field_names, mutable): illegal name, the type_name must be legal name')
    
    if type(field_names) not in [str, list]:
        raise SyntaxError('pnamedtuple(type_name, field_names, mutable): type(field_names) must be str or list')
        
    if type(field_names) == str:
        if field_names.find(',') > 0:
            field_list = [i.strip() for i in field_names.split(',')]
            
        elif field_names.find(' ') > 0:
            field_list = field_names.split(' ')
            
        else:
            raise SyntaxError('pnamedtuple(type_name, field_names, mutable): field_names must be separated by comma or space')
        if False in set(_is_legal_name(f) for f in set(field_list)):
            raise SyntaxError('pnamedtuple(type_name, field_names, mutable): illegal name, the field_names must consist of legal names')
                
    else:
        field_list = field_names
        if False in set(_is_legal_name(f) for f in field_names):
            print('not working')
            raise SyntaxError('pnamedtuple(type_name, field_names, mutable): illegal name, the field_names must be list of legal names')
    
    
    #__init__ method
    attr = '\n'
    for i in field_list:
        attr += '        self.{att} = {att}\n'.format(att = i)
    attr = attr[0:-1]
    class_definition = '''\
class {type_name}:  
    def __init__(self, {field_names}):{attribute}
        self._fields = {_fields}
        self._mutable = {mutable}

'''.format(type_name = type_name, field_names = ', '.join(field_list),attribute = attr, _fields = str(field_list), mutable = mutable)
    
    
    #__repr__method        
    repre = '''\
    def __repr__(self):
        return {type_name}({inside}'''.format(type_name ="'"+type_name, inside = ','.join([str(i)+'={'+str(i)+'}' for i in field_list]))+')'+"'"
         
    class_definition+= repre
    class_definition+= '.format('+','.join([str(i)+'='+'self.'+str(i) for i in field_list])+')\n'
    
    
    #get_ method
    get_method = ''
    for i in field_list:
        get_method+= '''\
    def get_{field}(self):
        return self.{field}

'''.format(field = i)
    class_definition += get_method
    
    
    #__getitem__ method
    getitem_method = '''\
    def __getitem__(self, p):
        field_index = [{fieldd}]
        if p in list(range(len(field_index))):
            return field_index[p]
        elif p in self._fields:
            return field_index[self._fields.index(p)]
        else:
            raise IndexError('{type_name}.__getitem__(self, p): p is out of bounds int or a string that does not name a field.')

'''.format(fieldd = ','.join('self.'+str(i) for i in field_list), type_name = type_name)
    class_definition += getitem_method
    
    
    #__eq__method
    eq_method = '''\
    def __eq__(self, right):
        if type(right) != {type_name}:
            return False
        else:
            return False if False in [self.__getitem__(i) == right.__getitem__(i) for i in self._fields] else True
            
'''.format(type_name = type_name)
    class_definition += eq_method
    
    
    #_replace method
    replace_method = '''\
    def _replace(self, **kargs):
        for key in kargs:
            if key not in self._fields:
                raise TypeError('{type_name}._replace(self, **kargs): key of kargs must be in self._fields')
        if self._mutable:
            for i in kargs.items():
                if i[0] in self.__dict__:
                    self.__dict__[i[0]] = i[1]
        else:
            for i in self._fields:
                if i not in kargs:
                    kargs[i] = self.__dict__[i]
        return {type_name}({inner})
            
'''.format(type_name = type_name, inner = ','.join(str(i)+'=kargs['+"'"+str(i)+"'"+']' for i in field_list))
    class_definition += replace_method
    # For initial debugging, always show the source code of the class
    show_listing(class_definition)
    
    # Execute the class_definition string in a local name_space and bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   show the error
    
      
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except (SyntaxError,TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]



if __name__ == '__main__':
    import driver
    driver.driver()
