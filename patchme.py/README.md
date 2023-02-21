
# patchme.py

Challenge from picoCTF 2022.



## Challenge description

Can you get the flag?
Run this [[Python program]](https://artifacts.picoctf.net/c/387/patchme.flag.py) in the same directory as this [[encrypted flag]](https://artifacts.picoctf.net/c/387/flag.txt.enc).

## Explained

Download both files to same directory. Open python file to check code. I suggest using sublime text, so type ```subl patchme.flag.py```. There you can find:

```python
user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
```

which define what password is correct to get the flag. You can write it by yourself or above this input add your code:

```python
print("ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000")
```

which will print you correct password after you run program (```python patchme.flag.py```). Just copy and paste password and get the flag!

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/287]](https://play.picoctf.org/practice/challenge/287)

