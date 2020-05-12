from sys import argv #this imports the argv for use. 
from os.path import exists #this imports exists() for use in checking t/f if exists?

script, from_file, to_file = argv #these are variables being assigned for the args in script command line

print(f"copying from {from_file} to {to_file}")
#no mode arg given for open() because defaul is read mode
#we could do these two on one line, how:
in_file = open('from_file')
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f'Does the output file exist? {exists(to_file)}')
print('Ready, hit RETURN to continue, CTRL-C to abort')
input()
#open to_file and write mode for the mode argument, default is r if ommited
out_file = open(to_file, 'w')
out_file.write(indata)

#print(out_file) <-- this did not print the contents of the file
print('Alright, all done')

out_file.close()
in_file.close()
#open(to_file)
#print(to_file.read()) #perhaps you have to close file before can print the contents?
