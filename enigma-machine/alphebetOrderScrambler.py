import os
import os.path


for i in range(5):
    while os.path.exists('check.txt'):
        seed = open('seed4.txt', 'r')

        elSeed = int(seed.read())
        
       
        


        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        shiftedLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        shiftCounter = int()
        shiftAmount = int(elSeed)
        switchBack = int()


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

        dec = open('seed5.txt', 'r')

        layerToBeginOn = int(dec.read())

        if layerToBeginOn > 3:
            while layerToBeginOn > 3:
                layerToBeginOn = layerToBeginOn - 3
                if layerToBeginOn in range(3):
                    break



        output = shiftedLetters.copy()
        tumblr = ''.join(str(e) for e in output)

        newOrder = open('scrambler.txt', 'w')
        newOrder.write(tumblr)
        newOrder.close

        whenShould = open('seed5.txt', 'w')
        whenShould.write(str(layerToBeginOn))
        whenShould.close
        
        break
    else:
        continue

