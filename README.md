Checker (Vietnamese)
A simple Python app built with Tkinter that helps players find suitable roles (in Vietnamese) for the Assassins Convention mode in the Wolvesville game.

🖥️ What is on the screen?

Input field at the top of the window

Buttons on the left

Functions on the right

🎮 How to Use

_ stands for a character

0 stands for a space

🔤 Input
Use the buttons on the left with _ or press 1 on your keyboard to add a new character.

Press 0 (or Space on the keyboard) for a space.

Instant input buttons (2, 3, 4, 5 or keys 2, 3, 4, 5) will add that many _ characters at once.
These also automatically add a space at the end.

✅ You do not need to delete the trailing space manually — the program handles that when you click CHECK.

Example:
The game shows: ___ __
You can input: 3 2
This will give: ___0__0

✅ Main Functions
Check — (or press Enter) to display all possible results

Clear — (or press Delete) to remove all characters

Backspace — (or press Backspace) to remove the last character

🕵️ What is "Unfinished Check"?
If the phrase is too long and doesn't fully show on screen (especially on mobile), use Unfinished Check.

Example:
Game shows: ___ __ _____ __
But only ___ __ _____ _ is visible — you're unsure how many characters are missing.

Input:
___0__0_____0_0
Then press Unfinished Check.
It will automatically add more characters until it finds at least one result.

⚠️ Notes
The input field can't be focused manually due to technical limitations.
If you find a solution, set the state to "normal" at line 246 to allow text input. Then it can base on the given character to find possible result.

For example:
S__ __ ___ will be better than nothing.

🛠 Installation
If the app doesn't run, you may not have Tkinter installed.

Windows 10/11
Open Command Prompt and run:
pip install tkinter
macOS/Linux
Tkinter usually comes pre-installed. If not, search for platform-specific installation methods.

This program also work in other languages, just change the role_list to the language you want.

⚖️ Disclaimer
This tool is for educational purposes only.
I do not recommend using it to cheat in the game.