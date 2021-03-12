print("""
you enter in adark room
with TWO doors
Do you go through DOOR '1' or DOOR '2' ?
""")

door = input(" ")

if door == '1':
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


elif door == '2':
    print("""
    you stare into the endless abyss at Cthulhu's retina
    what will you choose ?
    1. blueberryies
    2. yellow jacket
    3. yelling melodies
    """)

    insanity = input('>')
    if insanity == '1' or insanity =='2':
        print("your body survive powered by the mind of jello")
        print(" Good Job !")
    else:
        print("Insanity rots your eyes in a pool of muck")
        print('Good Job !')

else:
   print("you stumble on a kinfe and die. GOOD JOB!")
