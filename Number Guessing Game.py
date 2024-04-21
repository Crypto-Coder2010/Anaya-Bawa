
import random

name = input("What is your name?")

print("")
ans_num = random.randint(1,101)
print(f"Hello, {name}. Let us play a number guessing game!")
print("")
guess_num = input("Now, try and guess a number between 1 and a 100")
print("")
guess_num = int(guess_num)

while guess_num != ans_num :

    if guess_num < ans_num:
        print(f"Oops! {guess_num} is lower than the number I chose.")
        print("")
    else :
        print(f"Oops! {guess_num} is greater than the number I chose.")
        print("")
    guess_num = input("Now, try and guess a number between 1 and a 100")
    print("")
    guess_num = int(guess_num)

print(f"Good Job! The correct answer was {ans_num}")
