import numpy as np
import string



inputs = ord(input())
#plugboard settings

if inputs == 97:
    inputs = 100

if inputs == 102:
    inputs = 120

if inputs == 98:
    inputs = 110

if inputs == 99:
    inputs = 115


#rotors
def rotor(rotor):
    rotor = inputs+1


    rotor2 = rotor+1

    rotor3 = rotor2+1

    if rotor3 >= 122:
        rotor3 = rotor3 -26

    print(rotor3)
    print(chr(rotor3))

rotor(rotor)