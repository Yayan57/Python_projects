import random

while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?:").lower()

    if player == computer:
        print("Computer:", computer)
        print("Player:", player)
        print("TIE!")
    elif player == 'rock':
        if computer == 'paper':
            print("Computer:", computer)
            print("Player:", player)
            print("You lose :(")
        if computer == 'scissors':
            print("Computer:", computer)
            print("Player:", player)
            print("You win")
    elif player == 'paper':
        if computer == 'scissors':
            print("Computer:", computer)
            print("Player:", player)
            print("You lose :(")
        if computer == 'rock':
            print("Computer:", computer)
            print("Player:", player)
            print("You win")
    elif player == 'scissors':
        if computer == 'rock':
            print("Computer:", computer)
            print("Player:", player)
            print("You lose :(")
        if computer == 'paper':
            print("Computer:", computer)
            print("Player:", player)
            print("You win")

    playAgain = input("Do you want to play again Y/N:").lower()

    if playAgain != "y":
        break
print("bye!")

