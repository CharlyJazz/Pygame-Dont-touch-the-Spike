# coding=utf-8


from Variables import *
import pygame



class Bird(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.radius = 25
        self.sprite = pygame.image.load(bird)
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (0, 54)
        self.gravity = 0.3
        self.game_status = game_on

    def get_rect(self):
        return self.rect

    def get_position(self):
        return (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.sprite, [self.x, self.y])

    def moving(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        self.vel[1] = 0.9*self.vel[1] + self.gravity*1.4

        if self.x + self.rect.center[1] > WIDTH:
            self.vel[0] *= -1

        if self.x - self.rect.center[0] < 0:
            self.vel[0] *= -1

        if self.rect.height - self.rect.center[0] > self.y:
            self.y += self.y/4
            self.vel[1] *= -1

        if self.y > HEIGHT - self.rect.center[0]*2.3:
            self.vel[1] *= -1


    def up(self):
        self.vel[1] -= 2

    def keydown(self):
        key = pygame.key.get_pressed()

        if not self.game_status  and key[pygame.K_SPACE]:
            self.game_status = True
            self.start()

        if self.game_status and key[pygame.K_SPACE]:
            self.up()


    def start(self):
        self.gravity = 0.3
        self.vel[0] = 3

    def update(self, screen):
        self.draw(screen)
        self.moving()
        self.keydown()
        self.get_rect()


