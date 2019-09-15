import turtle
import math
import random
import time
import pygame


# pygame.mixer.music.load("Oh My One Oh One.mp3")
# pygame.mixer.music.play(-1)


screen = turtle.Screen()

left_moves = [
    "./imgs/flat-black-l.gif",
    "./imgs/heel-black-l.gif",
    "./imgs/tap-black.gif",
]
right_moves = [
    "./imgs/flat-black-r.gif",
    "./imgs/heel-black-r.gif",
    "./imgs/tap-black.gif",
]

for move in left_moves:
    screen.addshape(move)

for move in right_moves:
    screen.addshape(move)
dancer = turtle.Turtle()
left_foot = turtle.Turtle()
right_foot = turtle.Turtle()

left_foot.shape(left_moves[0])
right_foot.shape(right_moves[0])

left_foot.speed(1)
right_foot.speed(1)
left_foot.penup()
right_foot.penup()
right_foot.goto(60, 0)
left_foot.goto(-60, 0)

scale = 200
while True:
    for _ in range(2):
        left_move = random.choice(left_moves)
        angle = random.randrange(0, 360) / 360 * 2 * math.pi
        x = scale * math.cos(angle)
        y = scale * math.sin(angle)
        left_foot.goto(x, y)
        left_foot.shape(left_move)
        left_foot.stamp()
        time.sleep(1)
        left_foot.shape(left_moves[0])
        left_foot.goto(-60, 0)
        left_foot.clear()

        right_move = random.choice(right_moves)
        angle = random.randrange(0, 360) / 360 * 2 * math.pi
        x = scale * math.cos(angle)
        y = scale * math.sin(angle)
        right_foot.goto(x, y)
        right_foot.shape(right_move)
        right_foot.stamp()
        time.sleep(1)
        right_foot.shape(right_moves[0])
        right_foot.goto(60, 0)
        right_foot.clear()
    for _ in range(3):
        floss_speed = random.randrange(1, 5) / 100
        for frame in range(1, 16):
            image = f"./gif/{frame:04d}.gif"

            screen.addshape(image)
            turtle.shape(image)
            time.sleep(floss_speed)
    turtle.shape("arrow")
