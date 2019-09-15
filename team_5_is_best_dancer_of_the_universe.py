from itertools import chain

from cocos.actions import Delay
from cocos.actions import MoveBy
from cocos.actions import Repeat
from cocos.actions import RotateBy
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite

def left(speed: float):
    return ((MoveBy((100, 0), speed), Delay(speed)), (Delay(speed), MoveBy((100, 0), speed)))


def right(speed: float):
    return ((Delay(speed), MoveBy((-100, 0), speed)),
     (MoveBy((-100, 0), speed), Delay(speed)))

def front(speed: float):
    return ((Delay(speed), MoveBy((0, 100), speed)), (MoveBy((0, 100), speed), Delay(speed)))

def back(speed: float):
    return ((Delay(speed), MoveBy((0, -100), speed)), (MoveBy((0, -100), speed), Delay(speed)))

class LetsDance(Layer):
    def __init__(self, sequence, bpm):
        super().__init__()
        self.left_foot = Sprite("./images/flat-black-l.png")
        self.right_foot = Sprite("./images/flat-black-r.png")

        self.left_foot.position = 200, 200
        self.right_foot.position = 300, 200
        self.add(self.left_foot)
        self.add(self.right_foot)

        speed = 60 / bpm
        dance = [s(speed) for s in sequence]

        right_leg_sequence = chain(*(step[0] for step in dance))
        left_leg_sequence = chain(*(step[1] for step in dance))

        self.right_foot.do(Repeat(sum(right_leg_sequence, Delay(0))))
        self.left_foot.do(Repeat(sum(left_leg_sequence, Delay(0))))


if __name__ == "__main__":
    director.init()
    director.run(Scene(LetsDance([left, right, front, back], 120)))
