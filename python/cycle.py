"""import random
while True:
    print(random.randint(1,9))
    favnumber = input("Is this your favorite number?: ")
    if favnumber == "no":
        continue
    elif favnumber == "yes":
        break"""
from random import randint 
number = randint(1,10)
counter = 0
sum = 0
while number != 10:
    counter += 1
    sum += number
    print(number)
    number = randint(1,10)
print(number)
counter += 1
sum += 10
print(f"You got a number 10 after {counter} tries")
print(f"Totalt sum is {sum})