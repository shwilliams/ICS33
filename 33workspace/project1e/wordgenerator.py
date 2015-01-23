# Submitter: bohyunk(Kim, Bohyun)
# Partner  : ablattle(Blattler, Albert)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict
from random import choice

def read_corpus(order:int, f):
    file = open(f, 'r')
    dic = defaultdict(list)
    word_list = [word for line in file for word in line.rstrip().split()]
    for i in range(0, len(word_list)-order):
        tup = tuple([word_list[k] for k in range(i, i+order)])
        if word_list[i+order] not in dic[tup]:
            dic[tup].append(word_list[i+order])
    
    return dic


def print_corpus(dic:dict):
    key_list = sorted([key for key in dic])
    val_list = sorted([v for k,v in dic.items()], key = lambda v: len(v))
    minval, maxval = len(val_list[0]), len(val_list[-1])
    print('Corpus')
    
    for key in key_list:
        print('    {key} can be followed by any of {val}'.format(key = key, val = dic[key]))
    print('min/max = {m}/{mm}'.format(m = minval, mm = maxval))
    

def produce_text(dic:dict, l:list, num:int)-> list:
    rlist = l.copy()
    size = len([k for k in dic][0])
    for i in range(0, num):
        tup = tuple(rlist[i:i+size])
        if tup in dic:
            new = choice(dic[tup])
            rlist.append(new)
        else:
            rlist.append(None)
    
    return rlist    
   
if __name__ == '__main__':
    order_stat = int(input('Enter order statistic: ').strip())
    file = input('Enter file to process: ').strip()
    corpus = read_corpus(order_stat, file)
    print_corpus(corpus)
    print()
    print('Enter {order} words to start with'.format(order = order_stat))
    requested_word = []
    
    for i in range(0, order_stat):
        word = input('Enter word {i}: '.format(i = i+1))
        requested_word.append(word)
    
    requested_number = int(input('Enter # of words to generate: '))
    text_list = produce_text(corpus, requested_word, requested_number)
    print('Random text = {list}'.format(list = text_list))           
    
