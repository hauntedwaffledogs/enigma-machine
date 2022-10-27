
cock = open('transfer2.txt', 'r')
plaintext = cock.read()

text2numoutput = [ord(plaintext)-96 for plaintext in plaintext]



for i in text2numoutput:
    if i < 0 or i > 26:
        text2numoutput.remove(i)
        break
    else:
        continue


#file delete shit \/\/\/

cock.close



seed = open('seed2.txt', 'r')
elSeed = int(seed.readline())
seed.close

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shiftedLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shiftCounter = int()
shiftAmount = int(elSeed)
switchBack = int()

# Encrypting Shit \/\/\/\/

output = text2numoutput.copy()

if shiftAmount > 26:
    while shiftAmount > 26:
        shiftAmount = shiftAmount - 26
        if shiftAmount in range(len(letters)):
            break
    
for i in shiftedLetters:
    if (shiftCounter + shiftAmount) >= 26:
        switchBack = 26
    else:
        switchBack = 0
    shiftedLetters[shiftCounter] = letters[(shiftCounter + (shiftAmount - switchBack))]
    shiftCounter = shiftCounter + 1
    #print(shiftedLetters[(shiftCounter - 1)])
    if shiftCounter == 26:
        break
    else:
        continue

sCounter = int(0)

msgLength = len(text2numoutput)

while sCounter < msgLength:
    output[sCounter] = shiftedLetters[(text2numoutput[sCounter] - 1)]
    sCounter = sCounter + 1
    if not sCounter >= msgLength:
        continue
    else:
        sCounter == 0
        break
        

tumblr = ''.join(str(e) for e in output)

outputfile = open('transfer3.txt', 'w')
outputfile.write(tumblr)
outputfile.close