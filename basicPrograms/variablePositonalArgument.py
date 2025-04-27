def minimum(*n):  #here *n means packing
    print(type(n))

    if n:
        small = n[0]
        for value in n[1:]:
            if value < small:
                small = value
        return small
print(minimum(10,20,30,40,50,60,4,2,100))


nos = [1,20,30,-4,100]
print(minimum(*nos)) #here *n means unpacking