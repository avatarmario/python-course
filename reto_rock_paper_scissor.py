user_a = input("Player A, enter your choice (rock, paper, scissors): ").lower()
user_b = input("Player B, enter your choice (rock, paper, scissors): ").lower()

#python function to determine the winner of rock-paper-scissors
def determine_winner(choice_a, choice_b):
    if choice_a == choice_b:
        return "It's a tie!"
    elif choice_a == "rock":
        if choice_b == "scissors":
            return "Player A wins!"
        else:
            return "Player B wins!"
    elif choice_a == "paper":
        if choice_b == "rock":
            return "Player A wins!"
        else:
            return "Player B wins!"
    elif choice_a == "scissors":
        if choice_b == "paper":
            return "Player A wins!"
        else:
            return "Player B wins!"
    else:
        return "Invalid input. Please choose rock, paper, or scissors."
    
result = determine_winner(user_a, user_b)
print(type(result))
print(result)