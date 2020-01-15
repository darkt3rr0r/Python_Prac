from sys import argv
#we are gonna import some features known as modules aka libraries.
#argv --- Argument Variables
#Explain the WYSS section
#In this exercise we are combining the concept of argv and input()
#Both are ways of providing input to your script. But, input() takes input from
#user while script is running but argv does it before running the script.
script, first, second, third = argv #Basically argv unpacks the value inside it
#to different variables in this case. It takes the arguments and they are divided
#So when we are providing the argv with arguments (4 in this case) they are
#assigned from left to right.

print("The script is called:",script)
print("Your first variable is:", first)
print("Your second variable is", second)
print("Your third variable is", third)

name = input("Name ? ")
print(f"So you are {name}.")
