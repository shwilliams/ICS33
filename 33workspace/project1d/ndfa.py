# Submitter: bohyunk(Kim, Bohyun)
# Partner  : ablattle(Blattler, Albert)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict


def read_ndfa(f):
    dic = defaultdict(list)
    file = open(f, 'r')
    
    for line in file:
        line_list = line.rstrip().split(';')
        value, state = line_list[1:-1:2], [k for k in line_list[2:len(line_list):2]]
        d = defaultdict(set)
        
        for i in range(0, len(value)):
            d[value[i]].add(state[i])
        fa_list = [(k,d[k]) for k in d]
        dic[line_list[0]] = (fa_list)
    
    return dic


def print_ndfa(dic: dict):
    print('Non-Deterministic Finite Automaton')
    
    for k in dic:
        print('    {k} transitions: {v}'.format(k = k, v = dic[k]))

        
def process(dic:dict, sstate:str, l:list)-> list:
    rlist = [sstate]
    explored = l.copy()
    state = {sstate}
    
    while explored:
        for value in l:
            key_tup = [k for v in state for k in dic[v]]
            key = [item for tup in key_tup for item in tup]
            
            if value in key:
                next_state = [items[1] for new_state in state for items in dic[new_state] if items[0] == value]
                union = {i for k in next_state for i in k}
                rlist += [(value, union)]
                state = union
            explored.remove(value)
    
    return rlist        


def interpret(l:list):
    print('Start state = {sstate}'.format(sstate = l.pop(0)))
    for tup in l:
        print('    Input = {inn}; new possible states = {nstate}'.format(inn = tup[0], nstate = tup[1]))
    print('Stop state(s) = {key}'.format(key = tup[1]))
    
    
if __name__ == '__main__':
    file = input('Enter file with non-deterministic finite automaton: ').strip().lower()
    print()
    ndfa = read_ndfa(file)
    print_ndfa(ndfa)
    print()
    ndfafile = open(input('Enter file with start-state and input: ').lower(), 'r')
    for line in ndfafile:
        print()
        print('Starting new simulation')
        ndfalist = line.rstrip().split(';')
        sstate = ndfalist.pop(0)
        interpret(process(ndfa, sstate, ndfalist))
        
    