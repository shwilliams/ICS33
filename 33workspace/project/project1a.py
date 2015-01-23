# Submitter: bohyunk(Kim, Bohyun)
# Partner  : ablattle(Blattler, Albert)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict
from goody       import safe_open



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

#print_graph(read_graph('graph1.txt'))

def reachable(dic: dict, snode: str)->set:
    result = set(snode)
    for item in dic[snode]:
        result.add(item)
        if item in dic:
            deeper = reachable(dic, item)
            for i in deeper:
                result.add(i)
            
                
    
    return result

print(reachable(read_graph('graph1.txt'),'e'))     
