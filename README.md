# Idle_game_concet_python3

-the game goal is to collect as much coins as possible, it's just a concept-
Lunch the game.py file in the Terminal

---------------------------------




Features

-save and load function (game load files based on given user name)
![name](https://user-images.githubusercontent.com/111911254/219869900-7d6e9f73-7588-4a69-bb4c-6a7cff1a5ede.jpg)


-.txt file with modifable quantity and stats of tool's (in-game items) by user without limits

-random events (just one at the moment)

-currency (value) updated with every input

![game](https://user-images.githubusercontent.com/111911254/219869910-7f885c49-7d2a-4f91-8e10-811f377ce18e.jpg)




Bugs:

-yes


---------------------------------


How to play:

With every input you are getting coins, based on the number of miners you have and tool's power they are using (added coins per input  = number of miners * tool's power)

-Hit ENTER to dig

-or use provided inputs to visit other panels:

"type '/b' - to visit Blacksmith, type '/s' to visit Miner Shop"

---
Blacksmith:

-can update current tool used by miners
![forge](https://user-images.githubusercontent.com/111911254/219869921-ab5746cf-4c37-4f37-a56c-b1d38c56d6d5.jpg)

---
Miner Shop:

-let you hire more miners

---
Random event:
-with every input there is a chance to get x10 coins, based on current modifiers (number of miners and tool's power). 
Base chance is 4% (can be modifiable in the game.py file)

---
-type '/q' to save the progress and quit the game

---------------------------------
-to load a save type the same user name you choosed before or use any file name located in /saves folder

---------------------------------

To expand the available tool upgrades, add the following line in the tools.txt file, as follow:


[Tool name]

[Tool power] - will muliple the coins digged by miner

[Tool purchase cost] - nuber of coins needed


For example:

Wooden pickaxes 

1

1000


