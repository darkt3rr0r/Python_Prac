#Checking out different file modes such as 'a' and if there is no 'w' specified.
from sys import argv

script , filename = argv

print(f"We are gonna to play with {filename}.")
print("Press Ctrl-C if you wanna abort this.")
print("If you do want that smash the Enter key.")

input("> ")
print("Opening the file.")
target = open(filename,'a') #'w','r','a' are some of the modes you can open the
#file in.
#also if we use 'w' mode we would not have to use truncate as in 'w' mode it will
#automatically remove the contents of the file.

#print("Truncating the file. Goodbye ! ")
#target.truncate()

print("Now I am gonna ask you to enter 3 lines that you want to be added.")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")
formatter ="{}\n{}\n{}\n" #Used this concept in previous ex08.py
#write in 1 line these above lines to avoid repetition using what we learnt.
target.write(formatter.format(line1, line2, line3))

#print(target.read()
#When I tried reading it, It showed an I/O error which means can't write and read
#together. Have to close the file and then only can read work !

print ("Finally closing the file.")
target.close()
