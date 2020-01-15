from sys import argv

script , input_file = argv

def print_all(f):  #Takes filename as arg and then prints it contents
    print(f.read())

def rewind(f):  #Just a function
    f.seek(0)  #Sends the cursor at the beginning of the file.

def print_a_line(line_count,f):
    print(line_count,f.readline(),end='') #prints the value of line_count and 1 line

current_file =open(input_file) #Opens the file given by user

print("Here are the contents of the file.")
print_all(current_file)

print("Let's rewind like a mix-tape and as if it's the 90's")
rewind(current_file)

print("Now here we go again.")

current_line = 1
print_a_line(current_line, current_file)

#What does += do ? Also known as short hand operator
# a+=1 -----> a = a+1
current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
