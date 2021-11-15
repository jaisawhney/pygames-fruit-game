from random import randrange, choice
from gameObject import GameObject
from constants import *


class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, "./images/bomb.png")
        self.dx = 0
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        if self.x > 500 or self.x < 0 or self.y > 500 or self.y < 0:
            self.reset()

    def reset(self):
        direction = randrange(4)
        self.dx = 0
        self.dy = 0

        # Up
        if direction == 0:
            self.x = choice(lanes)
            self.y = 436
            self.dy = -1
        # Down
        elif direction == 1:
            self.x = choice(lanes)
            self.y = 64
            self.dy = 1
        # Left
        elif direction == 2:
            self.x = 436
            self.y = choice(lanes)
            self.dx = -1
        # Right
        elif direction == 3:
            self.x = 64
            self.y = choice(lanes)
            self.dx = 1
