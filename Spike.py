# coding=utf-8
from Variables import *
from Bird import Bird

import pygame


class Spike(object):
    def __init__(self, x, y, bool):
        self.position_x = x
        self.position_y = y
        self.bool = bool
        self.sprite_spike = pygame.image.load(spike)
        self.rect = self.sprite_spike.get_rect()
        self.angle_right = 270
        self.RIGHT = pygame.transform.rotate(self.sprite_spike, self.angle_right)
        self.LEFT = pygame.transform.flip(self.RIGHT, True, True)

    def get_rect(self):
        return self.rect

    def draw(self):
        if self.bool == True:
            screen.blit(self.RIGHT, [self.position_x, self.position_y])
        else:
            screen.blit(self.LEFT, [self.position_x, self.position_y])

    def update(self):
        self.draw()
        self.get_rect()
