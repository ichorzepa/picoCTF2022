
# buffer overflow 0

Challenge from picoCTF 2022.



## Challenge description

Smash the stack
Let's start off simple, can you overflow the correct buffer? The program is available [[here]](https://artifacts.picoctf.net/c/521/vuln) You can view source [[here]](https://artifacts.picoctf.net/c/521/vuln.c). And connect with it using:
nc saturn.picoctf.net 65355

## Explained

Start with reading code. Reading from top to bottom, you'll see the function sigsegv_handler which cause printing flag and the vuln function. Read on to main. You will see that you must have the flag.txt file (if you do not have it, it is also possible to redirect the program call, i.e. nc saturn.picoctf.net 65355 > flag.txt). But we will create file using ```touch flag.txt```.

Later you will see "signal handler" which causes the sigsegv_handler function to be called in case of SIGSEGV signal. On the internet you will find that it is a segmentation violation. Next, the program expects you to provide input. The intended buffer for your input is 100. Then the vuln function is called and your input is passed to it. The vuln function tries to write your input to buf2 of size 16. If the buffer is too large (more than 18 characters), then the aforementioned segmentation violation (SIGSEGV) occurs and a flag is displayed.

## More details (Explained II)

Inside ```man strcpy``` you can find that the programmer is responsible for allocating a destination buffer large enough, that is, strlen(src) + 1. While inside ```man gets``` you can finde that it is not adviced to use (use fgets, not gets) because it is impossible to tell without knowing the data in advance how many characters gets() will read, and because  gets() will  continue  to  store  characters past the end of the buffer, it is extremely dangerous to use.

What does it mean for us?

If we pass our input that is more than size of buf2 (16 /in fact 16-1/) then it will cause SIGSEGV. If we pass our input that is more than size of buf1 (100 /in fact 100-1/) it may cause SIGSEGV because gets() will not check if input is in size of buf1.

What is adviced?
1. Use ```strncpy()``` to set max number of characters to copy.
2. Use ```fgets()``` to set how many characters your program should read.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/253]](https://play.picoctf.org/practice/challenge/253)

