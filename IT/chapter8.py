
i =3 
a=fruit [i]
print(a)


last = fruit[len(fruit)-1]
print(last)

fruit = input('fill in the gap pls:')
def call(fruit):
    
    index = len(fruit)-1

    while index > -1:
        letter = fruit[index]
        print (letter)
        index = index -1

print(call(fruit))    

for letter in fruit:
    print(letter)


prefixes = 'JKLMNOPQ'
suffix = 'ack'
a= 'uack'
for letter in prefixes :
    if letter == prefixes[7] :
        print (letter + a)
    elif letter == prefixes[5]:
        print (letter +a)
    else:
        print(letter+ suffix)

word = input(' dien tu di be: ')
letter = input('?')



def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index +1

    else:
            return -1

print(find('watermelon', 'e'))

def in_both(a,b):
    for letter in a:
        if letter in b:
            print(letter)

print(in_both('apple', 'orange'))







