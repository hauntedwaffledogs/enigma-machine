letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

originalText = ""
mainSeed = int()

print("Input Plaintext")
input(originalText)

print("Input Seed, Use Numbers")
input(mainSeed)

# Encrypting Shit \/\/\/\/

def caeser(PlTxt, Seed):
    shiftAmount = (PlTxt + Seed)


caeser(originalText, mainSeed)
    
while (shiftAmount > 26):
    shiftAmount = shiftAmount - 26
else:
    returnText = 
