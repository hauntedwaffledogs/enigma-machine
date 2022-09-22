import numpy as np
import string

alp = list(string.ascii_lowercase)

seed = 64876

encoder1 = np.random.choice(alp, size=24)

print(encoder1)


