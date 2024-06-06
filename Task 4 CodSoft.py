import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    return input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You Win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You Win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You Win!"
    else:
        return "Computer Wins!"
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":   
            print("Thanks for playing!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        print()

if __name__ == "__main__":
    play_game()

