from apple import Apple
from bomb import Bomb
from player import Player
from strawberry import Strawberry
from random import randint
from constants import *

import pygame


def main():
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.init()
    clock = pygame.time.Clock()

    # Sprites
    apple = Apple()
    strawberry = Strawberry()
    player = Player()
    bomb = Bomb()

    # Sprite groups
    all_sprites = pygame.sprite.Group()
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
            fruit.reset()
            for entity in all_sprites:
                if not isinstance(entity, Player):
                    entity.set_speed(entity.speed + 0.25)

        if pygame.sprite.collide_rect(player, bomb):
            for entity in all_sprites:
                entity.set_speed((randint(0, 200) / 100) + 1)
                entity.reset()

        for entity in all_sprites:
            entity.move()
            entity.render(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
