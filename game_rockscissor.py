import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to stop): ").lower()
    if user_choice == "exit":
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print(result)
