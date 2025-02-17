n = int(input("Enter the no of elements u want in ur tuple "))
x = []
for i in range(0,n):
    #x+=[int(input("Enter the element"))]
    x.append(int(input("Enter the element: ")))

a = sorted(tuple(x));

# max = a[len(a)-1]
max = a[n-1]
min = a[0]

print(f"For tuple{a} max element in  is {max} and min element in tuple is {min} ")

