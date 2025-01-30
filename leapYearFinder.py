year = int(input("Enter the year : "))

if (0 == year % 400) or ((year%100 != 0) and (0 == year % 4 )): 
    print("The year ",year," is a leap year")
else:
    print("The year ",year," is not  a leap year")