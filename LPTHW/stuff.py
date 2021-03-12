#if door == 1:
print("""
    there is a gaint bare there eating a cheese cake
    WHAT WOULD YOU DO ?
    1. Take the cake ?
    2. Scream at the bear ?
    """)
bear = input('>')
if bear == '1':
    print("the bear ate ur face off good job")
elif bear == '2':
    print("the bear ate ur leg off")
else:
    print(f" well, doing {bear} is probably better Bear Runs away") # not working
