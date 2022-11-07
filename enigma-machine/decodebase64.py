import base64

saltRemover = []
seed = input("Seed: ")
input = input("Text: ")
seedAmount = int(seed)
r = int(0)

decode = base64.a85decode(input)
decode = decode.decode('ascii')

for i in decode:
    saltRemover.append(i)


while seedAmount > 0:
    del saltRemover[0]
    seedAmount = seedAmount - 1



output = ''.join(saltRemover)
print(output)