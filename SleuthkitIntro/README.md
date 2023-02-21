
# Sleuthkit Intro

Challenge from picoCTF 2022.



## Challenge description

Download the disk image and use ```mmls``` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
Note: if you are using the webshell, download and extract the disk image into ```/tmp``` not your home directory.
[[Download disk image]](https://artifacts.picoctf.net/c/114/disk.img.gz)
Access checker program: ```nc saturn.picoctf.net 52279```

## Explained

Download disk image using ```wget``` (it has 28.34MB). Extract the file using ```gzip -dk disk.img.gz```. Run ```mmls disk.img```. Now run ```nc saturn.picoctf.net 52279```. The checker program asks you for length in sectors. The result is in last line of mmls raport. It's length next to Linux description. Put this value to program and get the flag.


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/301]](https://play.picoctf.org/practice/challenge/301)

