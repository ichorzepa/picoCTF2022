
# patchme.py

Challenge from picoCTF 2022.



## Challenge description

A type of transposition cipher is the rail fence cipher, which is described [[here]](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
Download the message [[here]](https://artifacts.picoctf.net/c/273/message.txt).
Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.


## Explained

Download the message using ```wget```. Check link and read wiki about Rail fence cipher. We will use popular cryptography website which is [[https://www.dcode.fr]](https://www.dcode.fr/rail-fence-cipher). 

Paste message and set key=4, set "keep punctuation and spaces" and set chracter for spaces as underscore (low dash), then decrypt rail fence. Put decrypted message into correct format: picoCTF{flag}. Do not copy: The_flag_is:_

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/289]](https://play.picoctf.org/practice/challenge/289)

