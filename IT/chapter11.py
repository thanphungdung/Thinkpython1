# eng2vn = dict()

# eng2vn ={
#     'one ': 'mot',
#     'two' : 'hai',
#     'three' : 'ba',
#     'four':'bin',


# }

# print(eng2vn['three '])

def histogram(s):
    d=dict()
    for a in s :
        if a not in d :
            d[a]=1
        else:
            d[a]+=1
    return d

print(histogram('banana'))




def invert_dict(d):
   inverse = dict()
   for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
   return inverse

print(invert_dict('banana'))



     

