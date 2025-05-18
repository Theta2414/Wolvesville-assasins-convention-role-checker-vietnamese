# Wolvesville-assasins-convention-role-checker-vietnamese
A simple Python with Tkinter code that find suitable roles in Vietnamese from the given string, helping players get better in Assassins convention mode in Wolvesville game.
What is on the screen?
1. Input field on top of the window.
2. Buttons are in the left.
3. Some functions in the right.
How to use?
"_" stands for character.
"0" stands for space.
- You can click on the buttons "_" (or press on 1 on the keyboard) in the left to add a new character and "0" (or keyborad Space) for space. There are instant input buttons "2, 3, 4, 5" (or 2, 3, 4, 5 on keyboard) to add 2 or more underscores at once. It will automatically add a space at the end if you use instant input the "0" at the end will be automatically eliminated when you click "CHECK" so don't need to delete it manually.
For example: The game shows "___ __", type in "3 2" and you should get "___0__0"
- After entering the word, click on check (or keyboard Enter), all possible result will be shown.
- Click on clear to delete all the characters (or delete on the keyboard)
- Click on backspace to delete a character (or keyboard Backspace)
What is "Unfinished check"?
In case the question is to long and you can't see all of it on the screen (especially for mobile devices), you can use unfinish check.
For example: The game shows "___ __ _____ __" but you can only see "___ __ _____ _" because of screen's width and unsure how many characters after that, just type in "___0__0_____0_0" and use "Unfinished check", this will add more characters until it found at least a result.
The input field can't be focus as I don't know how to unfocus it. If you found a way, you can change the "state" on line 246 to "normal". After this, it is possible to enter a known character to get a better result in input field.
If you can't run the code, it is possible that you didn't download Tkinter. To download Tkinter, open your command prompt on windows 10, 11 and type "pip install tkinter". If you use other operating systems, check alternative ways.
This is for educational purposes only, I do not recommend using this to cheat the game.