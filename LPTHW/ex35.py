from sys import exit

def gold_room():
    print("this is room full of gold, how much do u take ?")
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man learn to type a number")

    if how_much < 50:
        print("nice , you are not greedy, you win")
        exit(0)

    else:
        dead("you greedy bastard")

def bear_room():
    print("""there is a bear here,
    bear has a bunch of honey
    fat bear is in front on another door
    How are you going to remove the bear""")

    bear_moved = false

    while True:
        choice = input(">")

        if choice == "take honey":
            dead("the bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door, you can go through the door now")
            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("got no idea what that means")

def cthulhu_room():
    print("bull shit.. do you flee for your life or eat your head?")

    choice = input('>')

    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead("well that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print(why, "good job")
    exit(0)


def start():
    print(""" you are in a dark room,
    there is a door to your right and left..
    which one do you take""")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room untill you starve")

start()
