#Trying to copy one file into another
#We have ""removed "" extra functionalities as we dont need them to copy.
#We have to shorten the code a bit.

from sys import argv
from os.path import exists

script , from_file , to_file = argv

in_file = open(from_file).read()

print(f"Does the output file exist ? {exists(to_file)}")

out_file=open(to_file,'w').write(in_file)

print("All done.")
