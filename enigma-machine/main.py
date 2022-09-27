from re import X
import numpy as np
import string

x = "a"

reflector1 = ord(x)+3
reflector2 = reflector1+2
reflector3 = reflector2-10

print(chr(reflector3))