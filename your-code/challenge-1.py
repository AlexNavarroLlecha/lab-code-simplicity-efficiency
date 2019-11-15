"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""


print('Welcome to this calculator!')

print('It can add and subtract whole numbers from zero to five')

str_numbers = (['zero', 'one','two', 'three', 'four', 'five'])

ops = (['plus', 'minus'])

##make a dictionary to match the string with their respective int.
numbers = ([0,1,2,3,4,5,])
dict_numbers =dict(zip(str_numbers,numbers))

#################Main Functions for the doomie calculator:

#Input the first number:

def request_a(str_numbers):
    a = input('Please choose your first number (zero to five): ')
    while a not in str_numbers:
            a = input('''Please, I cannot understand your input, please choose your first number (zero to five): ''')
    return a

# Input the '+' or '-'

def request_b(ops):
    b = input('What do you want to do? plus or minus: ')
    while b not in ops:
            b = input('''Please, I cannot understand your input, please tell me what do you want to do? plus or minus: ''')
    return b


#Input the second number

def request_c(str_numbers):
    c = input('Please choose your second number (zero to five): ')
    while c not in str_numbers:
            c = input('''Please, I cannot understand your input, please choose your first number (zero to five): ''')
    return c



#Does the sum or the minus of both numbers.

def calculation(a,b,c,dict_numbers):
    if b == 'plus':
        return  dict_numbers[a] + dict_numbers[c]
    else:
        return dict_numbers[a] - dict_numbers[c]

# convert the number into absolut value to erase the negative if their is.    
    
def convert_int(dict_numbers,result):
    for el in dict_numbers:
        if dict_numbers[el] == abs(result):
            return  el

# Print the final result.        
        
def declaration(a,b,c,result_int_to_str,result):
    if result  >= 0:
        return print(f'"{a} {b} {c} equals {result_int_to_str}')
    else :
        return print(f'"{a} {b} {c} equals negative {result_int_to_str}')

################


###request of inputs
a = request_a(str_numbers)
b = request_b(ops)
c = request_c(str_numbers)

###make the computation
result = calculation(a,b,c,dict_numbers)

###transform the int into a string
result_int_to_str = convert_int(dict_numbers,result)

###make the declaration of values
declaration(a,b,c,result_int_to_str,result)

    
    
    
    



