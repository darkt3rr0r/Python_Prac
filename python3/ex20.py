from sys import argv

script , input_file = argv

def print_all(f):  #Takes filename as arg and then prints it contents
    print(f.read())

def rewind(f):  #Just a function
    f.seek(0)  #Sends the cursor at the beginning of the file.

def print_a_line(line_count,f):
    print(line_count,f.readline()) #prints the value of line_count and 1 line
#Inside readline() is code that scans each byte of the
#file until it finds a \n character, then stops reading the file to return what
#it found so far. The file f is responsible for maintaining the current position
#in the file after each readline() call, so that it will keep reading each line.
#You can experiment with this by removing line_count & current_line from script.

current_file =open(input_file) #Opens the file given by user

print("Here are the contents of the file.")
print_all(current_file)

print("Let's rewind like a mix-tape and as if it's the 90's")
rewind(current_file)

print("Now here we go again.")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line =current_line + 1
print_a_line(current_line,current_file)
#The readline() function returns the \n that’s
#in the file at the end of that line. Add a end = "" at the end of your print
#function calls to avoid adding double \n to every line.
