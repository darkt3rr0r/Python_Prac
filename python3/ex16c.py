#list of commands you can give to files
#   close : Closes the file.
#   read : Read the contents of the file.
#   readline : Reads just one line of each line.
#   truncate: Empties the file.
#   write('stuff') : Writes "stuff" to the file.
#   seek(0) : Moves the read/write location to the beginning of the line.

from sys import argv

script , filename = argv

print(f"We are gonna to erase {filename}.")
print("Press Ctrl-C if you wanna abort this.")
print("If you do want that smash the Enter key.")

input("> ")
print("Opening the file.")
target = open(filename,'w') #'w','r','a' are some of the modes you can open the
#file in.

print("Truncating the file. Goodbye ! ")
target.truncate()

print("Now I am gonna ask you to enter 3 lines that you want to be added.")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")
formatter ="{}\n{}\n{}\n" #Used this concept in previous ex08.py
#write in 1 line these above lines to avoid repetition using what we learnt.
target.write(formatter.format(line1, line2, line3))

print ("Finally closing the file.")
target.close()
