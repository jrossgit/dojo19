"""
    test_api

    Copyright TotalSim Ltd, 2019 all rights reserved
        jross (james@totalsim.co.uk)

    The contents of this file are NOT for redistribution
    Please see the README.md file distributed with this source code
"""

from __future__ import division, print_function, unicode_literals

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../images'))

from pyglet.gl import *
from pyglet.window import key

from cocos.actions import *
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite


def get_sprite_test(index):
    d = tests[index]
    return Scene(FontLayer(title=d[0], subtitle=d[1]), d[2](index))


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


class SpriteLayer(Layer):

    is_event_handler = True     #: enable pyglet's events

    def __init__(self, index=1):
        super(SpriteLayer, self).__init__()
        self.index = index

        from os import getcwd
        print (getcwd())

        self.image = pyglet.resource.image('flat-black-l.png')
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2

        self.image_sister1 = pyglet.resource.image('heel-black-r.png')
        self.image_sister1.anchor_x = self.image_sister1.width // 2
        self.image_sister1.anchor_y = self.image_sister1.height // 2

        self.image_sister2 = pyglet.resource.image('tap-black.png')
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

        if keys in (key.LEFT, key.RIGHT, key.ENTER):
            director.replace(get_sprite_test(self.index))
            return True

    # def on_exit( self ):
    #    for o in self.objects:
    #        o.stop()


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


class SpriteRepeatMoveBy(SpriteLayer):

    def on_enter(self):
        super(SpriteRepeatMoveBy, self).on_enter()

        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = 120, 100

        move = MoveBy((150, 0), 0.5)
        rot = RotateBy(360, 0.5)

        sprite.do(Repeat(Place((120, 100)) + rot + move + rot + move + rot + move + rot))


