from random import randrange, choice
from gameObject import GameObject
from constants import *


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, "./images/strawberry.png")
        self.dx = 0
        self.dy = 0
        self.direction = 1
        self.reset()

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy

        if self.x > 500 or self.x < 0:
            self.reset()

    def reset(self):
        direction = (-1) ** randrange(2)

        self.x = 436 if direction < 0 else 64
        self.y = choice(lanes)
        self.dx = direction
