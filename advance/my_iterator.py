class PowerOfTwo:
    def __init__(self,max = 0):
        self.max = max

    def __iter__(self):
        print("Iter called")
        self.n = 0
        return self

    def __next__(self):
        if(self.n<= self.max):
            result = 2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration


number = PowerOfTwo(5)

num_iter = iter(number)

print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
# print(next(num_iter))


for pows in number:
    print(pows)
    
for pows in number:
    print(pows)