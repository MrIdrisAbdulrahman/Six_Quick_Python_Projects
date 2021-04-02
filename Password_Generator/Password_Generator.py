import random

print('Welcome to your Password Generator')

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%&*().,?0123456789'

number = input('Number of passwords to be generated: ')
number = int(number)

length = input('Your password length')
length = int(length)

print('\nhere are your passwords:')

for password in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(characters)
    print(passwords)
