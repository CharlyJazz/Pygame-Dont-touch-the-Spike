# coding=utf-8


from Variables import *
import pygame



class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, vel):
        self.vel = vel
        self.radius = 25
        self.sprite = pygame.image.load(bird)
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity = 0.3
        self.game_status = game_on
        self.jump_sound = pygame.mixer.Sound('jump.wav')

    def get_rect(self):
        return self.rect

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def draw(self, screen):
        screen.blit(self.sprite, [self.rect.x, self.rect.y])

    def moving(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
        self.vel[1] = 0.9*self.vel[1] + self.gravity*1.4

        if self.rect.x > WIDTH-self.rect[3]: #RIGHT COLLITION
            self.vel[0] *= -1

        if self.rect.x < 0:                  #LEFT COLLITION
            self.vel[0] *= -1

        if self.rect.y > HEIGHT-self.rect[3]:#BOTTOM COLLITION
            self.vel[1] *= -1

        if self.rect.y < 0:                  #TOP COLLITION
            self.rect.y += 3
            self.vel[1] *= -1

    def up(self):
        self.vel[1] -= 2
        self.jump_sound.play()

    def keydown(self):
        key = pygame.key.get_pressed()

        if not self.game_status and key[pygame.K_SPACE]:
            self.game_status = True
            self.start()

        if self.game_status and key[pygame.K_SPACE]:
            self.up()


    def start(self):
        self.gravity = 0.3
        self.vel[0] = 3

    def update(self, screen):
        self.jump_sound.set_volume(0.1)
        self.draw(screen)
        self.moving()
        self.keydown()
        self.get_rect()
