import numpy as np
import string


alp = list(string.ascii_lowercase)

encoder1 = np.random.choice(alp, size=24)
encoder2 = np.random.choice(alp, size=24)
encoder3 = np.random.choice(alp, size=24)

print(encoder1, encoder2, encoder3)

