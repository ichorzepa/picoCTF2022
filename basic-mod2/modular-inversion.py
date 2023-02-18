#!/usr/bin/env python3

import string

characters = []
flag = []

def Extended_Euclidean_algorithm(a,b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = Extended_Euclidean_algorithm(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = Extended_Euclidean_algorithm(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

for number in range(0,26):
	characters.append(string.ascii_uppercase[number])
for number in range(0,10):
	characters.append(string.digits[number])
characters.append('_')

with open("message.txt") as mess:
	message = mess.read()
	for number in message.split():
		
		# use modulus = pow(int(number), -1, 41) in Python 3.8+
		# we use functions to be compatible with previous versions
		modulus = modinv(int(number), 41) - 1
		flag.append(characters[modulus])

print("picoCTF{" + "".join(flag) + "}")