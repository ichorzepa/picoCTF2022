#!/usr/bin/env python3

import string

characters = []
flag = []

for number in range(0,26):
	characters.append(string.ascii_uppercase[number])
for number in range(0,10):
	characters.append(string.digits[number])
characters.append('_')

with open("message.txt") as mess:
	message = mess.read()
	for number in message.split():
		modulus = int(number) % 37
		flag.append(characters[modulus])

print("picoCTF{" + "".join(flag) + "}")