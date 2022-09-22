import numpy as np
import string

input = input()

alp = list(string.ascii_lowercase) 

encoder1 = np.random.choice(alp, size=64)

print(encoder1)


