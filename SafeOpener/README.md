
# Safe Opener

Challenge from picoCTF 2022.



## Challenge description

Can you open this safe?
I forgot the key to my safe but this [[program]](https://artifacts.picoctf.net/c/463/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
Put the password you recover into the picoCTF flag format like:
picoCTF{password}

## Explained

Download the program using ```wget```. Check code using ```subl SafeOpener.java```. You will find out that the encoding type is Base64. You can find that encoded key is "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz". Now you can use popular cryptography site [[decode.fr]](https://www.dcode.fr/base-64-encoding) to decode this key from base64.

You get the flag! Put it inside picoCTF{flag}.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/294]](https://play.picoctf.org/practice/challenge/294)

