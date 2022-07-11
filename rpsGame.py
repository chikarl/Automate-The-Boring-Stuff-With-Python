import random

wins = 0
losses = 0
ties = 0

while True:
    print("ROCK, PAPER, SCISSORS")
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    user_move = input(
        "Enter your move: (r)ock (p)aper (s)cissors or (q)uit \n")
    cpu_move = random.randint(1, 3)
    print(" ")
    if user_move == "q":
        break
    elif cpu_move == 1 and user_move == "r":
        print("ROCK versus ...")
        print("ROCK")
        print("It is a tie!")
        ties = ties + 1
    elif cpu_move == 1 and user_move == "p":
        print("PAPER  versus ...")
        print("ROCK")
        print("You Win!")
        wins = wins + 1
    elif cpu_move == 1 and user_move == "s":
        print("SCISSORS  versus ...")
        print("ROCK")
        print("You Losses!")
        losses = losses + 1
    elif cpu_move == 2 and user_move == "r":
        print("ROCK versus ...")
        print("PAPER")
        print("You Losses!")
        ties = ties + 1
    elif cpu_move == 2 and user_move == "p":
        print("PAPER  versus ...")
        print("PAPER")
        print("It is a tie!")
        wins = wins + 1
    elif cpu_move == 2 and user_move == "s":
        print("SCISSORS  versus ...")
        print("PAPER")
        print("You Win!")
        losses = losses + 1
    elif cpu_move == 3 and user_move == "r":
        print("ROCK versus ...")
        print("SCISSORS  ")
        print("You Win!")
        ties = ties + 1
    elif cpu_move == 3 and user_move == "p":
        print("PAPER  versus ...")
        print("SCISSORS  ")
        print("You Losses!")
        wins = wins + 1
    elif cpu_move == 3 and user_move == "s":
        print("SCISSORS  versus ...")
        print("SCISSORS  ")
        print("It is a tie!")
        losses = losses + 1
    print(" ")
