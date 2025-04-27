def power_of_two(max):
    nums = [item for item in range(0,max+1)]
    for n in nums:
        result = 2 **n
        yield result

two_gens = power_of_two(5)

print(next(two_gens))
print(next(two_gens))
print(next(two_gens))
print(next(two_gens))
print(next(two_gens))
print(next(two_gens))
# print(next(two_gens))