# Submitter: bohyunk(Kim, Bohyun)
# Partner  : ablattle(Blattler, Albert)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict

def read_fa(f):
    dic = defaultdict(set)
    file = open(f)
    for line in file:
        file_list = line.rstrip().split(';')
        value = file_list[1:-1:2]
        fa = file_list[2:len(file_list):2]
        finite_pair = list(zip(value, fa))
        dic[file_list[0]] = finite_pair
        
    return dic


def print_fa(dic: dict): 
    print('Finite Automaton')
    for key in dic:
        print('    {k} transition: {v}'.format(k = key, v = dic[key]))
         
def process(fa:dict, sstate:str, slist: list):
    rlist = [sstate]
    explored = slist.copy()
    state = sstate
    
    while explored:
        for element in slist:
            if element == 'x':
                rlist.append((element, None))
                explored.remove(element)
            else:
                for values in fa[state]:
                    if values[0] == element:
                        rlist.append((element, values[1]))
                        explored.remove(element)
                        state = values[1]

    return rlist

def interpret(l:list):
    sstate = l.pop(0)
    print('Start state = {s}'.format(s = sstate))
    for input in l:
        if input[0] == 'x':
            print('    Input = {inn}; illegal input: terminated'.format(inn = input[0]))
        else:
            print('    Input = {inn}; new state = {outt} '.format(inn = input[0], outt = input[1]))
        outt = input[1]
    print('Stop state = {outt}'.format(outt = outt))
    
if __name__ == '__main__':
    file = input('Enter file with finite automaton: ').lower()
    print()
    fa = read_fa(file)
    print_fa(fa)
    print()
    fafile = open(input('Enter file with start-state and input: ').lower(), 'r')
    for line in fafile:
        print()
        print('Starting new simulation')
        falist = line.rstrip().split(';')
        sstate = falist.pop(0)
        interpret(process(fa, sstate, falist))
        
    
    
    