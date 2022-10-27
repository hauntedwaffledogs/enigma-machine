encryptState = input('decrypt message, or encrypt message? (d/e): ')


if encryptState == 'd':
    encryptState = False
else:
    if encryptState == 'e':
        encryptState = True

plTxt = input('Input your Message or the Message given to you; lowercase letters only, no spaces, numbers or special characters: ')
seed1 = input('Input your first Seed numbers; Use only numbers, no letters or Special characters: ')
seed2 = input('Input your second Seed numbers: ')
seed3 = input('Input your final Seed numbers: ')


firstFile = open('transfer1.txt', 'w')
seed1File = open('seed1.txt', 'w')
seed2File = open('seed2.txt', 'w')
seed3File = open('seed3.txt', 'w')
firstFile.write(plTxt)
seed1File.write(seed1)
seed2File.write(seed2)
seed3File.write(seed3)
firstFile.close
seed1File.close
seed2File.close
seed3File.close

if encryptState == True:
    print('To continue encryption, go to "firstLayerEN.py"')
else:
    print('"To continue encryption, go to "firstLayerDE.py"')