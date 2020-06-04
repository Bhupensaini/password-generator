from module import num_letter
from module import num
from module import letter
import random

while True:
    print("what type of password you want number/alphabets or both")
    choice = input(">> ")

    if choice == 'number' or choice == 'Number':
        chars = num
        break
    elif choice == 'alphabets' or choice == 'Alphabets':
        chars = letter
        break
    elif choice == 'both' or choice == 'Both':
        chars = num_letter
        break
    else:
        print('just type that you alphabets/number or both')
print('')
number = input('number of Passwords:  ')
number = int(number)

length = input('Password length:  ')
length = int(length)
print('')

for p in range(number):
    password = ''
    for c in range(length):
	    password += random.choice(chars)
    print(password)