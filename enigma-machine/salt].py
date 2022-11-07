import string
import random
import base64
inputs = input()
output = []

for i in inputs:
    output.append(i)

g = string.ascii_letters

for p in g:
    r = random.choice(g)
    output.append(r)

foutput = ''.join(output)

encode1 = foutput.encode("ascii")
encode2 = base64.a85encode(encode1)
print(encode2)