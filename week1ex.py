# Write a script that takes a dollar amount and recommennds a tip (15%, 18% and 20%)
# Get a name
name = input("What is you're name? ")
print(name)

total = float(input("What is you're bill sub-total? ").strip('$'))
print(total)

tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.20

# print(f"15% is ${tip_15:.2f}")
# print(f"18% is ${tip_18:.2f}")
# print(f"20% is ${tip_20:.2f}")

final1 = total + tip_15
final2 = total + tip_18
final3 = total + tip_20

print(f"If you select 15 % Your total is {final1:.2f}")
print(f"If you select 18 % Your total is {final2:.2f}")
print(f"If you select 20 %Your total is {final3:.2f}")

#########################################################################################################
