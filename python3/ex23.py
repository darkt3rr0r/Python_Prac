#Use the languages.txt file in the repo.
#The languages.txt file simply contains a list of human language names that
#are encoded in UTF-8.

import sys
script , input_encoding, error = sys.argv
#script variable means the name of the program.py file
#input_encoding variable get passed to main() in the variable 'encoding'
#error is passed to main() in the variable 'errors'

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding , errors):
        next_lang = line.strip() #strip function removes the new line character from all the lines
        raw_bytes = next_lang.encode(encoding, errors=errors)
        cooked_string = raw_bytes.decode(encoding, errors=errors)

        print(raw_bytes, "<=====>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
