import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors"))
if choice == 0:
    youthrow = rock
elif choice == 1:
    youthrow = paper
else:
    youthrow = scissors

print(youthrow)
random_integer = random.randint(0,2)
if random_integer == 0:
    compthrow = rock
elif random_integer == 1:
    compthrow = paper
else:
    compthrow = scissors

print(compthrow)

if choice == 0:
    if random_integer == 0:
        print("It's a tie")
    elif random_integer == 1:
        print("You lose")
    else:
        print("You win")

if choice == 1:
    if random_integer == 0:
        print("You win")
    elif random_integer == 1:
        print("It's a tie")
    else:
        print("You lose")
        
if choice == 2:
    if random_integer == 0:
        print("You lose")
    elif random_integer == 1:
        print("You Win")
    else:
        print("It's a tie")

