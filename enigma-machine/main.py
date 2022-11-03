import random
fart = random.randrange(1, 11)
inputs = input('message to encrypt: ')
for r in inputs:
    l = ord(r)
    g = l + fart
    op = chr(g)
    print(op)
fart = str(fart)
file1 = open('key1.txt', 'w')
file1.write(fart)
file1.close