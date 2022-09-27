import numpy as np
import string


alp = list(string.ascii_lowercase)

encoder1 = np.random.choice(alp, size=64)

print(encoder1)