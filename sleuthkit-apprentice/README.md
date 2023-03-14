
# Sleuthkit Apprentice

Challenge from picoCTF 2022.



## Challenge description

Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into ```/tmp``` not your home directory.

[Download compressed disk image](https://artifacts.picoctf.net/c/88/disk.flag.img.gz)

## Explained

Download using ```wget``` into ```/tmp```. Extract it there and check partition table using ```mmls``` command. We can see that one (last) has suspicious length. We will mount it using ```sudo mount /tmp/disk.flag.img /tmp/foo -o offset=$((360448*512))```. 360448 is start of the last partition. From the header you can see that units are in 512-byte sectors. That's why for offset we have to multiply it to find adress of this partition.

You can see the new partition mounted inside /tmp/foo. Check what is inside using ```ls -alps /tmp/foo```.

We can search for something called "flag" inside. Use ```sudo find /tmp/foo -name flag*```.  You will get the flag, just ```cat``` it.


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/300]](https://play.picoctf.org/practice/challenge/300)

