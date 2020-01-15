#Trying to copy one file into another

from sys import argv
from os.path import exists

script , from_file , to_file = argv

print(f"Copying {from_file} to {to_file}.")

#Can write in 1 Line ?
in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long.")

print(f"Does the output file exist ? {exists(to_file)}")
print("Ready ? Smash the Enter key or CTRL-C if you a chicken.")
input("> ")

out_file = open(to_file ,'w')
out_file.write(in_data)

out_file.close()
in_file.close()
