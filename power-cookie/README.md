
# Power Cookie

Challenge from picoCTF 2022.



## Challenge description

Can you get the flag? Go to this [website](http://saturn.picoctf.net:63115/) and see what you can discover.

## Explained

Open the website. You can see that you can continue as guest but it will not give you anything. Go to the main site, view page source and check ```guest.js```. As you can see, we have to modify isAdmin to be 1 (true). Continue as guest, then Inspect. Go to Storage and check Cookies. Modify value of isAdmin to 1 and refresh website. You will get the flag.


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/288]](https://play.picoctf.org/practice/challenge/288)

