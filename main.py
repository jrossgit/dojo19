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


class DanceMoveLayer:
    pass


# dance_scene = Scene(BackgroundLayer())


if __name__ == "__main__":
    director.init(800, 533, do_not_scale=True, caption="Cocos - Sprite demo")
    dance_scene = Scene(BackgroundLayer())

    director.run(dance_scene)
