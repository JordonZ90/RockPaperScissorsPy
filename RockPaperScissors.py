import random
import sys
print("Rock, Paper, Scissors")

wins = 0
losses = 0
ties = 0

while True:
    print(f"{wins} Wins, {losses} Losses,  {ties} Ties")
    while True:
        player_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit ")

        if player_move == "q".lower():
            print("Goodbye!")
            sys.exit()
        if player_move == "r".lower() or player_move == "p".lower() or player_move == "s".lower():
            break
        print("Type one of r, p, s, or q")
    if player_move == "r".lower():
        print("Rock versus...")
    elif player_move == "p".lower():
        print("Paper versus...")
    elif player_move == "s".lower():
        print("Scissors versus...")

    #  Display computer choice
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = "r"
        print("Rock")
    elif random_number == 2:
        computer_move = "p"
        print("Paper")
    elif random_number == 3:
        computer_move = "s"
        print("Scissors")

    #  Display and record win/loss/tie
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif player_move == "r" and computer_move == "s":
        print("You win!")
        wins += 1
    elif player_move == "p" and computer_move == "r":
        print("You win")
        wins += 1
    elif player_move == "s" and computer_move == "p":
        print("You win")
        wins += 1
    elif player_move == "r" and computer_move == "p":
        print("you lose!")
        losses += 1
    elif player_move == "p" and computer_move == "s":
        print("you lose!")
        losses += 1
    elif player_move == "s" and computer_move == "r":
        print("you lose!")
        losses += 1



