

print("Hello Periode 2")

def show_menu():
    print("=== Fantasy Item Shop ===")
    print("1. Koop Sword (50 gold)")
    print("2. Koop Shield (40 gold)")
    print("3. Koop Potion (20 gold)")
    print("4. Koop Bow (60 gold)")
    print("5. Bekijk Inventory")
    print("6. Verlaat Shop")

def show_inventory(inventory):
    if inventory:
        print("Your inventory contains:")
        for item in inventory:
            print("- " + item)
    else:
        print("Your inventory is empty.")


def can_buy(gold, price):
    return gold >= price


def buy_item(gold, inventory, item_price, item_name):
    if not can_buy(gold, item_price):
        print("Je hebt niet genoeg gold!")
        return gold

    inventory.append(item_name)
    gold -= item_price
    print("Je hebt een " + item_name + " gekocht en toegevoegd aan je inventory.")
    print("Je hebt nog " + str(gold) + " gold.")
    return gold


Player_name = input("What is your name? ")
player_gold = int(input("How much gold do you have? "))
inventory = []

print("welcome " + Player_name + " you have " + str(player_gold) + " gold and your inventory contains: " + str(inventory))

while True:
    show_menu()

    keuze = int(input("What would you like to do? "))

    if keuze in (1, 2, 3, 4):
        item_name, item_price = {
            1: ("Sword", 50),
            2: ("Shield", 40),
            3: ("Potion", 20),
            4: ("Bow", 60),
        }[keuze]
        player_gold = buy_item(player_gold, inventory, item_price, item_name)
    elif keuze == 5:
        show_inventory(inventory)
    elif keuze == 6:
        print("Thanks for visiting!")
        break
    else:
        print("Please choose a number from 1 to 6.")