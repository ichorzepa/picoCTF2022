
# transposition-trial

Challenge from picoCTF 2022.

## Challenge description

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message [[here]](https://artifacts.picoctf.net/c/457/message.txt).

## Explained

Download the message using ```wget```. We will write script to solve this:

Read message and divide it into code of each 3 letters.

```python
import re
import numpy as np
with open("message.txt") as mess:
	message = mess.read()


blocks = re.findall('...', message)
```

We can see that first letter of each 3 is on the last position while should be on the first. We create multidimentional array and replace places of letters.

```python
count = len(blocks)
correct = np.empty(shape=(count,3), dtype=str)

for number in range(0,count):
	correct[number][0] = blocks[number][2]
	correct[number][1] = blocks[number][0]
	correct[number][2] = blocks[number][1]
```

We print flag.

```python
print(''.join(correct.flatten()))
```

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/312]](https://play.picoctf.org/practice/challenge/312)