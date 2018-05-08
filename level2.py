

# level 2
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

