try:
    numerator = int(input("Please enter numerator: "))
    denominator = int(input("Please enter denominator: "))

    result = numerator/denominator
    print(result)

    my_list = [1, 2, 3]
    i = int(input("Enter index: "))
    print(my_list[i])

except ZeroDivisionError:
    print("Denominator cannot be 0. Please try again.")

except IndexError:
    print("Index cannot be greater than the size of list.")

print("Program ends")