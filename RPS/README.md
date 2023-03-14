
# RPS

Challenge from picoCTF 2022.



## Challenge description

Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row. Connect to the program with netcat: ```$ nc saturn.picoctf.net 64710``` The program's source code with the flag redacted can be downloaded [here](https://artifacts.picoctf.net/c/114/game-redacted.c).

## Explained

Download using ```wget``` and check the code. Program check if we won using following code:
```c
  if (strstr(player_turn, loses[computer_turn])) {
    puts("You win! Play again?");
    return true;
 ```

Function ```strstr``` chceck if part of ```player_turn``` string is inside ```loses[computer_turn]```. Player turn buffer is set for 100 characters. If we make our selection as: rockepaperscissors , then no matter what computer played, you won.

Do it 5 times in row and get the flag!



## 🔗 Links
[[https://play.picoctf.org/practice/challenge/293]](https://play.picoctf.org/practice/challenge/293)

