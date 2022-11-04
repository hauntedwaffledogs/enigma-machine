import random
import numpy as np
output = []
inputs = input('enter in plaintext: ')
seed = input('input a number 1 - 10: ')

for s in seed:
    s = ord(s)

for i in inputs:
    i = ord(i)
    i = i + s - 96
    output.append(i)



print(output)