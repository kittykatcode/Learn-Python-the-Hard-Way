people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take cars")
elif cars < people:
    print("we should not take the cars")
else:
    print("we can't decide")

if trucks > cars:
    print("thats too many trucks")
elif trucks < cars:
    print("we could take cars")
else:
    print("we still can't decide")

if people > trucks:
    print("ohh ohh hoo")
else:
    print("fine, lets just stay at home")
