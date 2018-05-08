
# coding: utf-8

# In[1]:


import time
import sys                                                                                  

class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print("INST126 Final: Space Race Game")
print("Group Members: \n   ChiaWen Chen\n   Cory Chassagne\n   Michael Mirabello\n   Timothy Park\n")


# In[2]:


# intoduction and title screen
print("######################")
print(color.UNDERLINE + "Welcome to Space Race" + color.END)
print("######################\n")
intro = "Welcome to the planet Brierton. The planet is in a state of chaos and needs your assistance. Gorgs have taken over and are threatening to rule the galaxy. It's a race against time before the Gorgs conquer the planet and force its inhabitants into slavery. The entire balance of the galaxy is in your hands.\n\n"
for letter in intro: # letter by letter print for intro -
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.01)


# In[3]:


print("Choose your character:")
print("[1] Warrior - High health, Low attack\n[2] Assassin - Medium armor, Medium attack\n[3] Magician - Low health, High attack")
character = ""
HA = {"health": 0, "attack": 0}
while character != "1" and character != "2" and character != "3":
    character = input()
    if character == "1":
        print("You chose " + color.UNDERLINE + "WARRIOR" + color.END)
        HA["health"] += 30
        HA["attack"] += 10
    elif character == "2":
        print("You chose " + color.UNDERLINE + "ASSASSIN" + color.END)
        HA["health"] += 20
        HA["attack"] += 20
    elif character == "3":
        print("You chose " + color.UNDERLINE +"MAGICIAN" + color.END)
        HA["health"] += 10
        HA["attack"] += 30
    else:
        print("ERROR: Please select by number!")
        
print("Your health level is:", HA["health"])
print("Your attack strength is:", HA["attack"])

name = input("Enter your character's name: ")
print("\nEverything depends on you, "+name+"!")


# In[4]:


# level one - Timothy
level_one1 = "Your journey starts now. You have arrived on Brierton. Take some time to gather resources that will help you along your way to victory.\n"
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


# In[ ]:


#level 2
print("\nEntering:")
intro=("  _                    _   ___  \n"
" | |                  | | |__ \ \n"
" | |     _____   _____| |    ) |\n"
" | |    / _ \ \ / / _ \ |   / / \n"
" | |___|  __/\ V /  __/ |  / /_ \n"
" |______\___| \_/ \___|_| |____|\n")
for letter in intro: # letter by letter print for intro -
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.01)
print("\nNow that you have a weapon you should probably get on with saving the planet. However theres an unexplored room in the council building. :")
print("1 for explore the room or 2 to continue on with your mission")
choice = input("What do you do? ")
if choice.lower() == ("1"):
    print("The room was booby trapped. You died and failed to save the planet, resulting in the death of millions. Good job")
    death = quit(1)
elif choice.lower() == ("2"):
        print("You leave the council building in search of the gorg leader. In your search you encounter a group of Gorg minions.")
else:
    print("ERROR: Please enter 1 or 2!")

