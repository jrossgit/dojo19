from __future__ import division, print_function, unicode_literals
import argparse
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pyglet.gl import *
from pyglet.window import key

from cocos.actions import *
from cocos.director import director
from cocos.layer import Layer, ColorLayer
from cocos.scene import Scene
from cocos.sprite import Sprite

#import foo      # Bezier configurations


def get_dance(index):
    d = dances[index]
    layer = ColorLayer(0, 255, 0, 100)
    s = Scene(FontLayer(title=d[0], subtitle=d[1]), d[2](index))
    s.add(layer)
    # return Scene(FontLayer(title=d[0], subtitle=d[1]), d[2](index))
    return s


class FontLayer(Layer):

    def __init__(self, title="Sprite Exmaple #", subtitle="Goto()"):
        super(FontLayer, self).__init__()

        self.title = title
        self.subtitle = subtitle

        self.batch = pyglet.graphics.Batch()

        self.text_title = pyglet.text.Label(self.title,
                                            font_size=32,
                                            x=5,
                                            y=director.get_window_size()[1],
                                            anchor_x='left',
                                            anchor_y='top',
                                            batch=self.batch)

        self.text_subtitle = pyglet.text.Label(self.subtitle,
                                               multiline=True,
                                               width=600,
                                               font_size=16,
                                               x=5,
                                               y=director.get_window_size()[1] - 80,
                                               anchor_x='left',
                                               anchor_y='top',
                                               batch=self.batch)

    def draw(self):
        super(FontLayer, self).draw()
        self.batch.draw()


class SpriteLayer(Layer):

    is_event_handler = True     #: enable pyglet's events

    def __init__(self, index=1):
        super(SpriteLayer, self).__init__()
        self.index = index

        # self.image = pyglet.resource.image('grossini.png')
        # self.image.anchor_x = self.image.width // 2
        # self.image.anchor_y = self.image.height // 2
        #
        # self.image_sister1 = pyglet.resource.image('grossinis_sister1.png')
        # self.image_sister1.anchor_x = self.image_sister1.width // 2
        # self.image_sister1.anchor_y = self.image_sister1.height // 2
        #
        # self.image_sister2 = pyglet.resource.image('grossinis_sister2.png')
        # self.image_sister2.anchor_x = self.image_sister2.width // 2
        # self.image_sister2.anchor_y = self.image_sister2.height // 2

        self.image_left = pyglet.resource.image('images/flat-white-l.png')

        self.image_left.anchor_x = self.image_left.width // 2
        self.image_left.anchor_y = self.image_left.height // 2
        self.image_right = pyglet.resource.image('images/flat-white-r.png')

        self.image_right.anchor_x = self.image_right.width // 2
        self.image_right.anchor_y = self.image_right.height // 2

    def on_key_release(self, keys, mod):
        pass
        # LEFT: go to previous scene
        # RIGTH: go to next scene
        # # ENTER: restart scene
        # if keys == key.LEFT:
        #     self.index -= 1
        #     if self.index < 1:
        #         self.index = len(dances)
        # elif keys == key.RIGHT:
        #     self.index += 1
        #     if self.index > len(dances):
        #         self.index = 1
        #
        # if keys in (key.LEFT, key.RIGHT, key.ENTER):
        #     director.replace(get_dance(self.index))
        #     return True


class SpriteMoveTo(SpriteLayer):

    def on_enter(self):
        super(SpriteMoveTo, self).on_enter()

        sprite3 = Sprite(self.image)
        self.add(sprite3)
        sprite3.position = 320, 300
        sprite3.do(MoveTo((620, 300), 4))


class SpriteMoveBy(SpriteLayer):

    def on_enter(self):
        super(SpriteMoveBy, self).on_enter()

        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = 320, 200

        move = MoveBy((150, 0), 3)
        sprite.do(move)

class Jive(SpriteLayer):

    def on_enter(self):
        super(Jive, self).on_enter()

        leftFoot = Sprite(self.image_left)
        rightFoot = Sprite(self.image_right)

        self.add(leftFoot)
        self.add(rightFoot)

        leftFoot.position = 400, 250
        rightFoot.position = 500, 250

        #left down
        down = MoveBy((0, -100), 1)
        #left.do(move)

        #left up and left
        left_up = MoveBy((-100, 100), 1)
        #left.do(move2)

        left = MoveBy((-100, 0), 1)

        right = MoveBy((100, 0), 1)


        leftFoot.do(Repeat(down + left_up + Delay(1) + left + Delay(2) + right + Delay(1) + right))
        rightFoot.do(Repeat(Delay(2) + left + Delay(1) + left + right + Delay(1) + right + Delay(1)))


class Waltz(SpriteLayer):

    def on_enter(self):
        super(Waltz, self).on_enter()

        leftFoot = Sprite(self.image_left)
        rightFoot = Sprite(self.image_right)

        self.add(leftFoot)
        self.add(rightFoot)

        leftFoot.position = 200, 200
        rightFoot.position = 300, 200

        left = MoveBy((-100, 0), 1)

        right = MoveBy((100, 0), 1)

        up = MoveBy((0, 100), 1)
        down = MoveBy((0, -100), 1)
        up_right = MoveBy((100, 100), 1)
        down_left = MoveBy((-100, -100), 1)

        leftFoot.do(Repeat(up + Delay(1) + right + Delay(1) + down_left + Delay(1)))
        rightFoot.do(Repeat(Delay(1) + up_right + Delay(1) + down + Delay(1) + left))



dances = {
    1: ('Learn to Dance', "Jive!", Jive),
    2: ('Learn to Dance', 'Waltz', Waltz),
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dance', choices=['jive', 'waltz'], help='Please select a dance to learn')

    args = parser.parse_args()

    director.init(resizable=True, caption='Cocos - Sprite demo')
#    director.window.set_fullscreen(True)
    if args.dance == 'jive':
        director.run(get_dance(1))
    elif args.dance == 'waltz':
        director.run(get_dance(2))