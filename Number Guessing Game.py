
import random

diff = input("Let's play a number guessing game, choose the difficulty of the game (easy, medium, hard)")

if diff.lower() == 'easy':
    num_range = 10 #num_range will be the last number from which the computer will choose a random number.
elif diff.lower() == 'medium':
    num_range = 100
elif diff.lower() == 'hard':
    num_range = 1000
        
while diff != 'easy' or diff != 'medium' or diff != 'hard':
    diff = input("Choose between easy, medium or hard.")
    if diff.lower() == 'easy':
        num_range = 10 #num_range will be the last number from which the computer will choose a random number.
        break
    elif diff.lower() == 'medium':
        num_range = 100
        break
    elif diff.lower() == 'hard':
        num_range = 1000
        break
    

print("")
def user_guess(x):
    chosen_num = random.randint(1, x)
    guess = 0
    while guess != chosen_num:
        guess = input(f"Guess a number between 1 and {x}")
        guess = int(guess)
        
        if guess > chosen_num:
            print("Oops! Your guess is too high!")
        elif guess < chosen_num:
            print("Oops! Your guess is too low!")
    print("Yay! You guessed the number!")




def computer_guess(x):
    low = 1
    high = x
    feedback = ''# This is where user tells computer if guess is correct, high or low.
    while feedback != 'c' :
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high(H), low(L) or correct(C)?".lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer has guessed your number {guess} correctly')


game_mode = input("Do you want to guess the computer's number(user) or do you want the computer want to guess your number(computer)?")

if game_mode == 'user':
    user_guess(num_range)
elif game_mode == 'computer':
    computer_guess(num_range)
else:
    while game_mode != 'user' or game_mode != 'computer':
        game_mode = input("Type either 'user' or 'computer'.")
        if game_mode == 'user':
            user_guess(num_range)
            break
        elif game_mode == 'computer':
            computer_guess(num_range)
            break

while True:
    game_mode = input("To play again or the other game mode type 'user', 'computer' or 'end'")
    if game_mode == 'user':
        user_guess(num_range)
    elif game_mode == 'computer':
        computer_guess(num_range)
    elif game_mode == 'end':
        break
    else:
        pass




