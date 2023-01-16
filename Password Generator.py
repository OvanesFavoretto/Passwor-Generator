import random

print('Welcome to your password generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = input('Amount of password to generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere are your password:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
