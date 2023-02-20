
# file-run1

Challenge from picoCTF 2022.



## Challenge description

A program has been provided to you, what happens if you try to run it on the command line?
Download the program [[here]](https://artifacts.picoctf.net/c/309/run).

## Explained

At first download file using ```wget```. Then check type using ```file run```. Now the question is, what type of tool we should use. To be honest i started with ```strings run``` which will show you the flag, but it's much easier to just add permisions to run script ```chmod +x run``` and run it with ```./run```. The script will print you the flag.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/266]](https://play.picoctf.org/practice/challenge/266)

