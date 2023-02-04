import random
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

count = len(names) - 1
random_int = random.randint(0, count)
payer = names[random_int]
print(f"{payer} will pay the bill today")


