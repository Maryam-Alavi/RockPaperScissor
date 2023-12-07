import random

print("Choose your option ")
print("1. Rock")
print("2. Paper")
print("3. Scissor")

x = input("Please write your options:")
user_choice = x.lower()
print(f"user choice is: {user_choice}")


pc_choice = random.choice(["rock", "paper", "scissor"])
print(f"Pc chooses: {pc_choice}")
if user_choice == pc_choice:
    print("It is a tie!")
elif user_choice == "rock" and pc_choice == "paper":
    print("You win!")
elif user_choice == "paper" and pc_choice == "rock":
    print("You win!")
elif user_choice == "scissor" and pc_choice == "paper":
    print("You win!")
elif user_choice == "rock" and pc_choice == "scissor":
    print("You win!")
else:
    print("You lose!!")


