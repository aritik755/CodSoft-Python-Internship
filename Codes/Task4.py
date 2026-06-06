import random

computer = random.choice([1, 2, 3])
youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ")

yourDict = {"r": 1, "p": 2, "s": 3}
reverseDict = {1: "Rock", 2: "Paper", 3: "Scissors"}

you = yourDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It's a Draw")
else:
    if (computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1):
        print("You Win!")
    else:
        print("You Lose!")
