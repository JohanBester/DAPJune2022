import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "))

        if guess < random_number:
            print("Sorry, guess again, to low.")
        else:
            print("Sorry, guess again, to high.")

    print(f"\nYeaaaaaah!!! Congrats, you guessed {random_numberx} correctly!")


# guess(10)


def computer_guess(x):
    low = int(1)
    high = int(x)+1
    guess = 0
    feedback = ""
    computer_guesses = 0

    while feedback != "c":
        computer_guesses = computer_guesses + 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high

        feedback = input(
            f"\nIs {guess} too hight (H), too low (L) or correct (C)?").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback != "c":
            print("\nSorry, I did not understand your response. Please try again.")
            continue

    print(
        f"\nYeaaaaaah!!! The computer guessed your number, {guess}, correctly!")
    print(f"The computer took only {computer_guesses} guesses.")


computer_guess(1000)
