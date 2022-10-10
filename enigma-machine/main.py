import numpy as np
import string
#inputs = input()
seed = 64254

def rotor(rotor):
    alphabet = list(string.ascii_lowercase)
    rotor1 = np.random.choice(alphabet, size=26)
    a = str(rotor1)
    print(a)

rotor(rotor)

