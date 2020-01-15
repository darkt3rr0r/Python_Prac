#A fucntion can return something. The use of return statement
#What happened here ?
#1. Our function is called with two arguments: a and b .
#2.We print out what our function is doing, in this case ”ADDING."
#3.Then we tell Python to do something kind of backward: we return the addition of a + b
#4.Python adds the two numbers. Then when the function ends, any line that runs it will be able to
#assign this a + b result to a variable.


def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some maths using fractions.")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#Some extra maths here and a small puzzle
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
