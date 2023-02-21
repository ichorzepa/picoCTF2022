
# Search source

Challenge from picoCTF 2022.



## Challenge description

The developer of this website mistakenly left an important artifact in the website source, can you find it?
The website is [[here]](http://saturn.picoctf.net:50761/)

## Explained

Open the website on your web browser. You can check website source. There is some interesting information:

```html
<!-- six_box
            end six_box   The flag is not here but keep digging :)-- >

            <!-- We Do Yogas -->
```

We can search something inside included files from <head> section. There we can just ctrl+f "ctf". That's how you will find flag inside style.css


## 🔗 Links
[[https://play.picoctf.org/practice/challenge/295]](https://play.picoctf.org/practice/challenge/295)

