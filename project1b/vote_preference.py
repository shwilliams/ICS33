# Submitter: bohyunk(Kim, Bohyun)
# Partner  : ablattle(Blattler, Albert)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict
from test.test_importlib.test_util import SetLoaderTests

NONE = None

def read_voter_preferences(given_file: str):
    file = open(given_file, 'r')
    dic = defaultdict(list)

    for line in file:
        text = line.rstrip()
        text = text.split(';')
        key = text[0]
        for i in range(1,4):
            dic[key].append(text[i])
    
    return dic

def print_dict(title:str, dic: dict, f= None, b = False):
    new = sorted(dic, key = f)
    print(title)
    if b == True:
        new = reversed(sorted(dic, key = f))
    for item in new:
        print('{k}-> {v}'.format(k = item, v = dic[item]))
        
def evaluate_ballot(dic: dict, s: set):
    ndic = defaultdict(int)
    voter, voted = {k for k in dic}, set()
    
    for person in voter:
        for pref in dic[person]:
            if pref in s:
                if person not in voted:
                    if pref not in ndic:
                        ndic[pref] = 0
                    ndic[pref] += 1
                    voted.add(person)
    return ndic

def remaining_candidates(dic: dict):
    s = {k for k in dic}
    for k in dic:
        if dic[k] == min(dic.values()):
            s.remove(k)
            
    return s

def decide_winner(s:set):
    if len(s) >= 2:
        return NONE
    else:
        return s
    
if __name__ == '__main__':
    file = 'votepref1.txt'#input('Enter file with voter preferences: ').lower()
    mydic = read_voter_preferences(file)
    print_dict('Voter Preferences', mydic)
    winner = NONE
    count = 0
    remained_candidates = {c for c in 'XYZ'}
    
    while winner == NONE:
        count += 1
        evaluated = evaluate_ballot(mydic, remained_candidates)
        print()
        print_dict('Vote count on ballot #{c} with candidates (alphabetically)'.format(c = count),
                   evaluated)
        print()
        print_dict('Vote count on ballot #{c} with candidates (numerically)'.format(c = count),
                   evaluated, evaluated.get)
        remained_candidates = remaining_candidates(evaluated)
        winner = decide_winner(remained_candidates)
    
    print()
    print('Winner is {w}'.format(w = winner))