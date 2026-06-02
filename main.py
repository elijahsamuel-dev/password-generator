import random

# variables

easy = (0, 50)
medium = (0, 100)
hard = (0, 1000)
guesses = 0
is_running = True
difficulty = 0
asking_name = True
selecting_difficulty = True

while asking_name:
    name = input("Hello! What is your name?: ")
    
    if name == "":
        print("You did not enter a name. Please enter a a name to play the game.")
    elif name.isdigit():
        print("You have entered a number. Please enter a valid name to play the game.")
    else:
        print(f"Hello, welcome to my python number guessing game, {name}!")
        asking_name = False

while selecting_difficulty:
    print(f"Please select a difficulty level (Easy, Medium, Hard): ")
    print("1. Easy (0-50)")
    print("2. Medium (0-100)")
    print("3. Hard (0-1000)")
        
    difficulty = input("Enter the number corresponding to your desired difficulty level: ")

    if difficulty.isdigit():
        difficulty = int(difficulty)

    if difficulty == 1:
        lowest_num, highest_num = easy
        break
    elif difficulty == 2:
        lowest_num, highest_num = medium
        break
    elif difficulty == 3:
        lowest_num, highest_num = hard
        break
    else:
        print("Invalid difficulty selected, please select a number between 1 and 3")
        continue

answer = random.randint(lowest_num, highest_num)

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}.")
        elif guess < answer: 
            print("Too low! Try again.")
        elif guess > answer: 
            print("Too high! Try again.")
        else:
            print(f"Correct! The answer was {answer}.")
            print(f"Number of guesses: {guesses}.")
            is_running = False
    
    else:
        print("Invalid guess.")
        print(f"Please select a number between {lowest_num} and {highest_num}.")