#!/usr/bin/env python3

import string
import io

characters = []
key_characters = []

with open("message.txt") as mess:
	message = mess.read()
	key = message.partition("\n")[0]

for character in key:
	key_characters.append(character)

for number in range(0,26):
	characters.append(string.ascii_uppercase[number])

print(characters)
print(key_characters)
