# -----------------------------------------------------------
# Number Guessing Game
# Intro to Python Project
# -----------------------------------------------------------

# Import the random module so the computer can choose a random number
import random


# Function to play one game
def play_game():

    # Randomly choose a number between 1 and 100
    secret_number = random.randint(1, 100)

    # Maximum number of guesses allowed
    max_guesses = 5

    # Keep track of the number of valid guesses
    guesses = 0

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_guesses} chances to guess it.\n")

    # Continue until the player runs out of guesses
    while guesses < max_guesses:

        # Get the player's guess
        guess = input("Enter your guess: ")

        # Check if the input is a whole number
        if not guess.isdigit():
            print("❌ Please enter a whole number between 1 and 100.\n")
            continue

        # Convert the input into an integer
        guess = int(guess)

        # Check if the number is within range
        if guess < 1 or guess > 100:
            print("❌ Your guess must be between 1 and 100.\n")
            continue

        # Count only valid guesses
        guesses += 1

        # Player guessed correctly
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number in {guesses} guess(es)!")
            return

        # Calculate remaining guesses
        remaining = max_guesses - guesses

        # Tell the player if the guess was too low
        if guess < secret_number:
            print("Too low!")

        # Tell the player if the guess was too high
        else:
            print("Too high!")

        # If this was the 4th incorrect guess, give a hint
        if guesses == 4:

            # Simple beginner-friendly hint
            if secret_number % 2 == 0:
                print("💡 Hint: The secret number is EVEN.")
            else:
                print("💡 Hint: The secret number is ODD.")

        # Show guesses remaining if they still have some left
        if remaining > 0:
            print(f"You have {remaining} guess(es) remaining.\n")

    # If the loop ends, the player has used all guesses
    print("\n💥 You Lost! Better luck next time!")
    print(f"The correct number was {secret_number}.")


# Main program loop
while True:

    # Play one game
    play_game()

    # Ask if the player wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()

    # Start a new game if the answer is yes
    if play_again == "yes" or play_again == "y":
        print("\nStarting a new game...\n")

    # End the program if the answer is no
    elif play_again == "no" or play_again == "n":
        print("\n👋 Thanks for playing! Have a great day!")
        break

    # Handle invalid responses
    else:
        print("\nInvalid choice. The game will now end.")
        print("👋 Thanks for playing!")
        break