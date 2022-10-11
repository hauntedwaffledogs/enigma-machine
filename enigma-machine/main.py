import numpy as np
import string




inputs = ord(input())
print(inputs)
#plugboard settings

if inputs == 97:
    inputs = 100

if inputs == 102:
    inputs = 120

if inputs == 98:
    inputs = 110

if inputs == 99:
    inputs = 115

if inputs == 115:
    inputs = 99

if inputs == 111:
    inputs = 97


#rotors
def rotor(rotor):
    rotor = inputs+1


    rotor2 = rotor+1

    rotor3 = rotor2+1

    if rotor3 >= 122:
        rotor3 = rotor3 -26

    #reflection
    reflect = rotor3 +1
    reflect2 = reflect + 1
    reflect3 = reflect2 +1

    if reflect3 >= 122:
        reflect3 = 97

    print(reflect3)
    print(chr(reflect3))


rotor(rotor)
