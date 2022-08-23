
import os
import time
import random




#------------CONSOLE COMMANDS-------------------


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()


#------------LOADING TOOLS FILE(DO NOT CHANGE)-------------------

with open("tools.txt", "r") as lt:
    tools_in_file = []
    for tool in lt:
        tools_in_file.append(tool)

    tools = tools_in_file[::3]

remove_n = "\n"
for idx, ele in enumerate(tools):
    tools[idx] = ele.replace(remove_n, '')

#-----------LOADING TOOLS'SPECS (DO NOT CHANGE)--------

upgrade_cost_list = tools_in_file[1::3]
        
tool_power_list = tools_in_file[2::3]

purchase = 0


#------------GAME START------------------

player_name = input("Choose your name:")

save_name = player_name

try:
    os.chdir('saves/')
    read_save = open(player_name, "x")
    os.chdir('..')
    #-----------SAVING A NEW GAME--------
    os.chdir('saves/')

    tool_power_multipier = 0

    upgrade_cost_value = 0

    current_tool_level = 0

    coins = 0

    workers = 1

    with open(player_name, "w") as savevalues:
        savevalues.write(str(tool_power_multipier) + "\n")
        savevalues.write(str(upgrade_cost_value) + "\n")
        savevalues.write(str(current_tool_level) +"\n")
        savevalues.write(str(coins) + "\n")
        savevalues.write(str(workers) + "\n")
    os.chdir('..')

except FileExistsError:
    overwrite = input("You alredy have saved progess. Would you like to load you progress? (y/n)")
    if overwrite == "y":
        with open(player_name, "r") as load_game:
            save_file_values = []
            for values in load_game:
                save_file_values.append(values)
            
            tool_power_multipier = int(save_file_values[0])
            upgrade_cost_value = int(save_file_values[1])
            current_tool_level = int(save_file_values[2])
            coins = int(save_file_values[3])
            workers = int(save_file_values[4])

        os.chdir('..')
    else:
        print("Goodbye!")
        quit()

tool_power = tool_power_list[tool_power_multipier]
upgrade_cost = upgrade_cost_list[upgrade_cost_value]
current_tool = tools[current_tool_level]


clearConsole()


#------------GAME-------------------
print("hit ENTER to dig!")


while True:
    #------------LUCKY GEM STATS (modifiable)-------------------

    #--lucky gem chance---:
    lucky_gem= random.randint(1, 25)
    #--lucky gem power---:
    lucky_gem_power = (workers * int(tool_power)) * 10

    #------------STATUS-------------------
    print("COMMANDS: type '/b' - to visit Blacksmith, type '/s' to visit Miner Shop, type '/q' to save and quit the game \n \n")



    print("You are now in the MINE\n")
    print("Your miners:", str(workers))
    print("Tools: " + str(current_tool).rstrip('\n') + " (mined coins x" + str(tool_power).rstrip('\n') + ")")
    print('\n')
    print("Your coins: " + str(coins))



    if lucky_gem == 1:
        print("You found Lucky Gem! +" + str(lucky_gem_power) + " coins!")
        coins += lucky_gem_power

    x = input("").lower()
    clearConsole()
    coins += workers * int(tool_power)




    #------------MINER SHOP-------------------
    if x == "/s":
        clearConsole()

        #------------MINER SHOP INFO -------------------
        miner_cost = 5

        print("You are now in the MINER SHOP\n")
        print("Your coins: " + str(coins))
        print("1 Miner costs: " + str(miner_cost) + " coins" + "\n")


        print("Type '/b' if you want to quit the MINER SHOP\n")
        purchase = 1
        boost = purchase * miner_cost
        max_purchase = coins // boost

        purchase = input("type '/max' to purchese maximum amount of miners available (You can buy " + str(max_purchase) + " miner(s))" + "\nHow many miners you want to buy: ")
         
        if purchase == "/b":
            print("Going back to the MINE")
            time.sleep(1)
            clearConsole()
            continue

        if purchase == "/max":
            workers = workers + max_purchase
            print(str(max_purchase)+" miner(s) purchesed!")
            coins = coins - (max_purchase * miner_cost)
            print("Going back to the MINE")
            time.sleep(1)
            clearConsole()
            continue

        int(purchase)

        if boost > coins:
            print("Not enough coins!\n")
            print("You need " + str((purchase * miner_cost) - coins) + " more coins!")
            print("Going back to the MINE")
            time.sleep(1.5)
            clearConsole()
            continue
                

        if boost <= coins:
            print(str(purchase)+" miner(s) purchesed!")
            coins = coins - boost
            workers = int(workers) + int(purchase)
            print("Going back to the MINE")
            time.sleep(1.5)
            clearConsole()
            continue


    #------------BLACKSMITH--------------------
    if x == "/b":

        clearConsole()

        #------------BLACKSMITH INFO -------------------
        try:
            avail_upgrades = tools[current_tool_level + 1]

        except IndexError:
            print("Your tools are fully upgraded!")
            print("Going back to the MINE")
            time.sleep(2)
            clearConsole()
            continue





        print("You are now in the FORGE\n")
        print("Your current tool: " + str(current_tool))
        print("Your current tool's power: " + "x " + str(tool_power))
        print("Next level: " + str(tools[current_tool_level+ 1]) + ", Power: x " + str(tool_power_list[tool_power_multipier +1]))

        print("\nYour coins: " + str(coins))
        print("Upgrade cost: " + str(upgrade_cost_list[current_tool_level + 1]))

        upgrade_question = input("Would you like to upgrade your tool?: (y/n)")
        if upgrade_question == "y":

            if int(upgrade_cost_list[current_tool_level + 1]) > coins:
                print("Not enought coins!")
                print("Going back to the MINE")
                time.sleep(1)
                clearConsole()
                continue

            if int(upgrade_cost_list[current_tool_level + 1]) <= coins:
                current_tool_level += 1
                current_tool = tools[current_tool_level]

                tool_power_multipier += 1
                tool_power = tool_power_list[tool_power_multipier]

                coins = coins - int(upgrade_cost_list[current_tool_level])
                upgrade_cost_value += 1

                print("Tools upgraded to: " + str(tools[current_tool_level]))
                print("Going back to the MINE")
                time.sleep(2)
                clearConsole()
                continue

        if purchase == "/b" or "n":
            print("Going back to the MINE")
            time.sleep(1.5)
            clearConsole()
            continue



        


    #------------QUIT FUNCION-------------------    
    if x == ("/q"):
        os.chdir('saves/')
        with open(player_name, "w") as savevalues:
            savevalues.write(str(tool_power_multipier) + "\n")
            savevalues.write(str(upgrade_cost_value) + "\n")
            savevalues.write(str(current_tool_level) +"\n")
            savevalues.write(str(coins) + "\n")
            savevalues.write(str(workers) + "\n")
        os.chdir('..')
        print("Progress saved!")
        print("Goodbye!")
        time.sleep(2)
        clearConsole()
        quit()


    




