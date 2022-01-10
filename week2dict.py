# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

# Note that the key is the thing to the left of the colon, and it has to be a string. But the thing on the right is the value, and that can be any data type. The value can be a string, a number, a list, a dictionary, etc.

print("First state in the dictionary : ", states['NY'])
print("Second state in the dictionary : ", states['PA'])
print("Third state in the dictionary : ", states['CA'])

print(type(states))
print(states.get('NY', 'Not found'))
print(states.get('TX', 'Not Found'))
print(states.keys())
print(states.values())

states['TX'] = 'Texas'
print("New states:" , states)

# user = ['Mattan', 70, 10.5, 'Brown', 'Brown']
user = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
print(user)

########################################################################################################

# Dictionaries and lists can be inside each other

# Lists inside a dictionary
animal_sounds = {
   "cat": ["meow", "purr"],
   "dog": ["woof", "bark"],
   "fox": []
}
print(animal_sounds)

# Dictionaries inside a list

mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}
chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}
sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = [mattan, chris, sarah]
print(people)

for person in people:
    print(person['height'])

for person in people:
    print(person['name'])

for person in people:
    print(person['shoe size'])

#Note this only works because I know all the dictionaries have the 'height' key. A safer option might be:

for person in people:
    print(person.get('height', 'Not found'))















