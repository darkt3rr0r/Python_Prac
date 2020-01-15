print("Let's practise everything we have learnt.")
print('You need to know \' about how escape sequences work with \\')
print('\n newlines and \t tabs')

poem = """
\tI still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
\n\tAnd I cannot change you so I must replace you (oh)
"""
print("-" * 10)
print(poem)
print("-" * 10)

five = 10 - 2 + 3 - 6 
print(f"This should be {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans /1000
	crates = jars /100
	return jelly_beans, jars, crates

start_point = 10000

#Remember this was another way of formating string
print("With a starting point of : {}".format(start_point))
#Remember this is the one I feel is more convenient to use.
print(f"We have {beans} beans, jars {jars} and crates {crates}.") #Concept of tuple

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We have {} beans, {} jars and {} crates.".format(*formula))