class SpriteScale(SpriteLayer):

    def on_enter(self):
        super(SpriteScale, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = 320, 200

        sprite.do(ScaleTo(10, 5))


class SpriteRotate(SpriteLayer):

    def on_enter(self):
        super(SpriteRotate, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        self.position = 320, 200

        sprite.do(RotateBy(360, 2))


class SpriteJump(SpriteLayer):

    def on_enter(self):
        super(SpriteJump, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        self.position = 120, 100

        sprite.do(JumpBy((400, 0), height=100, jumps=4, duration=3))


class SpriteBezier(SpriteLayer):

    def on_enter(self):
        super(SpriteBezier, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        self.position = 120, 100

        sprite.do(Bezier(foo.curva, 5))


class SpriteSpawn(SpriteLayer):

    def on_enter(self):
        super(SpriteSpawn, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = 120, 100

        jump = JumpBy((400, 0), 100, 4, 5)
        rotate = RotateBy(720, 5)
        sprite.do(jump | rotate)


class SpriteSequence(SpriteLayer):

    def on_enter(self):
        super(SpriteSequence, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = (120, 100)

        bz = Bezier(foo.curva, 3)
        move = MoveBy((0, -250), 3)
        jump = JumpBy((-400, 0), 100, 4, 3)

        sprite.do(bz + move + jump)


class SpriteDelay(SpriteLayer):

    def on_enter(self):
        super(SpriteDelay, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = (120, 100)

        move = MoveBy((250, 0), 3)
        jump = JumpBy((-250, 0), 100, 4, 3)

        sprite.do(move + Delay(5) + jump)


class SpriteBlink(SpriteLayer):

    def on_enter(self):
        super(SpriteBlink, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = (320, 240)

        blink = Blink(10, 2)

        sprite.do(blink)


class SpriteFadeOut(SpriteLayer):

    def on_enter(self):
        super(SpriteFadeOut, self).on_enter()
        sprite1 = Sprite(self.image_sister1)
        sprite2 = Sprite(self.image_sister2)

        self.add(sprite1)
        self.add(sprite2)
        sprite1.position = 200, 240
        sprite2.position = 440, 240

        fadeout = FadeOut(2)
        fadein = FadeIn(2)

        sprite1.opacity = 0
        sprite1.do(fadein)
        sprite2.do(fadeout)


class SpriteRepeat(SpriteLayer):

    def on_enter(self):
        super(SpriteRepeat, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = 120, 100

        jump = JumpBy((400, 0), 100, 4, 3)

        sprite.do(Repeat(Place((120, 100)) + jump))


class SpriteRepeat2(SpriteLayer):

    def on_enter(self):
        super(SpriteRepeat2, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = 120, 100

        jump = JumpBy((400, 0), 100, 4, 3)

        sprite.do(Repeat(jump + Reverse(jump)))


class SpriteRepeatSeq(SpriteLayer):

    def on_enter(self):
        super(SpriteRepeatSeq, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = 120, 100

        jump = JumpBy((400, 0), 100, 4, 2)
        move = MoveBy((0, 100), 1)
        jump2 = JumpBy((-200, 0), 50, 4, 2)

        sprite.do((Place((120, 100)) + jump + move + jump2) * 4)


class SpriteRepeatSeq2(SpriteLayer):

    def on_enter(self):
        super(SpriteRepeatSeq2, self).on_enter()
        sprite = Sprite(self.image)

        self.add(sprite)
        sprite.position = 120, 100

        jump = JumpBy((150, 0), 50, 4, 1)
        move = MoveBy((0, 100), 0.5)
        action = jump * 3 + move * 3 + Reverse(jump) * 3

        sprite.do(Repeat(action + Reverse(action)))


class SpriteTrigger(SpriteLayer):

    def on_enter(self):
        super(SpriteTrigger, self).on_enter()
        sprite = Sprite(self.image)
        self.add(sprite)
        sprite.position = 120, 100

        move = MoveBy((100, 0), 2)

        sprite.do(move + CallFunc(self.say_hello))

    def say_hello(self):
        print("HELLO BABY")

        sprite2 = Sprite(self.image_sister1)
        self.add(sprite2)
        sprite2.position = 270, 110


class SpriteReuseAction(SpriteLayer):

    def on_enter(self):
        super(SpriteReuseAction, self).on_enter()
        sprite1 = Sprite(self.image_sister1)
        sprite2 = Sprite(self.image_sister2)

        self.add(sprite1)
        self.add(sprite2)
        sprite1.position = 120, 250
        sprite2.position = 20, 100

        jump = JumpBy((400, 0), 150, 4, 4)
        sprite1.do(jump)
        sprite2.do(jump)


class SpriteReuseSequence(SpriteLayer):

    def on_enter(self):
        super(SpriteReuseSequence, self).on_enter()
        sprite1 = Sprite(self.image_sister1)
        sprite2 = Sprite(self.image_sister2)

        self.add(sprite1)
        self.add(sprite2)

        sprite1.position = 120, 250
        sprite2.position = 20, 100

        jump = JumpBy((200, 0), 50, 4, 2)
        move = MoveBy((0, 100), 2)

        rotate = RotateBy(360, 2)

        seq = Repeat(jump + move + Reverse(jump))

        sprite1.do(seq)
        sprite2.do(seq)
        sprite2.do(Repeat(rotate))


class SpriteAlterTime(SpriteLayer):

    def on_enter(self):
        super(SpriteAlterTime, self).on_enter()
        sprite1 = Sprite(self.image_sister1)
        sprite2 = Sprite(self.image_sister2)

        self.add(sprite1)
        self.add(sprite2)

        sprite1.position = 20, 100
        sprite2.position = 20, 300

        move1 = MoveBy((500, 0), 3)
        move2 = Accelerate(MoveBy((500, 0), 3))

        sprite1.do(move1)
        sprite2.do(move2)


class SpriteRepeatAlterTime(SpriteLayer):

    def on_enter(self):
        super(SpriteRepeatAlterTime, self).on_enter()
        sprite1 = Sprite(self.image_sister1)
        sprite2 = Sprite(self.image_sister2)

        self.add(sprite1)
        self.add(sprite2)
        sprite1.position = (20, 100)
        sprite2.position = (20, 300)

        action = MoveBy((500, 0), 3)
        move1 = Accelerate(action)
        move2 = action
        sprite1.do(Repeat(move1 + Reverse(move1)))
        sprite2.do(Repeat(move2 + Reverse(move2)))


# accelerate() is a function that is part of actions.py
# It is really simple. Look at it:
# and it is very simple:
#
# def accelerate( t, duration ):
#    return t * (t/duration)
#
# To try some cool effects, create your own alter-time function!

tests = {
    1: ("Test #1 - MoveTo", "sprite.do( MoveTo( (x,y), duration ) )", SpriteMoveTo),
}

if __name__ == "__main__":
    director.init(resizable=True, caption='Cocos - Sprite demo')
    director.run(get_sprite_test(1))
