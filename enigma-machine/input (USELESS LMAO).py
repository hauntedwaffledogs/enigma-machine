encryptState = input('decrypt message, or encrypt message? (d/e): ')

while encryptState != True or False:
    if encryptState == 'd':
       print('Sorry, this function is not avalible yet')
       encryptState = input('decrypt message, or encrypt message? (d/e): ')
    else:
        if encryptState == 'e':
            encryptState = True

plTxt = input('Input your Message lowercase; letters only, no spaces, numbers or special characters: ')
seed = input('Input your first Seed numbers; Use only numbers, no letters or Special characters: ')




firstFile = open('transfer1.txt', 'w')
seed1File = open('seed1.txt', 'w')
firstFile.write(plTxt)
seed1File.write(seed)
firstFile.close
seed1File.close

if encryptState == True:
    print('To continue encryption, go to "string2numlist.py"')
else:
    print("YOU SHOULD'NT BE HERE YOU HERATIC")