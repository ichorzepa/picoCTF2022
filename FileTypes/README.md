
# File types

Challenge from picoCTF 2022.



## Challenge description

This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
You can download the file from [here]](https://artifacts.picoctf.net/c/324/Flag.pdf).

## Explained

At first download file using ```wget```. Then check type using ```file Flag.pdf```. The information is not normal. Shell arhcive text is not pdf type. If we type ```strings Flag.pdf``` then we get some script. We don't have to examinate what does it mean. Look for first commentary lines, we should save it to some FILE, remove everything before the ```#!/bin/sh``` line above, then type ```sh FILE```. Lets try it.

We use ```cp Flag.pdf FILE```. We have nothing to remove before mentioned line, but if you want you can check by yourself ```vi FILE``` or ```nano FILE```.

Run ```sh FILE```. If you get error: FILE: 119: uudecode: not found
then type ```sudo apt-get install sharutils```.

Now list files in directory (```ls```) and ```cat flag```. Wow! There is no flag. Check again using ```file flag``` [result: flag: current ar archive]. Search web for how to extract file from such extension. Use ```ar xv flag``` to extract the wole archive and list name of each member which is extracted.

Boom! We extracted 'flag'. Check it ```cat flag```, and again nothing, so ```file flag```. We get cpio archive. Search web again. Use ```cpio -idv < flag```. We can't do that so rename ```mv flag flag2``` and run again ```cpio -idv < flag2```.

Again we check what is inside our new flag file and we get nothing. We repeat steps (now bzip2). We have to decompress file ```bzip -dk flag```. We can again check what is inside file, and again get nothing. Repeat steps.

```mv flag flag.gz``` and ```gzip -d flag.gz``` ... repeat steps. You may have to install ```lzip``` from [[here]](http://download.savannah.gnu.org/releases/lzip/lzip-1.23.tar.gz) and then use ```lzip -d flag```. We can repeat steps (now lz4) ```lz4 -d flag.out flag```. We can repeat steps (now lzma which you may have to install ```sudo apt-get install lzma```). Rename file ```mv flag flag.lzma``` and decompress ```lzma -d flag.lzma```. And again (xd!) decompress lzop data (you may have to install ```sudo apt install lzop```). Rename ```mv flag flag.lzo``` and decompress ```lzop -d flag.lzo```. Repeat for lzip. Remove ```rm flag.out``` and run ```lzip -d flag```. Check file extension for flag.out and repeat steps. Rename ```mv flag.out flag.xz``` and run ```xz -d -v flag.xz```. Check for file extension ```file flag```.

Boom! ASCII text. It was looooong route. Check what is inside ```cat flag```. XD, what a joke. There is no flag. Copy this data and put it inside [Cyberchef]](https://gchq.github.io/CyberChef/).

Inside this website try operations (from base64, from hexdump etc.). You will find the flag.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/268]](https://play.picoctf.org/practice/challenge/268)

