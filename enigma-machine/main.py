import numpy as np
import string
#inputs = input()


def rotor(rotor):
    alphabet = list(string.ascii_lowercase)
    rotor1 = np.random.choice(alphabet, size=26)
    print(rotor1)

rotor(rotor)

