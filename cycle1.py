while True:
    number = int(input("Enter a number: "))
    if number != 0:
        print('This isnt zero!')
        continue
    print('Encountered zero')
    break
print('Program is continuing')