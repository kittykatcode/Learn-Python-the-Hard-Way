from sys import exit
from random import randint
from textwrap import dedent



class scene(object):
    def enter(self):
        print("this scene is not yet configured")
        print("subclass it and implement enter()")
        exit(1)


class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map


    def play(self):
        print("^^ Play")
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene()


        while current_scene != last_scene:
            print(">>>> top of while loop current sene:", current_scene,"last Scene :", last_scene)
            #next_scene_name = current_scene.enter()
            #current_scene = self.scene_map.next_scene(next_scene_name)
            print(">>>> end of ehile loop : current sene:", current_scene,"last Scene :", last_scene, "next_scene_name:", next_scene_name)
            #be sure to print out the last scene
        print("end of play : current scene =", current_scene )
        current_scene.enter()


class Death(scene):

    quips = [
    'you died, you kinda suck at this.',
    'your mom would be proud... if you were smarter.',
    'such a luser !',
    "I have a small puppy that's better at this",
    "you'r worse than your Dad's joke"
    ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)


class CentralCorridor(scene):
    def enter(self):
        print(dedent("""
        THe Gothons of planet percal#25 have invaded you ship and
        destroyed your entier crew. you are the last surviving member
        and your last mission is to get the neutron destruct bomb
        from the wepon armory, put it in the bridge , and
        blow the ship up after getting into an escape pod
        you're running down the centeral corriodoorto the wepons armory
        when a Gothon jumped out, red scaly skin, dark grimy teeth,
        and evil clown costume flowing around his hate filled boday,
        He's blocking the door to the Aromory and about to pull a wepon to blast
         """))
        action = input(">")

        if action == 'shoot!':
             print(dedent("""
             Quick on the draw, you yank out your blaster and configured
             and it is at GOthan, his clown coustume is flowing and
             moving around his body, which throws off your aim,
             your laser hits his coustume but misses him entirely.
             this completly ruins his brand new coustume his mother brought him,
             which makes him fly into an insane rage
             and blasts you repetately in the face until you are DEAD.
             then he eats you.
             """))
             return 'Death'
        elif action == "Dodge!":
            print(dedent("""
            Like a world class boxer you dodge you dodge, weave, slip and
            slide right as the GOthon's blaster cranks a laser past your head.
            in the middle of your artful dodge.
            your foot slips and you bang your head on the meatal
            wall and pass out, you wake up shortly after only to
            die as the Gothon stomps on your head and eats you.
            """))
            return 'Death'
        elif action == "tell a joke":
            print(dedent("""
            lucky for you they made you learn  gothon insults in
            the acedmey. you tell the one Gothon joke you know:
            osajf jopaj hfhoif hfjfo, hfoie hgf jour vgwqhe,
            bjfgv hfioegvd diwv gduiwagd,
            nks hiowqgf gdwqfrruhef 0efuuewb huwyf
            THe Gothon stomps ,tries  not to laugh then burst out laughing
            and cant move.
            while he's laughing you run up and shoot square in the head
            putting him down then jumps through the wepon Armory door
            """))
            return 'laser_wepon_armory'
        else:
            print("does not compute")
            return 'central_corridor'


class LaserWeaponArmory(scene):
    def enter(self):
        print(dedent("""
        you do a dive roll into the wepon Armory, crouch and scan
        the room for one more Gothon might be hiding, it's dead quite,
        too quite. You stand up and run far to the side of the room
        and find neutron bomb in its container. There's a keypad blockingon the boxerand
        you need the code to get the bomb out. if you get the code wrong 10 times then
        the lock closes forever and you can't get the bomb.
        the code is a 3 digits
        """))
        code = f"{randint(1,9)}, {randint(1,9)}, {randint(1,9)}"
        guess = input("[Keypad]>")
        guesses = 0
        while guess != code and guesses <10:
            print("BZZZEEDDDDD!")
            guesses +=1
            guess = input("[Keypad]>")

        if guess == code:
            print(dedent("""
            the container clicks open and seal breaks, letting the gas out.
            you grab the neutron bomb and run as fast as you can to the TheBridge
            where you must place itin the right spot."""))
            return 'the_bridge'

        else:
            print(dedent("""
            the lock buzzes one last time and then you head a
            sickinging melting sound as the machanie is fused together,
            youdecide to sit there, and finnaly the gothons blow up the ship
            from there ship and you die """))
            return 'death'


class TheBridge(scene):
    def enter(self):
        print(dedent("""
        you brust on to the bridge with the netron destruct bomb
        under your arm and surprised 5 Gothon who are trying to
        take control of the ship. Each of them has an uglier
        clown costume than the last one.
        they haven't pulled together their wepons out yet,
        as they see the active bomb under your armand don't want ot set it off
        """))
        action = input('>')

        if action == 'throw the bomb':
            print(dedent("""
            In panic you throw the bomb at the group of
            Gothons and make a leap for the door.
            right as you drop it a GOthon shoos you right in the back
            killing you, As you die you see another gothon frantically
            tries to  disarm the bomb.
            you die knowing they will probally blow up when it goes off
            """))
            return 'death'

        elif action == 'slowly place the bomb':
            print(dedent("""
            you point your blaster at he bomb under your arm
            ad the Gothan's put their hands up and start to sweat
            you inc backwards to the door, and then
            carefully place the bomb on the floor, pointing
            your blaster at it.
            you then jump back through the door
            punch close button and blast the lock so the
            gothans can't get out, NOw that the bomb is placed
            you run to the escape pod to get off this tin can.
            """))

            return 'escape_pod'
        else:
            print("Does not compute:")
            return 'the_bridge'



class Escapepod(scene):
    def enter(self):
        print(dedent("""
        you rush through the ship desperately trying to
        the escape pod before the whole ship explode,
        it seems like hardlely any Gothon are on the ship, so your run is
        clearof interference, you get to the chamber with the escape pod,
        and now need to pick one to take. some of them could be
        dmaged but you don'thave time to look,
        there's 5 pods
        which one do you take?
        """))

        good_pod = randint(1,5)
        guess = input("[pod #]>")

        if int(guess) != good_pod:
            print(dedent("""
            you jump into {guess} and hit the eject button.
            the pod escapes out into the void sapce, then
            implodes as the hull ruptures,
            crushing your body into jam-jelly
            """))
            return 'death'
        else :
            print(dedent("""
            you jump into the pod {guess} and hit the eject button.
            the pod easily slides out into space heading to the
            planet below. As it flies to the planet, you look back and see
            your ship implodes then explodes like a bright star,
            taking out the gothon ship at the same time
            You Won !
            """))
            return 'finished'

class Finished(scene):
    def enter(self):
        print("You Won! Good Job")
        return 'finished'
        exit(1)


class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_wepon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': Escapepod(),
    'death': Death(),
    'finished' : Finished()
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val


    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
