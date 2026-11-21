import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("=" * 40)
print("Welcome to the Rock-Paper-Scissors Game!. Press 'q' to quit the game.")
print("=" * 40)

while True:
    print(f"\nScore: you {player_score} - {computer_score} computer")
    player = input("put (rock, paper, scissors):").strip()

    if player == "q":
        break
    if player not in choices:
        print("Invalid choice, please try enter 'rock, paper, scissors!'")
        continue

    computer = random.choice(choices)
    print(f"you have {player}, computer has {computer}")

    if player == computer:
        print("equal, no one wins!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("you win!")
        player_score += 1
    else:
        print("computer wins!")
        computer_score += 1

    print("\n" + "=" * 40)
    print(f"Score: you {player_score} - {computer_score} computer")
    if player_score > computer_score:
        print("You are winning!")
    elif player_score < computer_score:
        print("Computer is winning!")
    else:
        print("It's a tie!")
    print("=" * 40)
