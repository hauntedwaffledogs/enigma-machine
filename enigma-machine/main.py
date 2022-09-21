import numpy as np
import string

#Picks a random number between 97 and 122
x = np.random.randint(24, size=64)

#output
encoder = np.random.choice(x, size=len(x))

print(encoder)