print("Hello Periode 2")


Player_name = input("What is your name? ")
player_gold = input("How much gold do you have? ")
inventory = input("What is in your inventory? ")

print("welcome " + Player_name + " you have " + player_gold + " gold and your inventory contains: " + inventory)


items = ["Sword", "Shield", "Potion", "Bow"]
inventory = []

for item in items:
    print(item)

    keuze = int(input("Welk nummer wil je kopen? "))
print("Je hebt gekozen:", items[keuze - 1])

while True:
    print("=== Fantasy Item Shop ===")
    print("1. Koop Sword (50 gold)")
    print("2. Koop Shield (40 gold)")
    print("3. Koop Potion (20 gold)")
    print("4. Koop Bow (60 gold)")
    print("5. Bekijk Inventory")
    print("6. Verlaat Shop")

    keuze = int(input("What would you like to do? "))

    if keuze == 1:
        if player_gold < 50: 
            print("Je hebt niet genoeg gold")

        else:

            print("Je hebt een Sword gekocht!")
            # kijk of imeand genoeg heeft
            # 
            # voeg toe aan inventory 
            append_to_inventory = input("Wil je dit item toevoegen aan je inventory? (ja/nee): ")
            if append_to_inventory.lower() == "ja":
                inventory.append("Sword")
                print("Sword is toegevoegd aan je inventory.")


    elif keuze == 2:
        if player_gold < 40:
            print("Je hebt niet genoeg gold!")

        else: 

            print("Je hebt een Shield gekocht!")
        append_to_inventory = input("Wil je dit item toevoegen aan je inventory? (ja/nee): ")
        if append_to_inventory.lower() == "ja":
            inventory.append("Shield")
            print("Shield is toegevoegd aan je inventory.")
    elif keuze == 3:
        
        if player_gold < 20:
            print("Je hebt niet genoeg gold!")

        else:
            print("You bought a Potion!")
    elif keuze == 4:
        if player_gold < 60:
            print("Je hebt niet genoeg gold!")

        else:
            print("You bought a Bow!")
            append_to_inventory = input("Wil je dit item toevoegen aan je inventory? (ja/nee): ")
            if append_to_inventory.lower() == "ja":
                inventory.append("Bow")
                print("Bow is toegevoegd aan je inventory.")

    elif keuze == 5:
        if inventory:
            print("Your inventory contains:")
            for item in inventory:
                print("- " + item)
        else:
            print("Your inventory is empty.")
        
    elif keuze == 6:
        print("Thanks for visiting!")
        break
    else:
        print("Please choose a number from 1 to 6.")
    
    show_player_gold = input("Do you want to see how much gold you have left? (yes/no): ")
    if show_player_gold.lower() == "yes":
        print("You have " + str(player_gold) + " gold left.")
        break 

    player_gold = int(input("How much gold do you have? "))





