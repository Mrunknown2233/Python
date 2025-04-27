def fibonnacci(num):
    a,b = 0,1

    for _ in range(num):
        a,b = b,a+b
        yield a
def square(nums):
    for num in nums:
        yield num**2

for element in square(fibonnacci(8)):
    print(element)


print("After loop")
print(sum(square(fibonnacci(5))))