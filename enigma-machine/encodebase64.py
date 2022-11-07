import string
import random
import base64
seed = input("Seed: ")
plTxt = input("Plaintext: ")
seedAmount = int(seed)

ascii = string.ascii_letters
output = []

while seedAmount > 0:
    r = random.choice(ascii)
    output.append(r)
    seedAmount -= 1


for i in plTxt:
    output.append(i)



for i in ascii:
    r = random.choice(ascii)
    output.append(r)




joinedoutput = ''.join(output)

encode1 = joinedoutput.encode("ascii")
encode3 = base64.a85encode(encode1)
encode3 = encode3.decode('ascii')

print(encode3)