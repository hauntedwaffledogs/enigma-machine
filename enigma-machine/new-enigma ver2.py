import numpy as np
import string
import random
#up to 512 characters

inputs = input()

output= [ord(inputs)-96 for inputs in inputs]
print(output)
