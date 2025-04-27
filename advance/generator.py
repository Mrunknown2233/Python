def my_generator():
    n = 1
    print("First")
    yield n

    n = 2
    print("Second")
    yield n

    n = 3
    print("Third")
    yield n

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))