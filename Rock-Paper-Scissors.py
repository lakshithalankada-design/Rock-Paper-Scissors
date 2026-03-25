import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()

    if user == 'q':
        break

    if user not in choices:
        print("Invalid choice, try again!")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score -> You: {user_score}, Computer: {computer_score}")
    print("-" * 30)

print("Final Score:")
print(f"You: {user_score}, Computer: {computer_score}")
