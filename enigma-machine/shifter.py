text = open('transfer2.txt', 'r')
plTxt = [int(x) for x in str(text.readline())]
seed = open('seed1.txt', 'r')
elSeed = int(seed.readline())

text.close
seed.close



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shiftedLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shiftCounter = int()
shiftAmount = int(elSeed)
switchBack = int()

# Encrypting Shit \/\/\/\/

output = [(int(x) + shiftAmount) for x in str(text.readline())]

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

'''
def caeser():
    while timesShifted != len(plTxt):
        output[i] = shiftedLetters[(plTxt[i] - 1)]
        timesShifted += 1
        continue
    return output

caeser()
    '''
print(output)
print(plTxt)