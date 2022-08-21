import random


def play():
    user = input("Choose 'r' for rock, 'p' for paper, or 's' for scissors : ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    elif is_win(user, computer):
        score["player"] = score["player"] + 1
        return "You win this one!"
    else:
        score["computer"] = score["computer"] + 1
        return "Sorry, better luck next time."


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def complete_game():
    if score["player"] > score["computer"]:
        return "\nWhoooohooooo! you WON the Match!!!"
    elif score["player"] < score["computer"]:
        return "\nSorry, you lost. Better luck next match."
    elif score["player"] == score["computer"]:
        print("\nWow! It's a tie! We need a tie Breaker!")
        return tie_breaker()


def tie_breaker():
    print("\nLast and deciding round ....")
    return play()


score = dict()
score = {"player": 0, "computer": 0}
round = 1

response = input("Shall we play some Rock-Paper-Scissors (y/n)? ").lower()
if response == 'y':
    while round <= 4:
        if round == 1:
            print(f"\nLet's go! Round #{round}!")
            print(play())
        elif (round == 2) or (round == 3):
            print(f"\nNext round, Round #{round}.")
            print(play())
        elif round == 4:
            print("\nLet's see who won the Match ....")
            print(complete_game())
            exit
        round += 1

else:
    print("Good Bye!")
