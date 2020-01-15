#Names, Variables, Code, Functions
#Functions finally. What they exactly do in a gist.
#1. They take arguments like argv.
#2. They name pieces of codes as variables name strings and numbers.
#3. They are like mini scripts when we combine 1 and 2.
#We can make a function in python using the key word "def" without the quotes
#def means define.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_one(arg1):
    print (f"arg1 : {arg1}")

def print_none():
    print("I got nothing!")

print_two("A","B")
print_two_again("BigDaddy", "Naru0tail")
print_one("One")
print_none()
