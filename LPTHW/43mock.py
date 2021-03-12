
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
        last_scene = self.scene_map.next_scene('finished')


        while current_scene != last_scene:
            print(">>>> top of while loop current sene:", current_scene,"last Scene :", last_scene)
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            print(">>>> end of ehile loop : current sene:", current_scene,"last Scene :", last_scene, "next_scene_name:", next_scene_name)
            #be sure to print out the last scene
        print("end of play : current scene =", current_scene )
        current_scene.enter()

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
