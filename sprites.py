import pygame
from random import randint, randrange, choice
from constants import *


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.speed = (randint(0, 200) / 100) + 1

        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))

    def set_speed(self, speed):
        self.speed = speed

    def set_image(self, image):
        self.surf = pygame.image.load(image)


class AnimatedGameObject(GameObject):
    def __init__(self, x, y, images):
        super(AnimatedGameObject, self).__init__(x, y, images[0])
        self.images = images
        self.frame_count = 0
        self.current_image_index = 0

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        self.frame_count += 1

        # New image every 6 frames
        if self.frame_count >= 6:
            self.frame_count = 0

            self.current_image_index += 1
            if len(self.images) <= self.current_image_index:
                self.current_image_index = 0

            # Update image
            self.surf = pygame.image.load(self.images[self.current_image_index])
        screen.blit(self.surf, (self.x, self.y))


class Player(AnimatedGameObject):
    def __init__(self):
        images = ["./images/player/pink-1.gif", "./images/player/pink-2.gif",
                  "./images/player/pink-3.gif", "./images/player/pink-4.gif",
                  "./images/player/pink-5.gif", "./images/player/pink-6.gif",
                  "./images/player/pink-7.gif", "./images/player/pink-8.gif",
                  "./images/player/pink-9.gif", "./images/player/pink-10.gif",
                  "./images/player/pink-11.gif"]

        super(Player, self).__init__(93, 93, images)
        self.dx = 93
        self.dy = 93
        self.pos_x = 1
        self.pos_y = 1
        self.reset()

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]


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

        self.x = 436 if direction < 0 else 0
        self.y = choice(lanes)
        self.dx = direction


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
        self.y = 436 if direction < 0 else 0
        self.dy = direction


class Asteroid(GameObject):
    def __init__(self):
        super(Asteroid, self).__init__(0, 0, "./images/asteroid.png")
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
            self.y = 0
            self.dy = 1
        # Left
        elif direction == 2:
            self.x = 436
            self.y = choice(lanes)
            self.dx = -1
        # Right
        elif direction == 3:
            self.x = 0
            self.y = choice(lanes)
            self.dx = 1
