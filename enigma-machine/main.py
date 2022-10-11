import numpy as np
import string
plugboard=ord(input())

def rotor(rotor):
    rotor = plugboard+1


    rotor2 = rotor+1

    rotor3 = rotor2+1

    if rotor3 >= 122:
        rotor3 = rotor3 -26

    print(chr(rotor3))



rotor = rotor(rotor)
