from random import randrange, choice
from gameObject import GameObject
from constants import *


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, "./images/apple.png")
        self.dx = 0
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy * self.speed

        if self.y > 500 or self.y < 0:
            self.reset()

    def reset(self):
        direction = (-1) ** randrange(2)

        self.x = choice(lanes)
        self.y = 436 if direction < 0 else 64
        self.dy = direction

    def set_pass(self):
        pass