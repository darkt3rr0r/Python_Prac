#Trying to copy one file into another
#We have ""removed "" extra functionalities as we dont need them to copy.
#We have to write the code in 1 line.

from sys import argv; spt, fr, to = argv; open(to,'w').write(open(fr).read())
