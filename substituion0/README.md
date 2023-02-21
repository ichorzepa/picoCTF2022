
# substitution0

Challenge from picoCTF 2022.



## Challenge description

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
Download the message [[here]](https://artifacts.picoctf.net/c/380/message.txt).

## Explained

Download the message using ```wget```. Show message using ```cat message.txt```. At the bottom we can see something looking similar to flag we are looking for. We know it's substition cipher and we see key at the begining. Each letter we can compare to the letter from our alphabet. For example: Q->A, W->B. Let's create simple python script to see it.

You can skip it, it's more recommended to use full tool. Read if you want decode it by yourself or slide down.

```python3
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
```

now you can decrypt last line of message.txt by yourself or use some online tool for monoalphabetic substitution like [[decode.fr]](https://www.dcode.fr/monoalphabetic-substitution) (remember to paste alphabet from message.txt). You will get the flag.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/307]](https://play.picoctf.org/practice/challenge/307)

