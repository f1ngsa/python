# python = input("What is your favorite coding language: ")
# if python == "Python" or python == "python":
#     print("Yes")
# else:
#     print("No")

# one = int(input("Enter a number: "))
# two = int(input("Enter a number: "))
# three = int(input("Enter a number: "))
# if one == 1 and two == 2 and three == 3:
#     print("START")
# else:
#     print("CANCEL")

# g = input("Enter a word: ")
# if "gold" in g or "Gold" in g:
#     print("Yes")
# else:
#     print("No")

number = int(input("Enter a distance in meters: "))
cmorkm = input("Do you want to convert it into centimeters or kilometers: ")
if cmorkm == "Kilometers" or cmorkm == "kilometers" or cmorkm == "km" or cmorkm == "Km" or cmorkm == "KM":
    print(number / 1000, "kilometers")
elif cmorkm == "Centimeters" or cmorkm == "centimeters" or cmorkm == "cm" or cmorkm == "Cm" or cmorkm == "CM":
    print(number * 100, "centimeters")
else:
    print(number)