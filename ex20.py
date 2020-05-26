#ex20 functions files

#this line allows us to use argv (variables in script line)
from sys import argv

#this line assigns argv
script, input_file = argv

#this line defines a function called print_all() that takes in an arg f
def print_all(f):
    #this line prints what is passed into print_all by reading the file
    print(f.read())

#this function starts back at beginning at char[0]
def rewind(f):
    f.seek(0)

#this function prints a line within the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

#assigns current_file to the input_file
current_file = open(input_file)

print("first let's print the whole file:\n")

print_all(current_file)

print("now let's rewind like a tape.")

rewind(current_file)

print("now let's print 3 lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
