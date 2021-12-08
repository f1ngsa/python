"""number = 20
while True:
    print(number)
    number -= 1
    if number < 0:
        break"""

"""conter = 2
multiply = 1
while True:
    multiply *= conter 
    conter += 2
    if conter > 10:
        break
print(multiply)"""

"""while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break"""

"""while True:
    number = input("Enter a number: ")
    if number == "stop":
        break"""

lines = 0
while True:
    thero = input("What's up: ")
    lines += 1
    if thero == "Thank you." or thero == "Thanks.":
        break
print(lines)