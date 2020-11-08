import sys
import pygame

from dont_touch_the_spikes.surfaces.game import GameSurface
from dont_touch_the_spikes.settings.constants import *


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Don\'t Touch the Spikes')
    pygame.font.init()
    clock = pygame.time.Clock()
    game = GameSurface(screen)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    game.jump()
                if event.key == pygame.K_RETURN and game.player.dying:
                    game.reset()

        game.update()
        pygame.display.update()

if __name__ == "__main__":
    main()
