sum = 0
quantity = 0
while True:
    number = float(input("Enter number, at least 1 number: "))
    if number == 0:
        break
    sum = number + sum
    quantity = quantity + 1
print(sum / quantity)