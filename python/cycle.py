import random
while True:
    print(random.randint(1,9))
    favnumber = input("Is this your favorite number?: ")
    if favnumber == "no":
        continue
    elif favnumber == "yes":
        break