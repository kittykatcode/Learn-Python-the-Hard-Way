the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'banana']
change = [1, 'pennies', 2, 'dime', 3, 'quater']
#this is a loop that goes through a list
for a in the_count:
    print(f"hi is the count {a}.")

#same as above
for f in fruits:
    print(f" A fruit of type :{f}")

for i in change:
    print(f"I got {i}")

#building a list
elements = []

for i in range(0,6):
    print(f'adding {i} to the list')

    elements.append(i)

for i in elements:
    print(f"Elements was: {i}.")
