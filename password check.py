username=input ('enter your username: ')
password=input('enter your password: ')

passlength= len(password)
secretpassword= '*'*passlength
print(f'{username}, your password {secretpassword}, is {passlength} letters long')