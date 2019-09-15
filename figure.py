from cocos.skeleton import Bone, Skeleton

import cocos
from cocos.director import director
from cocos.sprite import Sprite
from cocos import skeleton

import pickle

class Figure(Skeleton):

    def __init__(self, offset):
        self.offset = offset
        self.root = root = Bone("body", 70, -180.0, (0. + self.offset, 0.))
        root.add(
            Bone("upper right arm", 30, 120, (0, -70)).add(
                Bone("lower right arm", 30, 30, (0, -30))
            )
        )
        root.add(
            Bone("upper left arm", 30, -120, (0, -70)).add(
                Bone("lower left arm", 30, -30, (0, -30))
        ))

        root.add(
            Bone("right leg", 60, -150, (0, 0))
        )

        root.add(
            Bone("left leg", 60, 150, (0, 0))
        )


        super().__init__(self.root)


class TestLayer(cocos.layer.Layer):
    def __init__(self):
        super(TestLayer, self ).__init__()

        x,y = director.get_window_size()
        
        skel = Figure(-100)

        # create a ColorSkin for our skeleton
        self.skin = skeleton.ColorSkin(skel, (255,255,255,255))
        
        # add the skin to the scene
        self.add( self.skin )
        x, y = director.get_window_size()
        self.skin.position = x/2, y/2

        anim = pickle.load(open('dance.anim', 'rb'))
        self.skin.do(cocos.actions.Repeat(skeleton.Animate(anim)))

if __name__ == "__main__":

    director.init(width=200, height=200)
    test_layer = TestLayer()
    bg_layer = cocos.layer.ColorLayer(0,0,0,255)
    main_scene = cocos.scene.Scene()
    main_scene.add(bg_layer, z=-10)
    main_scene.add(test_layer, z=10)
    main_scene.load_music('audio.mp3')
    main_scene.play_music()
    director.run(main_scene)
    