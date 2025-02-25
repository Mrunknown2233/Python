n = int(input("Enter the no of elements u want in ur tuple "))
x = []
for i in range(0,n):
    #x+=[int(input("Enter the element"))]
    x.append(int(input("Enter the element: ")))

a = tuple(x);

sum = 0
for i in a:
        sum+=i

print(f"sum of all the elements in tuple a {a} is {sum}")