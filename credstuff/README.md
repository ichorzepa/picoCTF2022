
# credstuff

Challenge from picoCTF 2022.



## Challenge description
We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
Download the leak [[here]](https://artifacts.picoctf.net/c/534/leak.tar).
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

## Explained

Download file usin ```wget``` then extract it using ```tar -xvf leak.tar```.

Then find number of line where username is stored:
```egrep -n "cultiris" usernames.txt ```

Now print this line from file with encrypted passwords:
```sed -n '378p' passwords.txt```

We get something like this:
cvpbPGS{P7e1S_54I35_71Z3}

And it makes problem, you have to figure out what algorthm decrypted it. It is substitution cypher ROT13. Decrypt it and get flag.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/261]](https://play.picoctf.org/practice/challenge/261)

