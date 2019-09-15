

# Python Cocos2d Game Development
# Part 1: Getting Started

# Tutorial: http://jpwright.net/writing/python-cocos2d-game-1/
# Github: http://github.com/jpwright/cocos2d-python-tutorials

# Jason Wright (jpwright0@gmail.com)


# Imports

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director
from cocos import text

# Player class
bpm = 118
freq = 60.0/bpm
factor = bpm/33


from random import randint


class SequenceGenerator:

    steps = []

    moves = ["Slide", "Jump", "Step"]
    directions = {"Forward": (0, 1), "Backward": (-1, 0), "Right": (1, 0), "Left": (-1, 0)}
    for move in moves:
        for direction in directions.keys():
            step = direction + move
            steps.append(step)
    TOTAL_MOVES = 16


    def generate(self):

        return [self.steps[randint(0, len(self.steps) - 1)] for _ in range(self.TOTAL_MOVES)]


class Step(actions.Move):
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
  def step(self, dt):
    
    super(Step, self).step(dt) # Run step function on the parent class.
    
    # Determine velocity based on keyboard inputs.
    #velocity_x = 100 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
    #velocity_y = 100 * (keyboard[key.UP] - keyboard[key.DOWN])
    velocity_x = 0
    velocity_y = factor * bpm

    # Set the object's velocity.
    self.target.velocity = (velocity_x, velocity_y)


class Pulse(actions.Blink):

  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
  def step(self, dt):
    super(Pulse, self).step(dt)  # Run step function on the parent class.

    # Determine velocity based on keyboard inputs.
    # velocity_x = 100 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
    # velocity_y = 100 * (keyboard[key.UP] - keyboard[key.DOWN])
    velocity_x = 0
    velocity_y = 0

    # Set the object's velocity.
    self.target.velocity = (velocity_x, velocity_y)

# Main class

steps = [ "", "SR", "JF", "JB", "", "SL" ]
sprites = []


my_generator = SequenceGenerator()
steps = my_generator.generate()

def main():
  global keyboard # Declare this as global so it can be accessed within class methods.
  
  # Initialize the window.
  director.init(width=800, height=600, do_not_scale=True, resizable=True)

  layers = []
  # Create a layer and add a sprite to it.
  player_layer = layer.Layer()

  counter = 0
  for step in steps:
    a_sprite = sprite.Sprite('feet.png')
    player_layer.add(a_sprite)
    # Set initial position and velocity.
    a_sprite.position = (200, 300 * (counter * -1))
    a_sprite.velocity = (0, 0)

    # Set the sprite's movement class.
    a_sprite.do(Step())

    title = text.Label(
      step, (200,  300 * (counter * -1)), font_name='Gill Sans', color=(255,255,255,255),
      font_size=64, anchor_x='center', anchor_y='center')
    title.velocity = (0,0)
    title.do(Step())
    player_layer.add(title)

    counter = counter + 1

  pulse_layer = layer.Layer()

  a_sprite = sprite.Sprite('feet.png')
  pulse_layer.add(a_sprite)
  # Set initial position and velocity.
  a_sprite.position = (500, 300)
  a_sprite.velocity = (0, 0)

  # Set the sprite's movement class.
  a_sprite.do(actions.Blink(10000, freq * 10000))

  layers.append(player_layer)
  layers.append(pulse_layer)

  # Create a scene and set its initial layer.
  main_scene = scene.Scene(*layers)

  # Attach a KeyStateHandler to the keyboard object.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)

  # Play the scene in the window.
  director.run(main_scene)

if __name__ == '__main__':
    main()


