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
        self.image.anchor_y = self.image.height // 2

        self.image_sister1 = pyglet.resource.image("grossinis_sister1.png")
        self.image_sister1.anchor_x = self.image_sister1.width // 2
        self.image_sister1.anchor_y = self.image_sister1.height // 2

        self.image_sister2 = pyglet.resource.image("grossinis_sister2.png")
        self.image_sister2.anchor_x = self.image_sister2.width // 2
        self.image_sister2.anchor_y = self.image_sister2.height // 2

    def on_key_release(self, keys, mod):
        # LEFT: go to previous scene
        # RIGTH: go to next scene
        # ENTER: restart scene
        if keys == key.LEFT:
            self.index -= 1
            if self.index < 1:
                self.index = len(tests)
        elif keys == key.RIGHT:
            self.index += 1
            if self.index > len(tests):
                self.index = 1

    # def on_exit( self ):
    #    for o in self.objects:
    #        o.stop()




class SpriteMoveTo(SpriteLayer):
    def on_enter(self):
        super(SpriteMoveTo, self).on_enter()


class SpriteMoveBy(SpriteLayer):
    def on_enter(self):
        super(SpriteMoveBy, self).on_enter()


class SpriteRepeatMoveBy(SpriteLayer):
    def on_enter(self):
        super(SpriteRepeatMoveBy, self).on_enter()



class SpriteScale(SpriteLayer):
    def on_enter(self):
        pass


class SpriteRotate(SpriteLayer):
    def on_enter(self):
        pass


class SpriteJump(SpriteLayer):
    def on_enter(self):
        pass


class SpriteBezier(SpriteLayer):
    def on_enter(self):
        pass


class SpriteSpawn(SpriteLayer):
    def on_enter(self):
        super(SpriteSpawn, self).on_enter()


class SpriteSequence(SpriteLayer):
    def on_enter(self):
        super(SpriteSequence, self).on_enter()


class SpriteDelay(SpriteLayer):
    def on_enter(self):
        super(SpriteDelay, self).on_enter()


class SpriteBlink(SpriteLayer):
    def on_enter(self):
        super(SpriteBlink, self).on_enter()
        sprite = Sprite(self.image)


class SpriteFadeOut(SpriteLayer):
    def on_enter(self):
        super(SpriteFadeOut, self).on_enter()


class SpriteRepeat(SpriteLayer):
    def on_enter(self):
        pass


class SpriteRepeat2(SpriteLayer):
    def on_enter(self):
        super(SpriteRepeat2, self).on_enter()


class SpriteRepeatSeq(SpriteLayer):
    def on_enter(self):
        super(SpriteRepeatSeq, self).on_enter()

class SpriteRepeatSeq2(SpriteLayer):
    def on_enter(self):
        super(SpriteRepeatSeq2, self).on_enter()


class SpriteTrigger(SpriteLayer):
    def on_enter(self):
        super(SpriteTrigger, self).on_enter()
        sprite = Sprite(self.image)



class SpriteReuseAction(SpriteLayer):
    def on_enter(self):
        super(SpriteReuseAction, self).on_enter()


class SpriteReuseSequence(SpriteLayer):
    def on_enter(self):
        super(SpriteReuseSequence, self).on_enter()


class SpriteAlterTime(SpriteLayer):
    def on_enter(self):
        super(SpriteAlterTime, self).on_enter()


class SpriteRepeatAlterTime(SpriteLayer):
    def on_enter(self):
        super(SpriteRepeatAlterTime, self).on_enter()



if __name__ == "__main__":
    director.init(resizable=True, caption="Cocos - Sprite demo")
