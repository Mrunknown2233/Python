#inner function 
def print_msg(msg):
    def printer():
        print(msg)
    #printer()  ->This wont show the output as the function printer isn't called

print_msg("Hello world")

def outer_function():
    a = 5
    def inner_function():
        nonlocal a    #'nonlocal' is the keyword used to refer the global variable if local and global share the same name
                        #here it is use to refer the value of a defined in the outer_function scope
        a = 10
        print(f"Inner a = {a}")
    inner_function()
    print(f"Outer a = {a}")

outer_function()

    