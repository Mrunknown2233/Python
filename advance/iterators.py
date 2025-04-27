my_list = [0,2,4,6]

for element in my_list:
    print(element,end = " ")


my_iter = iter(my_list)
print(my_iter)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter)  raises StopIteration exception


#for in detailed code


iter_obj = iter(my_list)

while True:
    try:
        element = next(iter_obj)
        print(element,end = " ")
    except StopIteration:
        break
print("After While")