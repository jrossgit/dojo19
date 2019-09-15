from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pyglet.gl import *
from pyglet.window import key

from cocos.actions import *
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
from haiku import generate_haiku

from time import time

def get_steps(index):
    
    return Scene(FontLayer(title="", subtitle='\n'.join(generate_haiku())), SpriteMoveTo(index))

class SpriteLayer(Layer):

    is_event_handler = True     #: enable pyglet's events

    def __init__(self, index=1):
        super(SpriteLayer, self).__init__()
        self.index = index

        self.image = pyglet.resource.image('flat-black-l.png')
        self.image.anchor_x = self.image.width
        self.image.anchor_y = self.image.height

    def on_key_release(self, keys, mod):
        # LEFT: go to previous scene
        # RIGTH: go to next scene
        # ENTER: restart scene
        max_steps = 8

        if keys == key.LEFT:
            self.index -= 1
            if self.index < 0:
                self.index = max_steps - 1
        elif keys == key.RIGHT:
            self.index += 1
            if self.index >= 8:
                self.index = 0

        if keys in (key.LEFT, key.RIGHT, key.ENTER):
            director.replace(get_steps(self.index))
            return True

    # def on_exit( self ):
    #    for o in self.objects:
    #        o.stop()

class SpriteMoveTo(SpriteLayer):

    def on_enter(self):
        super(SpriteMoveTo, self).on_enter()

        sprite3 = Sprite(self.image)
        self.add(sprite3)
        x, y = divmod(self.index, 3)

        sprite3.position = x * 100 +100 , y * 100 + 100
        # sprite3.do(MoveTo((620, 300), 1))


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

        self.text_help = pyglet.text.Label("Press LEFT / RIGHT for prev/next test, "
                                           "ENTER to restart test",
                                           font_size=16,
                                           x=director.get_window_size()[0] // 2,
                                           y=20,
                                           anchor_x='center',
                                           anchor_y='center',
                                           batch=self.batch)

    def draw(self):
        super(FontLayer, self).draw()
        self.batch.draw()



if __name__ == "__main__":
    director.init(resizable=True, caption='SuperStepper')
    director.run(get_steps(1))