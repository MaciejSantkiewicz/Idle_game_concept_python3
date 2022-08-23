# Idle_game_concet_python3

-game has no goal, it's just a concept-

Lunch the game.py file in the Terminal

---------------------------------




Features

-save and load function

-.txt file with modifable quantity and stats of tool's (in-game items) by user without limits

-random events (just one at the moment)

-currency (value) updated with every input


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

-can upgrade current tool used by miners
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


