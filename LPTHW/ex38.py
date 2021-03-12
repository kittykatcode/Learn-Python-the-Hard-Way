ten_things = "apple orange crows telephone light sugar"

print("wait ther are not 10 things in ten_things list, lets fix that")

stuff = ten_things.split()
print(stuff)

more_stuff = ["day", "night", "song", "fris-bee", "corn", "banana", "girl", "boy"]
while len(stuff) !=10:
    next_one = more_stuff.pop()
    print("adding :", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now") # this is not working  whayyy

print("there we go :", stuff)

print("lets do one more thigs to stuff")

print(stuff[1])
print(stuff[-1]) # what doea this do
print(stuff.pop())
print(" ".join(stuff))# what si shappening
print("#".join(stuff[3:5])) # ok what now
