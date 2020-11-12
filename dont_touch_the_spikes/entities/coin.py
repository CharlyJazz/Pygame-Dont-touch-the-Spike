import pygame
import random
from dont_touch_the_spikes.settings.constants import *
from dont_touch_the_spikes.utils.aspect_scale import *

image_path = 'assets/images/coin/'
image_names = ['1', '2', '3', '4', "5", "6"]
size = 28
sprites = [
    aspect_scale(
        pygame.image.load("{}{}.png".format(image_path, i)), (size, size)
    ) for i in image_names
]

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = sprites
        self.image_index = 0
        self.image = self.sprites[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
        self.animation_countdown = 60
        self.last_animation = pygame.time.get_ticks()

    def update(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_animation >= self.animation_countdown:
            self.last_animation = pygame.time.get_ticks()
            self.image_index += 1 if self.image_index < 5 else -5
            self.image = self.sprites[self.image_index]
