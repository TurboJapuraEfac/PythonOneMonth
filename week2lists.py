the_count = [1, 2, 3, 4, 6]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no", "A list inside a list"]]

# for x in list
for number in the_count:
    print("this is count", number)

for stock in stocks:
    print("I like", stock)

for thing in random_things:
    print("This is a random thing", thing)

for thing in random_things:
    if type(thing) == list:
        for thing_inside in thing:
            print("This is a random thing inside a list", thing_inside)
    else:
        print("This is a random thing", thing)


