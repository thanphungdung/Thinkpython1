# def sum_all(*a):
#     return sum (a)


# print(sum_all(1,2,3))
import random
from this import d
t=['a','a','b']
def histogram (s):
    global d
    d =dict()
    for a in s:
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
    return d


def choose_from_hist(t):
    global d
    b=random.choice(t) 
    return b


print(choose_from_hist(t))
