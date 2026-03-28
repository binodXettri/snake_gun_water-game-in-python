# Creating the snake,water,gun game  project
import sys
import random

rules = """
Snake drinks Water → Snake wins 🐍
Water drowns Gun → Water wins 💧
Gun kills Snake → Gun wins 🔫
"""
print("Welcome to Snake-Water-Gun Game!")
print(rules,end="")
rounds=9
user_score=0
computer_score=0

for i in range(rounds):
    print(f"Round {i+1}")

computer=random.choice([1,0,-1])
print("FIRST ROUND!")
mystr=input("Enter your choice('s' for snake 'w' for water 'g' for gun):")
myDict={"s":1,"g":0,"w":-1}

if mystr not in myDict:
        print("Invalid input! Try again.")
        
    
my= myDict[mystr]
reverseDict={1:"snake",0:"gun",-1:"water"}
print(f"you chose:{reverseDict[my]}\ncomputer chose:{reverseDict[computer]}")

if computer == my:
        print("Draw 🤝")

elif (computer == -1 and my == 1) or \
         (computer == 0 and my == -1) or \
         (computer == 1 and my == 0):
        print("You win this round 🎉")
        user_score += 1

else:
        print("You lose this round 💻")
        computer_score += 1
        
computer=random.choice([1,0,-1])
print("SECOND ROUND!")
mystr=input("Enter your choice('s' for snake 'w' for water 'g' for gun):")
myDict={"s":1,"g":0,"w":-1}

if mystr not in myDict:
        print("Invalid input! Try again.")
        
    
my= myDict[mystr]
reverseDict={1:"snake",0:"gun",-1:"water"}
print(f"you chose:{reverseDict[my]}\ncomputer chose:{reverseDict[computer]}")

if computer == my:
        print("Draw 🤝")

elif (computer == -1 and my == 1) or \
         (computer == 0 and my == -1) or \
         (computer == 1 and my == 0):
        print("You win this round 🎉")
        user_score += 1

else:
        print("You lose this round 💻")
        computer_score += 1
        
computer=random.choice([1,0,-1])
print("THIRD ROUND!")
mystr=input("Enter your choice('s' for snake 'w' for water 'g' for gun):")
myDict={"s":1,"g":0,"w":-1}

if mystr not in myDict:
        print("Invalid input! Try again.")
        
    
my= myDict[mystr]
reverseDict={1:"snake",0:"gun",-1:"water"}
print(f"you chose:{reverseDict[my]}\ncomputer chose:{reverseDict[computer]}")

if computer == my:
        print("Draw 🤝")

elif (computer == -1 and my == 1) or \
         (computer == 0 and my == -1) or \
         (computer == 1 and my == 0):
        print("You win this round 🎉")
        user_score += 1

else:
        print("You lose this round 💻")
        computer_score += 1
        
computer=random.choice([1,0,-1])
print("FOURTH ROUND!")
mystr=input("Enter your choice('s' for snake 'w' for water 'g' for gun):")
myDict={"s":1,"g":0,"w":-1}

if mystr not in myDict:
        print("Invalid input! Try again.")
        
    
my= myDict[mystr]
reverseDict={1:"snake",0:"gun",-1:"water"}
print(f"you chose:{reverseDict[my]}\ncomputer chose:{reverseDict[computer]}")

if computer == my:
        print("Draw 🤝")

elif (computer == -1 and my == 1) or \
         (computer == 0 and my == -1) or \
         (computer == 1 and my == 0):
        print("You win this round 🎉")
        user_score += 1

else:
        print("You lose this round 💻")
        computer_score += 1
        
computer=random.choice([1,0,-1])
print("FIFTH ROUND!")
mystr=input("Enter your choice('s' for snake 'w' for water 'g' for gun):")
myDict={"s":1,"g":0,"w":-1}

if mystr not in myDict:
        print("Invalid input! Try again.")
        
    
my= myDict[mystr]
reverseDict={1:"snake",0:"gun",-1:"water"}
print(f"you chose:{reverseDict[my]}\ncomputer chose:{reverseDict[computer]}")

if computer == my:
        print("Draw 🤝")

elif (computer == -1 and my == 1) or \
         (computer == 0 and my == -1) or \
         (computer == 1 and my == 0):
        print("You win this round 🎉")
        user_score += 1

else:
        print("You lose this round 💻")
        computer_score += 1
        

        
print("\nFinal Score")
print(f"You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("🏆 You are the overall winner!")
elif user_score < computer_score:
    print("💻 Overall computer wins the game!")
else:
    print("🤝 It's a tie!")
     
     
