import pygame
import random
from dont_touch_the_spikes.settings.constants import *
from dont_touch_the_spikes.utils.aspect_scale import *


class Spike(pygame.sprite.Sprite):
    def __init__(self, size, spike_number_type: int, orientation='LEFT', index=1):
        pygame.sprite.Sprite.__init__(self)

        self.size = size

        self.image = aspect_scale(
            pygame.image.load(
                "assets/images/wall_enemies/{}.png".format(spike_number_type)
            ), (size, size)
        )

        self.rect = self.image.get_rect()

        if orientation == 'LEFT' or orientation == 'RIGHT':
            self.rect.y = random.randint(0, HEIGHT - self.size)

        if orientation == 'LEFT':
            self.image = pygame.transform.rotate(self.image, 270)
            self.rect.x = self.image.get_width() * -1
        elif orientation == 'RIGHT':
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect.x = WIDTH + self.rect.w
        elif orientation == 'TOP':
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect.x = self.rect.w * index
        elif orientation == 'BOTTOM':
            self.rect.x = self.rect.w * index
            self.rect.y = HEIGHT - self.rect.height

        self.orientation = orientation

    def update(self):
        if self.orientation == 'RIGHT' and self.rect.x > WIDTH - self.size:
            self.rect.x -= 1
        elif self.orientation == 'LEFT' and self.rect.x < 0:
            self.rect.x += 1
