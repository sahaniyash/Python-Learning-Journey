#rock #paper #scissors
import random
user_action = input("Enter a choice (rock,paper,scissors): ")

possible_action = ["rock","paper","scissors"]
computer_action = random.choice(possible_action)

print(f"\nYou Chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action :
    print(f"Both Players Selected {user_action}. It's a tie")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock samshes scissors! You Win!")
    else :
        print("Paper covers rocks! you lose.")

elif user_action == "paper":
    if computer_action == "rock":
        print("paper covers rock! You Win!")
    else :
        print("Scissors cuts paper! you lose.")

elif user_action == "Scissors":
    if computer_action == "paper":
        print("scissors cut paper! You Win!")
    else :
        print("Rock Smashes scissors! you lose.")