import pygame
from random import randint, choice, randrange

pygame.init()
screen = pygame.display.set_mode([500, 500])

lanes = [93, 218, 343]

global_speed = (randint(0, 200) / 100) + 1


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, "./images/apple.png")
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y > 500 or self.y < 0:
            self.reset()

    def reset(self):
        direction = (-1) ** randrange(2)

        self.x = choice(lanes)
        self.y = 436 if direction < 0 else 64
        self.dy = global_speed * direction


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, "./images/strawberry.png")
        self.dx = 0
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x > 500 or self.x < 0:
            self.reset()

    def reset(self):
        direction = (-1) ** randrange(2)

        self.x = 436 if direction < 0 else 64
        self.y = choice(lanes)
        self.dx = global_speed * direction


class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, "./images/bomb.png")
        self.dx = 0
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy

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
            self.dy = global_speed * -1
        # Down
        elif direction == 1:
            self.x = choice(lanes)
            self.y = 64
            self.dy = global_speed
        # Left
        elif direction == 2:
            self.x = 436
            self.y = choice(lanes)
            self.dx = global_speed * -1
        # Right
        elif direction == 3:
            self.x = 64
            self.y = choice(lanes)
            self.dx = global_speed


class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(93, 93, "./images/player.png")
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


all_sprites = pygame.sprite.Group()

apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()

clock = pygame.time.Clock()

all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        global_speed += 0.1
        fruit.reset()

    if pygame.sprite.collide_rect(player, bomb):
        for entity in all_sprites:
            entity.reset()

    for entity in all_sprites:
        entity.move()
        entity.render(screen)
    pygame.display.flip()
    clock.tick(60)

if __name__ == "__main__":
    pass