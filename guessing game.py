import random
print("Welcome to the number guessing game")
game_level = input("""Enter your difficulty level
                    select either
                    1 --> Beginner
                    2 --> Intermediate
                    3 --> Pro
                    \n""")
if game_level == "1":
    rand = random.randrange(1, 5)
    num = int(input("Enter the number you guessed: \n"))
    if num == rand:
        print(f"Dev you guessesd {rand} correctly")

    else:
        while num != rand:
            print(f"Sorry, Dev, your number {num} is wrong... \nThe correct answer is {rand}")
            num = int(input("Enter the number you guessed: \n"))

            
            
elif game_level == "2":
    rand = random.randrange(1, 10)
    num = int(input("Enter the number you guessed: \n"))
    if num == rand:
        print(f"Dev you guessesd {rand} correctly")

    else:
        while num != rand:
            print(f"Sorry, Dev, your number {num} is wrong... \nThe correct answer is {rand}")
            num = int(input("Enter the number you guessed: \n"))


elif game_level == "3":
    rand = random.randrange(1, 15)
    num = int(input("Enter the number you guessed: \n"))
    if num == rand:
        print(f"Dev you guessesd correctly")
        num = int(input("Enter the number you guessed: \n"))
    else:
        while num != rand:
            print(f"Sorry, Dev, your number {num} is wrong... \nThe correct answer is {rand}")
            num = int(input("Enter the number you guessed : \n"))


else:
    game_level = input("""Enter your difficulty level
                    select either
                    1 --> Beginner
                    2 --> Intermediate
                    3 --> Pro
                    \n""")
if game_level == "1":
    rand = random.randrange(1, 5)
    num = int(input("Enter the number you guessed: \n"))
    if num == rand:
        print(f"Dev you guessesd {rand} correctly")

    else:
        while num != rand:
            print(f"Sorry, Dev, your number {num} is wrong... \nThe correct answer is {rand}")
            num = int(input("Enter the number you guessed: \n"))

            
            
elif game_level == "2":
    rand = random.randrange(1, 10)
    num = int(input("Enter the number you guessed: \n"))
    if num == rand:
        print(f"Dev you guessesd {rand} correctly")

    else:
        while num != rand:
            print(f"Sorry, Dev, your number {num} is wrong... \nThe correct answer is {rand}")
            num = int(input("Enter the number you guessed: \n"))


elif game_level == "3":
    rand = random.randrange(1, 15)
    num = int(input("Enter the number you guessed: \n"))
    if num == rand:
        print(f"Dev you guessesd correctly")
        num = int(input("Enter the number you guessed: \n"))
    else:
        while num != rand:
            print(f"Sorry, Dev, your number {num} is wrong... \nThe correct answer is {rand}")
            num = int(input("Enter the number you guessed : \n"))


