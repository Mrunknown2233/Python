def my_range(start,stop,step = 1):
    current = start

    while current<stop if step > 0 else current>stop:
        yield current
        current+=step


for i in my_range(0,11):
    print(i)

for i in my_range(20,10,-2):
    print(i)