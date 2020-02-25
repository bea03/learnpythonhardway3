# do not want to 'hard code' a file name but prompt for it using argv or input()

from sys import argv

script, filename = argv

txt = open(filename)

print(f'here is your file {filename}')
print(txt.read())

print('type filename again: ')
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
