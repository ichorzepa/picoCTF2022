
# Enhance!

Challenge from picoCTF 2022.



## Challenge description
Download this image file and find the flag.
Download image file [[here]](https://artifacts.picoctf.net/c/137/drawing.flag.svg).

## Explained

Download image using ```wget```. We can view content of the .svg (vector image) using ```strings```.

Use this command and scroll down. You will find there parts of flag. Join them.

It begins with:

```html
<tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08501"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3748">p </tspan>
```

If you have tried with ```exiftool``` or ```hexeditor``` - good for you. Remember, flag can be everywhere. It's good to know more tools.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/265]](https://play.picoctf.org/practice/challenge/265)

