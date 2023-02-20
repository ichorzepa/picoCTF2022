
# file-run2

Challenge from picoCTF 2022.



## Challenge description

Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?
Download the program [here]](https://artifacts.picoctf.net/c/395/message.txt).

## Explained

At first download file using ```wget```. Then check type using ```file run```. 

If you use command ```strings run``` then, similar as in file-run1 exercise, you will be able to get flag. But let's play with this script. Add permisions to run code ```chmod +x run```. Then try to run program. You can see that you have to use one argument, ok use it with "hello" input as it is in challenge description. Now you get your flag (xD). You can try with other input argument.

## 🔗 Links
[[https://play.picoctf.org/practice/challenge/266]](https://play.picoctf.org/practice/challenge/266)

