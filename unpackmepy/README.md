
# unpackme.py

Challenge from picoCTF 2022.



## Challenge description

Can you get the flag? Reverse engineer this [[Python program.]](https://artifacts.picoctf.net/c/465/unpackme.flag.py)

## Explained

Download file using ```wget```. Chceck what is inside file using ```subl unpackme.flag.py```. This script uses ```Cryptography``` library which is responsible for some cryptography operations. We can see plain version of key_str which is:

```python3
key_str = 'correctstaplecorrectstaplecorrec'
```
Then, this string is ```encoded()```  and then utf-8 encoded version of this string is encoded into base64 format. Then it's used to generate Fernet key and payload is decrypted by this key. Decrypted version of payload is then exec. We can simply add ```print(plain)``` before exec and you will get the flag.


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/314]](https://play.picoctf.org/practice/challenge/314)

