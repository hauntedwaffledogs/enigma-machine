import numpy as np
import string

#this makes the alphabet
alphabet = np.array(list(string.ascii_lowercase + ' '))

#Picks a random number between 97 and 122
x = np.random.randint(97, 122, size=64)


#output
print(np.random.choice(alphabet, size=len(x)))