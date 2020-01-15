#Learning how to take input in python and playing around with it.
print "How old are you?",
age = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "How tall are you?",
height = raw_input()
print "You are %r years old , %s tall , % r heavy." %(age , height , weight) #Using %s instead of %r to avoid the the escaping of quote in the case %r. 
