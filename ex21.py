def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f'Subtracting {a} + {b}')
    return a - b

def multiply(a, b):
    print(f'Multiplying {a} * {b}')
    return a * b

def divide(a, b):
    print(f'Dividing {a} / {b}')
    return a / b

print('let us do some math')

age = add(30, 5)
height = subtract (68, 5)
weight = multiply (60, 5)
iq = divide(1000, 5)

print(f'Age: {age} Height: {height} Weight: {weight} IQ: {iq}')

#a puzzle for extra credit
print('here is a puzzle.')

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f'this becomes: {what}. Can you do it by hand?')
