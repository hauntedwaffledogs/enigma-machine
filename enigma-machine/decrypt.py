file1 = open('key1.txt', 'r')
x = file1.read()
ip = int(x)
output = []
inputs = input('enter in encrypted message: ')

for i in inputs:
    d = ord(i)
    peepeepoopoo = d - ip
    f = chr(peepeepoopoo)
    output.append(f)

print(output)