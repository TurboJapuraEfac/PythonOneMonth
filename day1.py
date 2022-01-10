import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samual L. Jackson",
          "Buddhika Weerasinghe"]

random_bar = random.choice(bars)
random_person1 = random.choice(people)
random_person2 = random.choice(people)

print(f"How about you go to {random_bar} with {random_person1} and {random_person2}")

a = 1
b = 2
c = a + b
print("c is" ,c)

# Variables are just nicknames
# there plain, lowercase words
# examples: x, y, banana, phone_a_quail

name = "Mattan Griffel"
orphan_fee = 200
teddy_bear_fee = 121.80

total = orphan_fee + teddy_bear_fee

print(name, "the total will be", total)