from itertools import chain

from cocos.actions import Delay
from cocos.actions import MoveBy
from cocos.actions import Repeat
from cocos.actions import RotateBy
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite


class HelloWorld(Layer):
    def __init__(self):
        super().__init__()
        self.left_foot = Sprite("./images/flat-black-l.png")
        self.right_foot = Sprite("./images/flat-black-r.png")

        self.left_foot.position = 200, 200
        self.right_foot.position = 300, 200
        self.add(self.left_foot)
        self.add(self.right_foot)

        speed = 0.5

        left = ((MoveBy((100, 0), speed), Delay(speed)), (Delay(speed), MoveBy((100, 0), speed)))

        right = ((Delay(speed), MoveBy((-100, 0), speed)), (MoveBy((-100, 0), speed), Delay(speed)))

        front = ((Delay(speed), MoveBy((0, 100), speed)), (MoveBy((0, 100), speed), Delay(speed)))

        back = ((Delay(speed), MoveBy((0, -100), speed)), (MoveBy((0, -100), speed), Delay(speed)))

        dance = [left, right, front, back]

        right_leg_sequence = chain(*(step[0] for step in dance))
        left_leg_sequence = chain(*(step[1] for step in dance))

        self.right_foot.do(Repeat(sum(right_leg_sequence, Delay(0))))
        self.left_foot.do(Repeat(sum(left_leg_sequence, Delay(0))))

    def on_key_press(self, key, modifiers):
        print("key pressed")
        self.left_foot.do(RotateBy(360, duration=3))


if __name__ == "__main__":
    print("start")
    director.init()
    layer = HelloWorld()
    scene = Scene(layer)
    director.run(scene)
