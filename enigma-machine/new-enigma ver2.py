import numpy as np
#up to 512 characters
plaintext = input()


for i in range(0, len(plaintext)):
    code = ord(plaintext[i])
    c = code +4
    print(c)


