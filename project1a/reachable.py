# Submitter: bohyunk(Kim, Bohyun)
# Partner  : ablattle(Blattler, Albert)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict


def read_graph(given_file:str) -> dict:
    '''reads a file and create a graph dictionary'''
    ndict = defaultdict(set)
    file = open(given_file, 'r') 
    
    for line_number, text in enumerate(file,1):
        text = text.rstrip().lower()
        if len(text) != 0:
            reach = text.split(';')
            key, value = reach[0], reach[1]
            ndict[key].add(value)
    
    return ndict

def print_graph(dic: dict)-> None:
    print('Graph: source -> {destination} edges')
    for node, reach in sorted(dic.items()):
        print( ('{node}:-> '+'{reach}').format(node=node,reach=reach))

def reachable(dic: dict, snode: str)->set:
    
    explore = set(snode)
    visited = set()

    while explore:
        node = explore.pop()
        if node not in visited:
            visited.add(node)
            for next in dic[node]:
                explore.add(next)
    
    return visited
        
