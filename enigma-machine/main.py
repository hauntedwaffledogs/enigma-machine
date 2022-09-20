import numpy as np
import string



#this makes the alphabet
alphabet = np.array(list(string.ascii_lowercase + ' '))

#Picks a random number between 97 and 122
x = np.random.randint(24, size=64)
RandomNumber = np.random.randint(111111, 999999)
seed = np.random.SeedSequence(RandomNumber)


#output
encoder = np.random.choice(alphabet, size=len(x))




print(encoder)