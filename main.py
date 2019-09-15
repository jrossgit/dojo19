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


class FontLayer(Layer):
    def __init__(self, title="Sprite Exmaple #", subtitle="Goto()"):
        super(FontLayer, self).__init__()

        self.title = title
        self.subtitle = subtitle

        self.batch = pyglet.graphics.Batch()

        self.text_title = pyglet.text.Label(
            self.title,
            font_size=32,
            x=5,
            y=director.get_window_size()[1],
            anchor_x="left",
            anchor_y="top",
            batch=self.batch,
        )

        self.text_subtitle = pyglet.text.Label(
            self.subtitle,
            multiline=True,
            width=600,
            font_size=16,
            x=5,
            y=director.get_window_size()[1] - 80,
            anchor_x="left",
            anchor_y="top",
            batch=self.batch,
        )

        self.text_help = pyglet.text.Label(
            "Press LEFT / RIGHT for prev/next test, " "ENTER to restart test",
            font_size=16,
            x=director.get_window_size()[0] // 2,
            y=20,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )

    def draw(self):
        super(FontLayer, self).draw()
        self.batch.draw()


class SpriteLayer(Layer):

    is_event_handler = True  #: enable pyglet's events

    def __init__(self, index=1):
        super(SpriteLayer, self).__init__()
        self.index = index

        self.image = pyglet.resource.image("grossini.png")
        self.image.anchor_x = self.image.width // 2

    def on_key_release(self, keys, mod):
        pass


class BackgroundLayer(Layer):

    is_event_handler = True

    def __init__(self):
        super(BackgroundLayer, self).__init__()
        self.batch = pyglet.graphics.Batch()
        self.image = pyglet.resource.image("background.jpg")

    def draw(self):
        super(BackgroundLayer, self).draw()
        self.batch.draw()


class DanceMoveLayer:
    pass


# dance_scene = Scene(BackgroundLayer())


if __name__ == "__main__":
    director.init(800, 600, do_not_scale=True, caption="Cocos - Sprite demo")
    dance_scene = Scene(BackgroundLayer())

    director.run(dance_scene)
