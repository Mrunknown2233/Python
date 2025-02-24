n = int(input("Enter a no : "))

if n>=0:
    fact = 1
    for i in range(1,n+1):
        fact *=i
    print(f"Factorial of {n} is {fact}")
else:
    print("Enter a positive number")
        
