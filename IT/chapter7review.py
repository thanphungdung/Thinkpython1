def countdown(n):
    while n>0:
        print(n)
        n=n-1
    print('blastoff')

print(countdown(5))

def print_n(s,n):
    while n <=0:
       return
    else:
        print(s)
        print_n(s,n-1)

print(print_n('yee',4))
