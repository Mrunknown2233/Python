def swap(x,y):
    return y,x


num1 = int(input("Enter no 1 : "))
num2 = int(input("Enter no 2 : "))

print(f"Num1 = {num1} and Num2 = {num2}");

num1,num2 = swap(num1,num2)

print(f"Num1 = {num1} and Num2 = {num2}");

