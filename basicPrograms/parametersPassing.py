def funct1(a,b,c):
    print(a,b,c)

def funct2(a,b,c=10):
    print(a,b,c)


funct1(10,20,30)  #positional arguments
funct1(b = 30, c = 10, a = 20)  #keyworded arguments


funct2(c=100,a = 10, b = 40)
funct2(10,20)