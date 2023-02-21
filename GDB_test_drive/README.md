
# GDB Test Drive

Challenge from picoCTF 2022.



## Challenge description

Can you get the flag?
Download this [binary]](https://artifacts.picoctf.net/c/116/gdbme)
Here's the test drive instructions:
```linux
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

## Explained

At first, download binary using ```wget```. Then add execution permission using ```chmod +x gdbme```. You can find out what type it is using ```file``` and what is inside using ```strings```. This time, using ```strings``` is not enought ;-)

Run command as it is in description: ```gdb gdbme```. You may have to install gdb using command ```apt install gdb```. Type ```layout asm``` to apply assembler layout. Set breakpoint using ```break *(main+99)```. Run command ```run``` and ```jump *(main+104)```. You get the flag. Borning.


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/273]](https://play.picoctf.org/practice/challenge/273)

