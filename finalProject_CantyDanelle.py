#Danelle Canty
#July 18, 2026
#Final Python Project
#Text based python game

# Import the libraries required for the game
import random
import time


# Display the introduction and explain the goal
def show_intro():
    print("========================================")
    print("   🧁 THE MOONLIGHT BAKERY MYSTERY 🧁")
    print("========================================")
    print()
    print("📜 The bakery's secret cupcake recipe is missing!")
    print("Three recipe pages have been scattered around town.")
    print("You must find all 3 pages before you run out of energy.")
    print()

    # Pause briefly before the game begins
    time.sleep(2)


# Display the player's current information
def show_status(player, inventory):
    print()
    print("----------- PLAYER STATUS -----------")
    print("🧑 Name:", player["name"])
    print("⚡ Energy:", player["energy"])
    print("🪙 Coins:", player["coins"])
    print("📄 Recipe pages found:", player["recipe_pages"], "out of 3")
    print("🍪 Snacks:", inventory["snacks"])
    print("-------------------------------------")
    print()


# Let the player use a snack from the inventory
def use_snack(player, inventory):
    if inventory["snacks"] > 0:
        inventory["snacks"] = inventory["snacks"] - 1
        player["energy"] = player["energy"] + 2

        print("🍪 You ate a bakery snack and gained 2 energy!")
        time.sleep(1)
    else:
        print("😕 You do not have any snacks.")
        time.sleep(1)


# Let the player visit the bakery shop
def visit_shop(player):
    print()
    print("🏪 You enter the Moonlight Bakery shop.")
    print("🥤 An energy drink costs 3 coins.")

    if player["coins"] >= 3:
        choice = input(
            "Would you like to buy one? Enter yes or no: "
        ).lower()

        if choice == "yes":
            player["coins"] = player["coins"] - 3
            player["energy"] = player["energy"] + 3

            print("🥤 You bought an energy drink and gained 3 energy!")
        else:
            print("🪙 You decided to save your coins.")
    else:
        print("😕 You do not have enough coins.")

    time.sleep(1)


# Display a special message when a recipe page is found
def find_recipe_page(player, location):
    if player["recipe_pages"] < 3:
        player["recipe_pages"] = player["recipe_pages"] + 1

        if location == "Old Library":
            print("📚 You found a recipe page hidden inside an old cookbook!")
        elif location == "Flower Garden":
            print("🌸 You found a recipe page underneath a flowerpot!")
        else:
            print("🛍️ A market baker handed you one of the missing pages!")

        print("📄 Recipe page collected!")

        # Celebrate when the player finds the final recipe page
        if player["recipe_pages"] == 3:
            print()
            print("✨ You found the FINAL recipe page! ✨")
            time.sleep(1)

    else:
        print("You searched carefully, but found nothing new.")


# Display a special message when coins are found
def find_coins(player, location):
    coins_found = random.randint(1, 3)
    player["coins"] = player["coins"] + coins_found

    if location == "Old Library":
        print(
            "📚 You found",
            coins_found,
            "coins between some dusty books!"
        )
    elif location == "Flower Garden":
        print(
            "🌸 You found",
            coins_found,
            "coins beside the garden fountain!"
        )
    else:
        print(
            "🛍️ You found",
            coins_found,
            "coins near a market stand!"
        )


# Display a special message when a snack is found
def find_snack(inventory, location):
    inventory["snacks"] = inventory["snacks"] + 1

    if location == "Old Library":
        print("🍪 The librarian gave you a freshly baked cookie!")
    elif location == "Flower Garden":
        print("🍓 A gardener gave you a sweet strawberry snack!")
    else:
        print("🧁 A baker at the market gave you a mini cupcake!")

    print("You can eat the snack later to restore energy.")


# Search one of the locations for a recipe page or another item
def search_location(player, inventory, location):
    print()
    print("You travel to the", location + "...")
    time.sleep(1)

    print("🔎 Searching...")
    time.sleep(1)

    print("✨ Something catches your eye...")
    time.sleep(1)

    # Searching costs one energy point
    player["energy"] = player["energy"] - 1

    # Select a random event number
    event = random.randint(1, 4)

    if event == 1:
        find_recipe_page(player, location)

    elif event == 2:
        find_coins(player, location)

    elif event == 3:
        find_snack(inventory, location)

    else:
        if location == "Old Library":
            print(
                "📚 You searched the shelves but found only dusty books."
            )
        elif location == "Flower Garden":
            print(
                "🌸 You searched the flowers but found nothing this time."
            )
        else:
            print(
                "🛍️ You searched the market but did not find anything."
            )

    time.sleep(1)


