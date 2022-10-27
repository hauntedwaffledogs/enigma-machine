import os
import os.path

encryptState = input('decrypt message, or encrypt message? (d/e): ')

usepreexistingseeds = False

seedcheck = ''

if encryptState == 'd':
    encryptState = False
else:
    if encryptState == 'e':
        encryptState = True

plTxt = input('Input your Message or the Message given to you; lowercase letters only, no spaces, numbers or special characters: ')
if os.path.exists('seed1.txt'):
    seedcheck = input('Would you like to create new seed files? (If not it will use the seed files that are saved in the directory)   [y/n?]: ')
else:
    print('No seed files found.')
    seed1 = input('Input your first Seed numbers; Use only numbers, no letters or Special characters: ')
    seed2 = input('Input your second Seed numbers: ')
    seed3 = input('Input your third Seed numbers: ')
    seed4 = input('Input your fourth Seed numbers: ')
    seed5 = input('Input your fifth Seed numbers: ')
    usepreexistingseeds = False

#to check if you used y/n only \/\/
while seedcheck != '':
    if seedcheck != 'y':
        if seedcheck != 'n':
            seedcheck = input('Would you like to create new seed files? (If not it will use the seed files that are saved in the directory)   [y/n?]: ')
        else:
            break
    else:
        if seedcheck != 'n':
            if seedcheck != 'y':
                seedcheck = input('Would you like to create new seed files? (If not it will use the seed files that are saved in the directory)   [y/n?]: ')
            else:
                break


if seedcheck == 'y':
    seed1 = input('Input your first Seed numbers; Use only numbers, no letters or Special characters: ')
    seed2 = input('Input your second Seed numbers: ')
    seed3 = input('Input your third Seed numbers: ')
    seed4 = input('Input your fourth Seed numbers: ')
    seed5 = input('Input your fifth Seed numbers: ')
if seedcheck == 'n':
    usepreexistingseeds = True


firstFile = open('transfer1.txt', 'w')
firstFile.write(plTxt)



if usepreexistingseeds == False:
    seed1File = open('seed1.txt', 'w')
    seed2File = open('seed2.txt', 'w')
    seed3File = open('seed3.txt', 'w')
    seed4File = open('seed4.txt', 'w')
    seed5File = open('seed5.txt', 'w')
    checkmarkFile = open('check.txt', 'w')

    seed1File.write(seed1)
    seed2File.write(seed2)
    seed3File.write(seed3)
    seed4File.write(seed4)
    seed5File.write(seed5)
    checkmarkFile.write('')

    seed1File.close
    seed2File.close
    seed3File.close
    seed4File.close
    seed5File.close
    checkmarkFile.close

    print('Seed files made! You can find them in the program directory')

if usepreexistingseeds == True:
    print('Using Prexisting seeds')



if encryptState == True:
    print('Go to firstLayerEN.py to Continue')
    import alphebetOrderScrambler
else:
    print('Go to firstLayerDE.py to Continue')
    import alphebetOrderScrambler