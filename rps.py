import random

lst = ['rock', 'paper', 'scissor']

# print(computer)

points = 0
chances = 0
while chances<3:
    input_user = input(f"Enter your choice from the following:\n{lst}\n")
    computer = random.choice(lst)
    if input_user=='rock' and computer == 'rock':
        print("Tie, it's rock from computer\n")
        points = points + 0
        chances = chances + 1

    elif input_user=='rock' and computer == 'paper':
        print("-1, it's paper from computer\n")
        points = points - 1
        chances = chances + 1

    elif input_user=='rock' and computer=='scissor':
        print("+1, it's scissor from computer\n")
        points = points + 1
        chances = chances + 1

    elif input_user=='paper' and computer=='rock':
        print("+1, it's rock from computer\n")
        points = points + 1
        chances = chances + 1

    elif input_user=='paper' and computer=='paper':
        print("Tie, it's paper from computer\n")
        points = points + 0
        chances = chances + 1

    elif input_user=='paper' and computer=='scissor':
        print("-1, it's scissor from computer\n")
        points = points - 1
        chances = chances + 1

    elif input_user=='scissor' and computer=='rock':
        print("-1, it's rock from computer\n")
        points = points - 1
        chances = chances + 1

    elif input_user=='scissor' and computer=='paper':
        print("+1, it's paper from computer\n")
        points = points + 1
        chances = chances + 1

    elif input_user=='scissor' and computer=='scissor':
        print("Tie, it's scissor from computer\n")
        points = points + 0
        chances = chances + 1

    else:
        print("wrong input")

if points>1:
    print(f"You won with {points} points")
else:
    print(f"You lost with {points} points")

