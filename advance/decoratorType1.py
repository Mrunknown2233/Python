def smart_division(func):
    def inner(a,b):
        print("I am going to divide ",a,"and",b)
        if b == 0:
            print("OOPs! cannot divide")
            return
        return func(a,b)
    return inner


@smart_division
def divide(a,b):
    print(a/b)

divide(10,2)
divide(5,0)