#
# cocos2d
# http://python.cocos2d.org
#

from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
import json 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

import cocos
from cocos.actions import *

# A color layer  is a Layer with the a color attribute

def make_person(position):
    x, y = position
    left = cocos.sprite.Sprite('images/left_arm_sprite.png', scale=0.15, position=(x-40, y))
    right = cocos.sprite.Sprite('images/arm_sprite.png', scale=0.15, position=(x+40, y))
    head = cocos.sprite.Sprite('images/head_sprite.jpg', scale=0.15, position=(x, y+30))

    return {
        'left_arm': left,
        'right_arm': right,
        'head': head,
    }


class HelloWorld(cocos.layer.ColorLayer):

    def __init__(self):
        # blueish color
        super(HelloWorld, self).__init__(64, 64, 224, 255)

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a CocosNode
        # label = cocos.text.Label('Hello, World!',
        #                          font_name='Times New Roman',
        #                          font_size=32,
        #                          anchor_x='center', anchor_y='center')

        # # set the label in the center of the screen
        # label.position = 320, 240
        # self.add(label)

        # similar to cocos.text.Label, a cocos.sprite.Sprite
        # is a subclass of pyglet.sprite.Sprite with the befits of
        # being a CocosNode.
        people = [make_person(((110 * i) + 100, 100 + (50 * i))) for i in range(5)]

        rot = RotateBy(90, duration=1)

        # add the sprite as a child, but with z=1 (default is z=0).
        # this means that the sprite will be drawn on top of the label
        for person in people:
            self.add(person['left_arm'], z=1)
            self.add(person['right_arm'], z=1)
            self.add(person['head'], z=1)

            person['left_arm'].do(Repeat(rot + Reverse(rot)))

        # create a ScaleBy action that lasts 2 seconds
        # scale = ScaleBy(3, duration=2)

        # tell the label to scale and scale back and repeat these 2 actions forever
        # label.do(Repeat(scale + Reverse(scale)))

        # tell the sprite to scaleback and then scale, and repeat these 2 actions forever
        # sprite.do(Repeat(Reverse(scale) + scale))

if __name__ == "__main__":
    with open('basic_moves.json', 'r') as fd: 
        move_json = json.loads(fd.read())
    #    print(move_json)
    #    print(type(move_json))

    actions = {
        ("UP", "UP"): RotateBy(180, duration=10),
        ("DOWN", "UP"): RotateBy(-180, duration=10)
    }


    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # We create a new layer, an instance of HelloWorld
    hello_layer = HelloWorld()

    # tell the layer to perform a Rotate action in 10 seconds.
    # hello_layer.do(RotateBy(360, duration=10))

    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene(hello_layer)

    # And now, start the application, starting with main_scene
    cocos.director.director.run(main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )
