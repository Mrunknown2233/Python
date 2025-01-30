num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))
num3 = int(input("Enter 2nd number "))

if num1 == num2 and num1 == num3 :
    print("All the numbers are equal")
elif num1 > num2 and num1 > num3 :
    print("Num1 is greatest")
elif num2 > num1 and num2 > num3:
    print("Num2 is greatest")
else:
    print("Num3 is greatest")