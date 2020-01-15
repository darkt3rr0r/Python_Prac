#Script which reads the contents of a file.

from sys import argv

script , filename = argv

print("Welcome to File-Reader Script.")
print("Press Ctrl-C(^c) to abort the script.")
print("Smash the Enter to continue.")
input("Enter the filename : >")

target = open(filename)

print(f"You chose to open {filename}.")
print("Here are the contents of the file.")
print(target.read())

print("Now closing the file.")
target.close()
