import pyttsx3
import time

CALLS = {
    "F": "Step Forwards",
    "B": "Step Bak",
    "L": "Step Left",
    "R": "Step Right",
    "ROT": "About turn",
    "CLAP": "Clapp"
}


class Caller:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 140)

    def say_command(self, cmd):
        call = CALLS.get(cmd, cmd)
        t = time.time()
        self.engine.say(call)
        self.engine.runAndWait()
        time.sleep(time.time()+1.5-t)

    def call(self, cmds):
        for cmd in cmds:
            self.say_command(cmd)


TEST_DANCE = [
    "B",
    "F",
    "R",
    "L",
    "B",
    "CLAP",
    "ROT"
]


def test():
    Caller().call(TEST_DANCE)


if __name__ == "__main__":
    test()
