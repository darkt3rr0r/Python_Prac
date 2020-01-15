#Let's learn a bit more about how Strings work and how the % symbol works in python
types_of_people = 10
x = f"There are {types_of_people} of people."

binary = "binary"
do_not = "don't"
y =f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny ? ! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side. "

print (w + e)

#Related to python 2
# % r we use for debugging as it displays the raw data of the variable.
# at line  10 we use '%s' to print a string which had double quote and brought it to single quote


#Study Drills: Solution 1. Commenting every line 2. Find all places where a string is put inside a string. 3. 4 is final ? 4. What is happening in w+e ?
#why is there a {} inside joke_evaluation ? It's for the use of joke_evaluation.format()
