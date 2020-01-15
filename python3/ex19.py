#Functions might be a lot to take in but lets try to see what it can. Explore !

def cheese_and_crackers(cheese_count, boxes_of_crackers): #function name & args
    print(f"The amount of cheese we have {cheese_count}.") #takes arg and prints
    print(f"The amount of Crackers we have {boxes_of_crackers}.")#Same as line 4
    print("That is enough for a party.")
    print("Get a blanket.\n")

print("We can just give the value to the function directly.") #pass by value
cheese_and_crackers(20 , 30)

print("Or We can pass it via variables.")
amount_of_cheese = 24 # this value is passed to cheese_count
amount_of_crackers =20 #this value is passed to boxes_of_crackers
#The variables are passed sequentially
#That means cheese_count=amount_of_cheese & boxes_of_crackers=amount_of_crackers

print("We can even do math inside it.")
cheese_and_crackers(20 + 10 - 1, 30 - 5) #Caculations can be performed too.

print("And we can combine both the variables and math together.")
cheese_and_crackers(amount_of_cheese + 100 , amount_of_crackers + 200)
#Operations can be performed on variables too.
