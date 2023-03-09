
# bloat.py

Challenge from picoCTF 2022.



## Challenge description
Can you get the flag? Run this [Python program](https://artifacts.picoctf.net/c/429/bloat.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/429/flag.txt.enc).

## Explained

Download the python program and encrypted flag using wget. You can run script. It will not help you. Then we have to open python program using subl. We can see that there is some kind of alphabet which is used to obfuscate this code.

We can see that user input is realised by ```arg232``` function and saved into ```arg432``` variable. We can also find that function ```arg132()``` is responsible for opening the flag. Returned encrypted bites are saved inside variable ```arg444```. It's later used as argument for```arg111``` which realise decode() function and save result into ```arg423``` which is printed. Inside ```arg432``` we suppose is flag. 

To sum up, what we see when we run program: ```arg232``` ask us for a password. Later ```arg133``` check password. If it's correct, it returns True, if it's not correct it (!!) closes program (and later return False but not important). This logical condition is no later checked so if we pass ```sys.exit(0)``` we will get the flag as everyting will be executed. It's simple: comment this line. You can write whatever as password.

You can write as well:
```python3
print(a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68])
```
And it will print you correct flag.


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/256]](https://play.picoctf.org/practice/challenge/256)

