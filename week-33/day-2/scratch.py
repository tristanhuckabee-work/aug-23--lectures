# Booleans
# in python # in js
print(True)              # True
print(False)             # False
print(True and True)     # True
print(False or True)     # True
print(not True or False) # False
"""
Falsey Values

None, False
0, 0.00
Empty Sequences or Collections
- ''
- []
- ()
- {}
- set()
- range(0)
"""

# Strings
color = 'red'
color_two = "blue"

## Escaping Characters
sentence = 'My name\'s Tristan!'

## Multiline-Strings
big_one = '''
    This
    is
    a
    string.
'''
## String Length
print(len(big_one))
## Indexing Strings
print(color_two[0])    # b
print(color_two[-1])   # e

print(color_two[1:-1]) # lu
print(color_two[1:3]) # lu
print(color_two[0:])   # blue
print(color_two[:2])   # bl

# print(color_two[42])   # error
print(color_two[42:])  # empty

## Formatting
first_name = "Tristan"
last_name = "Huckabee"
print('Your name is {0} {1}'.format(first_name, last_name))
print(f'Your name is {first_name} {last_name}')


# Numbers
# Integers
print(42)
print(int(16.2))

# Floats (decimals)
print(3.14)
print(float(96))
print(1e-2)

print(2**2) # 4
print(9 / 2) # 4.5
print(9 // 2) # 4
print(9 % 2) # 1
