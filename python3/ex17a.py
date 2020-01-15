#Trying to copy one file into another
#We have been asked to remove extra functionalities as we dont need them to copy
from sys import argv
from os.path import exists

script , from_file , to_file = argv

in_file = open(from_file)
in_data = in_file.read()

print(f"Does the output file exist ? {exists(to_file)}")

out_file = open(to_file ,'w')
out_file.write(in_data)

out_file.close()
in_file.close()
