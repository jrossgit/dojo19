#
# cocos2d
# http://python.cocos2d.org
#

from __future__ import division, print_function, unicode_literals

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pyglet.gl import *
from pyglet.window import key

from cocos.actions import *
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite


class SpriteLayer(Layer):

    is_event_handler = True  #: enable pyglet's events

    def __init__(self, index=1):
        super(SpriteLayer, self).__init__()
        self.index = index

        self.image = pyglet.resource.image("grossini.png")
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2

        self.image_sister1 = pyglet.resource.image("grossinis_sister1.png")
        self.image_sister1.anchor_x = self.image_sister1.width // 2
        self.image_sister1.anchor_y = self.image_sister1.height // 2

        self.image_sister2 = pyglet.resource.image("grossinis_sister2.png")
        self.image_sister2.anchor_x = self.image_sister2.width // 2
        self.image_sister2.anchor_y = self.image_sister2.height // 2

    def on_key_release(self, keys, mod):
        self.do_move(MoveTo(300, 150))
        self..do_move()

        # if keys in (key.LEFT, key.RIGHT, key.ENTER):
        #     director.replace(get_sprite_test(self.index))
        #     return True


class BackgroundLayer(Layer):

    is_event_handler = True

    def __init__(self):
        super(BackgroundLayer, self).__init__()
        self.batch = pyglet.graphics.Batch()
        self.image = pyglet.resource.image("background.jpg")
        self.background_sprite = Sprite(self.image)
        self.background_sprite.x = self.image.width // 2
        self.background_sprite.y = self.image.height // 2
        self.add(self.background_sprite)

    def draw(self):
        super(BackgroundLayer, self).draw()
        self.batch.draw()


class DanceMoveLayer(SpriteLayer):
    scheduled = False

    def __init__(self):
        super().__init__()
        self.image = pyglet.resource.image("grossini.png")
        self.sprite = Sprite(self.image)
        self.add(self.sprite)

    def do_move(self, move):
        self.sprite.do(move)

    def on_enter(self):
        super().on_enter()


# class SpriteDelay(SpriteLayer):
#     def on_enter(self):
#         super(SpriteDelay, self).on_enter()
#         sprite = Sprite(self.image)

#         self.add(sprite)
#         sprite.position = (120, 100)

#         move = MoveBy((250, 0), 3)
#         jump = JumpBy((-250, 0), 100, 4, 3)

#         sprite.do(move + Delay(5) + jump)


# dance_scene = Scene(BackgroundLayer())


if __name__ == "__main__":
    director.init(800, 533, do_not_scale=True, caption="Cocos - Sprite demo")
    dancer = DanceMoveLayer()
    dance_scene = Scene(BackgroundLayer(), dancer)
    director.run(dance_scene)

