import random

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
word_letters = word.split(", ")
guess = input("Choose a letter: ").lower()

for letter in word:
    if letter == guess:
        print("match")
    else:
        print("wrong")
    

