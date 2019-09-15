import pygame
import time
import random

from settings import Settings

canvas = pygame.display.set_mode((Settings.width, Settings.height))

done = False


class Foot(pygame.sprite.Sprite):
    def __init__(self, canvas, side):
        super().__init__()
        # self.positive_image = pygame.image.load(f'images/{positive_name}')
        # self.negative_image = pygame.image.load(f'images/{negative_name}')
        self.canvas = canvas

        # self.state = 1
        # self.step = 'heel'
        # self.side = side
        # orientation = 0
        # self.location = (10, 10)

        # moves = ['flat', 'heel']
        #
        # feet = {'flat': {}, 'heel': {}}
        # for foot in ['l', 'r']:
        #     for move in moves:
        #         feet[move][foot] = Foot(f'{move}-white-{foot}.png', f'{move}-black-{foot}.png')

        image = pygame.image.load(f'images/flat-white-{side}.png')
        self.image = pygame.transform.scale(image, (45, 100))

        self.rect = self.image.get_rect()
        self.rect.move_ip(300, 300)

    def move(self, x, y):
        self.rect.move_ip(x, y)

    # def set_orientation(self):

    def draw(self):
        canvas.blit(self.image, self.rect)
        # if self.state:
        #     canvas.blit(self.positive_image)
        # else:
        #     canvas.blit(self.negative_image)

# dance = [
#     'p',
#     'l up 2',
#      'p',
#      'r up 2',
#      'r right 1.5',
#     'p'
# ]

with open('dance.txt') as input_file:
    dance = input_file.readlines()


left_foot = Foot(canvas, 'l')
right_foot = Foot(canvas, 'r')
right_foot.move(50, 0)

all_feet = [left_foot, right_foot]


def draw_feet():
    for foot in all_feet:
        foot.draw()


def draw(canvas):
    canvas.fill((0, 0, 0))
    draw_feet()
    pygame.display.flip()


while True:
    for line in dance * 2:
        if line.startswith('p'):
            draw(canvas)
            time.sleep(0.666)
        else:
            assert line[0] in ['l', 'r']
            parts = line.split()
            foot = {'l': left_foot, 'r': right_foot}[parts[0]]
            distance = {'up': (0, -1), 'left': (-1, 0), 'right': (1, 0), 'down': (0, 1)}[parts[1]]
            m = Settings.multiplier * float(parts[2])
            distance = (int(distance[0] * m), int(distance[1] * m))
            foot.move(*distance)

    random.shuffle(dance)

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#
#
#
#     #     elif event.type == MY_EVENT:
#     #         game_counter.increase()
#     #
#     #     elif event.type == pygame.MOUSEBUTTONDOWN:
#     #         event_log.add(f'Mouse button down')
#     #
#     #     elif event.type == pygame.MOUSEBUTTONUP:
#     #         event_log.add('Mouse button up')
#     #
#     #     elif event.type == pygame.KEYDOWN:
#     #         event_log.add('Key down')
#     #
#     #     elif event.type == pygame.KEYUP:
#     #         event_log.add('Key up')
#     #
#     #         if event.key == pygame.K_LEFT:
#     #             event_log.add('   Left arrow')
#     #         elif event.key == pygame.K_RIGHT:
#     #             event_log.add('   Right arrow')
#     #         else:
#     #             event_log.add(f'    {event.key}')
#     # canvas.fill((0, 0, 0))
#     # game_counter.draw()
#     # show_status(canvas)
#     # event_log.draw()
#     draw()
#     pygame.display.flip()
