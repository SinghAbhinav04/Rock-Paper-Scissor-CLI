import random

choices = ["rock", "paper", "scissors"]
userChoices = ["rock", "paper", "scissors", "exit"]
computer_score = 0
player_score = 0

while True:
    player = None
    while player not in userChoices:
        player = input("rock, paper, scissors, or exit?: ").lower()

    if player == "exit":
        print("Thanks for playing!")
        print(f"Final Score -> Player: {player_score} - Computer: {computer_score}")
        break

    computer = random.choice(choices)

    if player == computer:
        print(f"Computer: {computer}")
        print(f"Player: {player}")
        print(f"TIE!!\tComputer: {computer_score} - Player: {player_score}")

    elif player == "rock":
        if computer == "scissors":
            player_score += 1
            print("You win!!")
        else:
            computer_score += 1
            print("You lose!!")

    elif player == "paper":
        if computer == "rock":
            player_score += 1
            print("You win!!")
        else:
            computer_score += 1
            print("You lose!!")

    elif player == "scissors":
        if computer == "paper":
            player_score += 1
            print("You win!!")
        else:
            computer_score += 1
            print("You lose!!")

    print(f"Computer: {computer}")
    print(f"Player: {player}")
    print(f"Score -> Computer: {computer_score} - Player: {player_score}\n")
