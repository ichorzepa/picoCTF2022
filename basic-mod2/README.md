
# basic-mod2

Challenge from picoCTF 2022.



## Challenge description

A new modular challenge!
Download the message [[here]](https://artifacts.picoctf.net/c/395/message.txt).
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Explained

Don't think too much about complexity of math operations. Just find how to get modular inverse. If you already did it, now you know we have to use: 

### Extended Euclidean algorithm
```python
def Extended_Euclidean_algorithm(a,b):
   if a == 0:
      return (b, 0, 1)
   else:
      g, y, x = Extended_Euclidean_algorithm(b % a, a)
      return (g, x - (b // a) * y, y)
```

### Modular inverse function

```python
def modinv(a, m):
    g, x, y = Extended_Euclidean_algorithm(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
```

If you use Python 3.8+ you don't have to use all this functions. You can use just:
```python
modulus = pow(int(number), -1, 41)
```

Now create small "dictionary" for letters as it was said in challenge discription. You can use string library (import string).

```python
for number in range(0,26):
   characters.append(string.ascii_uppercase[number])
for number in range(0,10):
   characters.append(string.digits[number])
characters.append('_')
```

You can see, here we start from 0 to 26 for uppercase ASCI letters while in quest description characters 1-26 are the alphabet. Later we just get our modular inversion result and substract 1.

Now open your message.txt and for each read number make reverse mod operation. Then append flag with correct character from our simple dictionary.

```python
with open("message.txt") as mess:
   message = mess.read()
   for number in message.split():
      modulus = modinv(int(number), 41) - 1
      flag.append(characters[modulus])
```

Now print your flag.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/253]](https://play.picoctf.org/practice/challenge/253)