# Ask the player where they want to search
def choose_location(player, inventory):
    print("Where would you like to search?")
    print("1. 📚 The Old Library")
    print("2. 🌸 The Flower Garden")
    print("3. 🛍️ The Town Market")

    choice = input("Enter 1, 2, or 3: ")

    # Use a loop until the player enters a valid choice
    while choice != "1" and choice != "2" and choice != "3":
        print("That is not a valid choice.")
        choice = input("Please enter 1, 2, or 3: ")

    if choice == "1":
        search_location(player, inventory, "Old Library")
    elif choice == "2":
        search_location(player, inventory, "Flower Garden")
    else:
        search_location(player, inventory, "Town Market")


# Display the celebration after the player wins
def show_win_message(player, inventory):
    print()
    print("🎉 🎉 🎉 CONGRATULATIONS! 🎉 🎉 🎉")
    time.sleep(1)

    print()
    print("📜 You found all 3 missing recipe pages!")
    time.sleep(1)

    print("🧁 The secret cupcake recipe has been saved!")
    time.sleep(1)

    print(
        "👩‍🍳 The bakery opens its doors, and customers"
    )
    print(
        "cannot wait to try the famous cupcakes!"
    )
    time.sleep(1)

    print(
        "🥳 Everyone cheers as the smell of fresh cupcakes"
    )
    print(
        "fills the bakery!"
    )
    time.sleep(1)

    print()
    print("🏆 You are officially the Moonlight Bakery Hero!")
    print("💜 Thank you for saving the bakery!")
    time.sleep(1)

    # Display a special message based on the player's remaining energy
    print()

    if player["energy"] >= 5:
        print(
            "⭐ Amazing job! You finished with lots of energy left!"
        )
    elif player["energy"] >= 2:
        print(
            "😊 Great work! You made it just in time!"
        )
    else:
        print(
            "😅 That was close! You barely made it,"
        )
        print(
            "but you saved the bakery!"
        )

    time.sleep(1)

    # Display the player's final results
    print()
    print("----------- 📋 FINAL RESULTS -----------")
    print("🧁 Baker:", player["name"])
    print("⚡ Energy left:", player["energy"])
    print("🪙 Coins collected:", player["coins"])
    print("📜 Recipe pages:", player["recipe_pages"], "out of 3")
    print("🍪 Snacks left:", inventory["snacks"])
    print("----------------------------------------")
    print()

    print("🎂 🍪 🧁 YOU SAVED THE BAKERY! 🧁 🍪 🎂")
    time.sleep(2)


# Run one complete game
def play_game():
    show_intro()

    # Ask the player to enter a name
    player_name = input("What is your character's name? ")

    # The main character is stored in a dictionary
    player = {
        "name": player_name,
        "energy": 8,
        "coins": 0,
        "recipe_pages": 0
    }

    # The player's inventory is stored in another dictionary
    inventory = {
        "snacks": 1
    }

    print()
    print("Welcome,", player["name"] + "! 👋")
    print("Your search begins now.")
    time.sleep(1)

    # Continue playing while the player has energy
    # and has not found all 3 recipe pages
    while player["energy"] > 0 and player["recipe_pages"] < 3:
        show_status(player, inventory)

        print("What would you like to do?")
        print("1. 🔎 Search a location")
        print("2. 🍪 Eat a snack")
        print("3. 🏪 Visit the bakery shop")

        choice = input("Enter 1, 2, or 3: ")

        # Check the player's menu choice
        if choice == "1":
            choose_location(player, inventory)
        elif choice == "2":
            use_snack(player, inventory)
        elif choice == "3":
            visit_shop(player)
        else:
            print("That is not a valid choice.")
            time.sleep(1)

    # Check whether the player won or lost
    if player["recipe_pages"] == 3:
        show_win_message(player, inventory)
    else:
        print()
        print("😴 You ran out of energy before finding every page.")
        print("The bakery will have to try again tomorrow.")

        print()
        print("----------- 📋 FINAL RESULTS -----------")
        print("🧁 Baker:", player["name"])
        print("⚡ Energy left:", player["energy"])
        print("🪙 Coins collected:", player["coins"])
        print("📜 Recipe pages:", player["recipe_pages"], "out of 3")
        print("🍪 Snacks left:", inventory["snacks"])
        print("----------------------------------------")

    time.sleep(2)


# The main function controls the play-again loop
def main():
    play_again = "yes"

    # Repeat the game if the player chooses yes
    while play_again == "yes":
        play_game()

        print()
        play_again = input(
            "Would you like to play again? Enter yes or no: "
        ).lower()

        # Make sure the player enters yes or no
        while play_again != "yes" and play_again != "no":
            print("That is not a valid choice.")
            play_again = input(
                "Please enter yes or no: "
            ).lower()

    print()
    print("💜 Thanks for playing The Moonlight Bakery Mystery!")
    print("🧁 See you at the bakery again soon! 🧁")


# Start the program by calling the main function
main()