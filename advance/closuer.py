def make_multiplier_by_n(n):
    # print("n ",n)
    def multiplier(x):
        return x * n
    return multiplier

def print_msg(msg):
    def printer():
        print(msg)
    return printer

closure_function = print_msg("Hello world")
closure_function()

del print_msg

closure_function()

#practical example 

# print("abc")
make_multiplier_by_10 = make_multiplier_by_n(10)
make_multiplier_by_5 = make_multiplier_by_n(5)

print(make_multiplier_by_10(2))
print(make_multiplier_by_5(1))