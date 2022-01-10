# we can also build lists, first let's start with an empty one
people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")
people.append("Samantha")
people.append("Sara")

# now we can print them out too
print(people)

# and remove some
people.remove("Sarah")
print(people)

for person in people:
    print("Person is:", person)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number , "Square is : ", number * number)

'''
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(number , "Square is : ", number * number)
'''
# Challenge: Print out the square of the numbers 1 to 10
for number in range(1,21):
    print(number, "squared is", number * number)

# How to Access Data in a List

# here's how you access elements of a list
animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

print("They're are this many things:", len(animals))
