"""from_num = int(input("From what number do you want to guess?: "))
to_num = int(input("To what number do you want to guess?: "))
guess = int(input("How many tries do you want?: "))
tries = guess
from random import randint
secretnumber = randint(from_num, to_num)
while True:
    answer = int(input("Enter a number: "))
    tries -= 1
    if answer > secretnumber:
        print("Secret number is smaller!")
    elif answer < secretnumber:
        print("Secret number is bigger!")
    else:
        print("You guessed the secret number!")
        print(f"You used {guess - tries} tries ")
        break
    if tries < 1: 
        print("You have no tries left!")
        break"""
