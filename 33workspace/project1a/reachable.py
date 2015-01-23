# Submitter: bohyunk(Kim, Bohyun)
# Partner  : ablattle(Blattler, Albert)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict

###Functions used in main script
def read_graph(given_file:str) -> dict:
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


def valid_start_node(dic: dict, snode: str)->bool:
    if snode not in dic:
        return False  
    else:
        return True 


###Here is the main script
if __name__ == '__main__':
    file = input('Enter file with graph: ').lower()
    graph = read_graph(file)
    print()
    print_graph(graph)
    print()
    snode = input('Enter starting node: ').lower()
    
    while snode != 'quit':
        if valid_start_node(graph, snode):
            reachable_nodes = reachable(graph, snode)
            print('From {node} the reachable nodes are {reachable}'.format(node = snode, reachable = reachable_nodes ))
            print()
            snode = input('Enter starting node: ').lower()
        else:
            print('    Entry Error: '+snode+';  Not a source node')
            print('    Please enter a legal String')
            print()
            snode = input('Enter starting node: ').lower()