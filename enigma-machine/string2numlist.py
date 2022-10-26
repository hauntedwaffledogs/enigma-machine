#up to 512 characters

inputs = str(input('Plaintext (lowercase characters only, no spaces): '))

output= [ord(inputs)-96 for inputs in inputs]
print(output)