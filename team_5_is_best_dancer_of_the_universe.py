import random
from enum import Enum
from enum import auto
from typing import NamedTuple

from cocos.actions import Delay
from cocos.actions import Move
from cocos.actions import MoveBy
from cocos.actions import MoveTo
from cocos.actions import Repeat
from cocos.actions import RotateBy
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite


class Leg(Enum):
    LEFT = auto()
    RIGHT = auto()


class DanceMove(NamedTuple):
    dx: int
    dy: int
    # speed: int
    leg: Leg


#left_leg_up = DanceMove(0, 10, Leg.LEFT)
# left_leg_up = DanceMove(0, 10, Leg.LEFT)



class HelloWorld(Layer):
    def __init__(self):
        super().__init__()
        self.left_foot = Sprite('./images/flat-black-l.png')
        self.right_foot = Sprite('./images/flat-black-r.png')

        self.left_foot.position = 200, 200
        self.right_foot.position = 300, 200
        self.add(self.left_foot)
        self.add(self.right_foot)
        #while True:
        # leg = random.choice((self.left_foot, self.right_foot))

        right = [
            MoveBy((100, 0), 1),
            Delay(1),
            MoveBy((-100, 0), 1),
            Delay(1)
        ]
        left = [
            Delay(1),
            MoveBy((100, 0), 1),
            Delay(1),
            MoveBy((-100, 0), 1)
        ]

        self.right_foot.do(Repeat(sum(right, Delay(0))))
        self.left_foot.do(Repeat(sum(left, Delay(0))))

        # self.left_foot.do(RotateBy(360, duration=3))

    def on_key_press(self, key, modifiers):
        print("key pressed")
        self.left_foot.do(RotateBy(360, duration=3))


if __name__ == "__main__":
    print("start")
    director.init()
    layer = HelloWorld()
    scene = Scene(layer)
    director.run(scene)