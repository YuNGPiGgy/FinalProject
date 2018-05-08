import time
import sys

def level1():
    # level one title screen - Cory (ASCII retrieved from http://patorjk.com/)
    print("\nEntering:\n  _                             _         _ \n"
          " | |       ___  __   __   ___  | |  _    / |\n"
          " | |      / _ \ \ \ / /  / _ \ | | (_)   | |\n"
          " | |___  |  __/  \ V /  |  __/ | |  _    | |\n"
          " |_____|  \___|   \_/    \___| |_| (_)   |_|\n")

    # level one - Timothy
    level_one1 = "Your journey starts now. You have arrived on Brierton. Take some time to gather resources " \
                 "that will help you along your way to victory.\n"
    for letter in level_one1:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

    print("\nYou have entered the armory of the Briertonian High Council. Choose your weapon:")
    print("[1] The Sword and Shield of Truth\n[2] The Bow and Cloak of Wonders\n[3] The Wand and Book of Destiny")
    weapon = ""
    while weapon != "1" and weapon != "2" and weapon != "3":
        weapon = input()
        if weapon == "1":
            print("\nYou chose " + color.UNDERLINE + "The Sword and Shield of Truth" + color.END)
            print("Good choice. Adding 20 health and 10 attack")
            HA["health"] += 20
            HA["attack"] += 10
        elif weapon == "2":
            print("\nYou chose " + color.UNDERLINE + "The Bow and Cloak of Wonders" + color.END)
            print("Wise choice. Adding 10 health and 10 attack")
            HA["health"] += 10
            HA["attack"] += 10
        elif weapon == "3":
            print("\nYou chose " + color.UNDERLINE + "The Wand and Book of Destiny" + color.END)
            print("Good choice. Adding 10 health and 20 attack")
            HA["health"] += 10
            HA["attack"] += 20
        else:
            print("ERROR: Please select by number!")

    print("Your health level is:", HA["health"])
    print("Your attack strength is:", HA["attack"])

    # In[5]:

    # possible inventory system - Timothy
    inventory = {}
    level_one2 = "\nTwo of these items will help you greatly, one will not...choose carefully.\n"
    for letter in level_one2:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0)
    print("Select an item:")
    print("\n[1] Cookie\n[2] Band-Aid\n[3] Refreshing ice cold Coca-Cola\n")
    item = ""
    while item != "cookie" and item != "band-aid" and item != "refreshing ice cold coca-cola":
        item = input().lower()
        if item == "cookie":
            inventory[item] = "+50 attack strength"
            HA["attack"] += 50
        elif item == "band-aid":
            inventory[item] = "+50 health"
            HA["health"] += 50
        elif item == "refreshing ice cold coca-cola":
            inventory[item] = "-10 health"
            HA["health"] -= 10
        else:
            print("ERROR: Please select by name! And watch your typing!")
    print(inventory)
    print("\n")

    flag = False
    user_input = input("To check your amount of health type H\n To check attack strength type A\n")
    while flag == True:
        if (user_input == "H" or user_input == "A"):
            flag == True

        else:
            print("ERROR: Enter H, A")
            user_input = input("To check your amount of health type H\n To check attack strength type A\n")

    print(HA["health"])
    print(HA["attack"])

    print("\nLet's take a break.")