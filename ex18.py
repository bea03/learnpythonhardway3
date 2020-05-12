#ex18 names, variables, code, functions
#this one is like your scripts with argv
def print_two(*args):
#tell python to define a function with def
#asterisk args *args must go in paraenthesis to work, 
#allows you to pass mult arg values to function but if only can end up passing what is def 
#inside the function. I tried to give three args and error
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')

#ok, that *args is actually pointless we can just do this:
def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')

#this just takes one argument:
def print_one(arg1):
    print(f'arg1: {arg1}')

#this takes no arguemtnts:
def print_none():
    print('I print none')

print_two('Zed', 'Nicole')
print_two_again('Claire', 'Amanda')
print_one('Bender')
print_none()
