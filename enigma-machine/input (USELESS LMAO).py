plTxt = input('Input your Message lowercase; letters only, no spaces, numbers or special characters: ')
seed = input('Input your first Seed numbers (Use only numbers, no letters or Special characters): ')


firstFile = open('transfer1.txt', 'w')
seed1File = open('seed1.txt', 'w')
firstFile.write(plTxt)
seed1File.write(seed)
firstFile.close
seed1File.close