#!/usr/bin/env python3

import re
import numpy as np
with open("message.txt") as mess:
	message = mess.read()


blocks = re.findall('...', message)

count = len(blocks)
correct = np.empty(shape=(count,3), dtype=str)

for number in range(0,count):
	correct[number][0] = blocks[number][2]
	correct[number][1] = blocks[number][0]
	correct[number][2] = blocks[number][1]


print(''.join(correct.flatten()))