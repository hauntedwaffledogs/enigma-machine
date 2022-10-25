switchBack = int()
# RE ADD THESE (anything with > ##) INTO CODE ONCE FUNCTION AND OTHER SHIT WORKS \/\/\/\/\/

##print("Input Plaintext")
##input(originalText)

##print("Input Seed, Use Numbers")
##input(mainSeed)

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
