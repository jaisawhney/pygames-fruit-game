from apple import Apple
from bomb import Bomb
from player import Player
from strawberry import Strawberry
from random import randint, uniform
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

    # Prevent collisions on start
    for entity in all_sprites:
        entity.render(screen)

    score = 0
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

        # If the player ate a fruit
        fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
        if fruit:
            score += 1
            pygame.mixer.music.load("./audio/fruit-eat.wav")
            pygame.mixer.music.play(1)
            fruit.reset()

            # Increase the speed of all non player sprites
            for entity in all_sprites:
                if not isinstance(entity, Player):
                    entity.set_speed(entity.speed + uniform(0.1, 0.2))

        # If the player hit a bomb
        if pygame.sprite.collide_rect(player, bomb):
            score = 0
            pygame.mixer.music.load("./audio/bomb-explode.wav")
            pygame.mixer.music.play(1)

            for entity in all_sprites:
                entity.set_speed((randint(0, 200) / 100) + 1)
                entity.reset()

        for entity in all_sprites:
            entity.move()
            entity.render(screen)

        # Render score
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"Score {score}", True, (0, 0, 0))
        center_text = text.get_rect(center=(screen_width / 2, 25))
        screen.blit(text, center_text)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
