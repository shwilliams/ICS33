'''
Created on Nov 8, 2014

@author: bohyunkim
'''
for i in range(1,6):
    print(i)
    break
else:
    print('executing else')
    
_hidden = iter(range(1,6))
try:
    while True:
        i = next(_hidden)
        print(i)
        break
except StopIteration:
    pass
    print('executing else')

alist = [5,2,8,3,5]
def abs_dif(iterable):
    answer = []
    i = iter(iterable)
    v2 = next(i)
    try:
        while True:
            v1, v2 = v2, next(i)
            answer.append(abs(v1 - v2))
    except StopIteration:
        pass
    return answer

print(abs_dif(alist))