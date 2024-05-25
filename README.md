This is a copy of the **Who Wants to be a Millionaire** game which is based off of the game show. It is created in the 
python programming language using the pygame library/engine.

I primarily started this project as a fun thing on the side during winter break 2022 and as a way to put into use the 
different OOP designs I had been learning. So, I promptly forgot this project existed until this spring of 2024. After
forgetting about this project and coming back to it, the motivation was the same except that now I had a challenge to 
overcome and a journey to begin. This Spring after rediscovering that I had begun work on this **Who Wants to be a 
Millionaire** game (which I had named Jeopardy incorrectly), I decided that to consider this game completed I needed to 
implement two things: not tkinter simultaneously with pygame, but also two different tkinter simultaneous tkinter 
windows. After embarking on this journey (having not used tkinter before), I believe I learned a fair bit not only about
tkinter and pygame, but what good programming patterns look like, especially in Object-Oriented Programming, something I 
had become increasingly familiar with throughout the years, and been forced to use in the **Advanced Placement Computer 
Science A** Course which utilized the notoriously obtuse, OOP language that was **JAVA**. This forced me to become
acquainted with **OOP**, not that it was naturally abhorrent. As I write this, I have mostly completed these goals and 
am left tasked with refactoring my code, adding icons to my windows, adding different styles to one of my tkinter 
windows, and thinking about what comes next.

There are a few things I want to learn more about in pygame, python, tkinter, etc. These things I think will come in the
form of work on this project. These things include:

- **Optimize using one large sprite sheet**
- Add more characters to phone a friend
- Adding sound to my game
- Adding settings
- Adding mac compatibility 
- Adding an advanced setting for users to customize their question set (least likely to happen, just sounds annoying)
- Finding a better question set with difficulties outlined so that difficulty increases with more correct questions

Overall, this has been a good learning experience, not least of all because of the various sources which allowed me to 
rapidly work on this project. These include the:
- Button Icons: https://millionaire.fandom.com/wiki/
- Santa Image: https://www.alamy.com/vector-pixel-art-santa-bored-isolated-cartoon-image361797411.html
- Parents Image: https://www.pinterest.com/pin/vixels-this-artist-will-turn-you-into-a-pixel-person--348325352413596829/
- Background: https://imgflip.com/memetemplate/135518796/Jeopardy-Empty-Box
- Question set: https://www.scribd.com/document/405636501/Wwtbam-Json-File-json
- Reset icon: https://www.iconfinder.com/icons/211882/refresh_icon
- The rest of the attributions for various other helps is embedded inside the source code

Known problems (I may think about fixing maybe):
1. One in every 500 or so times when the 50/50 button is clicked, 3 questions are removed this is probably easy to fix 
since I remove half of the questions in a hacky manner
2. Sometimes when the Ask the audience button is pressed the program just crashes - this is IMPOSSIBLE to fix (I don't 
want to change the tkinter pygame compatibility I somewhat have going on here)