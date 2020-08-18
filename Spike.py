# coding=utf-8
from Variables import *
from Bird import Bird

import pygame


class Spike(object):
    def __init__(self, x, y, bool):
        self.bool = bool
        self.image = pygame.image.load(spike)
        self.rect = self.image.get_rect()
        self.angle_right = 270
        self.rect.x = x
        self.rect.y = y
        self.RIGHT = pygame.transform.rotate(self.image, self.angle_right)
        self.LEFT = pygame.transform.flip(self.RIGHT, True, True)
        self.mask = pygame.mask.from_surface(self.image)


    def get_rect(self):
        return self.rect

    def draw(self):
        if self.bool == True:
            self.mask = pygame.mask.from_surface(self.RIGHT)
            screen.blit(self.RIGHT, [self.rect.x, self.rect.y])
        else:
            self.mask = pygame.mask.from_surface(self.LEFT)
            screen.blit(self.LEFT, [self.rect.x, self.rect.y])

    def update(self):
        self.draw()
