
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



