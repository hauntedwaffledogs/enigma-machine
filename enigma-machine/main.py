import random
fart = random.randrange(1, 10)

inputs = input('message to encrypt: ')

output = []


for i in inputs:
    x = ord(i)
    y = x +fart
    output.append(y)
print(output)

fart = str(fart)
file1 = open('key1.txt', 'w')
file1.write(fart)
file1.close


for x in output:
    pp = chr(x)
    print(pp)