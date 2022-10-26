cock = open('transfer1.txt', 'r')
plaintext = cock.readline()
seed = int(cock.readline())

txtoutput = [ord(plaintext)-96 for plaintext in plaintext]
numoutput = seed



for i in txtoutput:
    if i < 0 or i > 26:
        txtoutput.remove(i)
        break
    else:
        continue

jesseweneedtocook = [str(integer) for integer in txtoutput]
waltawhite = "".join(jesseweneedtocook)
skylerwhiteyo = str(waltawhite)
gustavofring = str(numoutput)

secondFile = open('transfer2.txt', 'w')
secondFile.write(skylerwhiteyo+'\n')
secondFile.write(gustavofring)
secondFile.close