
# basic-mod1

Challenge from picoCTF 2022.



## Challenge description

We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message [[here]](https://artifacts.picoctf.net/c/395/message.txt).
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Explained

Create simple python file, name it as you wish. At first, create small "dictionary" for letters as it was said in challenge discription. You can use string library (import string).

```python
for number in range(0,26):
   characters.append(string.ascii_uppercase[number])
for number in range(0,10):
   characters.append(string.digits[number])
characters.append('_')
```

Now open your message.txt and for each read number make basic mod operation (using % character). Then append flag with correct character from our simple dictionary.

```python
with open("message.txt") as mess:
   message = mess.read()
   for number in message.split():
      modulus = int(number) % 37
      flag.append(characters[modulus])
```

Now print your flag.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/253]](https://play.picoctf.org/practice/challenge/253)

