letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shiftedLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shiftCounter = int()
shiftAmount = int(input('Seed: '))
switchBack = int()
# RE ADD THESE (anything with > ##) INTO CODE ONCE FUNCTION AND OTHER SHIT WORKS \/\/\/\/\/

##plainText = input('Input Text (Lowercase Only, No Special Charactes or Spaces): ')

# Encrypting Shit \/\/\/\/

def caeser(PlTxt, Seed):
    shiftAmount = Seed
    return shiftAmount

caeser(0, 0)
    
if shiftAmount > 26:
    while shiftAmount > 26:
        shiftAmount = shiftAmount - 26
        #print(shiftAmount)
        if shiftAmount in range(len(letters)):
            break
    
for i in shiftedLetters:
    if (shiftCounter + shiftAmount) >= 26:
        switchBack = 26
    else:
        switchBack = 0
    shiftedLetters[shiftCounter] = letters[(shiftCounter + (shiftAmount - switchBack))]
    shiftCounter = shiftCounter + 1
    print(shiftedLetters[(shiftCounter - 1)])
    if shiftCounter == 26:
        break
    else:
        continue
