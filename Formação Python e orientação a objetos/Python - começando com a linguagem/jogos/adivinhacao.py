import random

print("+++++++++++++++++++++++++++++")
print("+ Welcome to Guessing Game! +")
print("+++++++++++++++++++++++++++++")

print("\nSECRET NUMBER GAME")

# Control variables
score = 1000
lost_score = 0
attempts = 0
shot_count = 0
secret_number = random.randint(1,100)
# print(secret_number)

print("@@@ Welcome to The Guessing Game @@@")
level = int(input("# Choose a level\n"
                  "  1. Easy\n"
                  "  2. Medium\n"
                  "  3. Hard\n"
                  "Your option: "))

difficulty_levels = {
    "Easy":   1,
    "Medium": 2,
    "Hard":   3,
}

if(level == difficulty_levels["Easy"]):
    attempts = 20
elif(level == difficulty_levels["Medium"]):
    attempts = 10
elif(level == difficulty_levels["Hard"]):
    attempts = 5
else:
    print("@ Your entered not valid option!")
    print("@ By standard your option was setting as easy mode!")
    attempts = 20

for turn in range(1, attempts + 1):
    shot_count = turn

# while(True):
#     shot_count += 1

    # String interpolation :: "$ Attempt {} of {}".format(shot_count, attempts)
    print("$ Attempt {} of {}".format(shot_count, attempts))
    shot = int(input("# Choose a number between 1 and 100:\n"))

    if(shot < 1 or shot > 100):
        print("You missed an attempt. Try again!")
        print("And remember that you must enter a number between 1 and 100!")
        continue

    hit          = secret_number == shot
    without_shot = attempts == shot_count
    bigger_then  = shot > secret_number

    lost_score += abs(secret_number - shot)
    score -= abs(secret_number - shot)

    if(hit):
        print("\n@@@                              @@@")
        print("\\0/ CONGRATULATIONS! YOU DID IT! \\0/")
        print("Shot = ", secret_number)
        print("Secret Number = ", secret_number)
        print("Score = ", score)
        print("Lost Score = ", lost_score)
        break
    elif(without_shot):
        print("\n#####                                  #####")
        print("(x_x) Sorry you couldn\'t get it right! (x_x)")
        print("Secret Number was", secret_number)
        print("Score = ", score)
        print("Lost Score = ", lost_score)
        # break
    elif(bigger_then):
        print("Shot was bigger than secret number.")
    else:
        print("Shot was less than secret number.")
