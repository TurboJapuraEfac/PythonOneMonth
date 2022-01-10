def greet(name):
    return f"Hello {name}"

name = greet('Buddhika')
print(name)

def concat(a, b):
    return a + b

print(concat('Hello ', 'Buddhika'))

def age_in_dog_years(age):
    return age * 7
   
print(age_in_dog_years(20))

'''
Function checklist
Function definitions begin with def
A function name can only contain characters or an _ (underscore)
Open parenthesis ( right after function name
Arguments are separated by commas
Each argument must be unique (no duplicate names)
Close parenthesis and use colon ): 
Indent all lines of code in the function with a tab (required)
End function by de-indenting back to the same indent level as the def
'''

# function uppercase and reverse

def uppercaseandreverse(string):
    return string.upper()[::-1]

print(uppercaseandreverse("BuddhikaandShashini"))