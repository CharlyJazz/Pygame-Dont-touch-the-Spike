import pygame
import numpy as np
from dont_touch_the_spikes.settings.constants import *
from pygame.transform import flip


class Bird(pygame.sprite.Sprite):
    def __init__(self, callback_change_orientation):
        pygame.sprite.Sprite.__init__(self)
        self.images_flying = [
            pygame.transform.scale(pygame.image.load(
                "assets/images/bird/live_1.png").convert_alpha(), PLAYER_SIZE),
            pygame.transform.scale(pygame.image.load(
                "assets/images/bird/live_2.png").convert_alpha(), PLAYER_SIZE)
        ]
        self.images_dying = [
            pygame.transform.scale(pygame.image.load(
                "assets/images/bird/dead_1.png").convert_alpha(), PLAYER_SIZE),
            pygame.transform.scale(pygame.image.load(
                "assets/images/bird/dead_2.png").convert_alpha(), PLAYER_SIZE)
        ]
        self.image_index = 0
        self.image = flip(self.images_flying[self.image_index], True, False)
        self.rect = self.image.get_rect()
        self.rect.center = CENTER
        # Call this when the orientation change
        self.callback_change_orientation = callback_change_orientation
        self._orientation = -1

        # Jump logic
        self.jump_linspace = self.create_jump_linspace()
        self.jumping = False

        # Animation
        self.animation_cooldown = 250
        self.last_animation = pygame.time.get_ticks()
        self.dying = False

    def dead(self):
        # To change the animation quickly
        self.last_animation = 0
        self.dying = True

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        self._orientation = value
        self.callback_change_orientation(value)
        if value == -1:
            self.image = flip(
                self.images_flying[self.image_index], True, False)
        else:
            self.image = flip(
                self.images_flying[self.image_index], False, False)

    @staticmethod
    def create_jump_linspace():
        return np.linspace(0, 10, num=20)

    def update(self):
        if self.dying:
            self.try_animate_dying()
        else:
            self.horizontal_movement()
            self.listen_limits()
            self.listen_jump()
            self.try_animate()

    def try_animate_dying(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_animation >= self.animation_cooldown:
            self.last_animation = pygame.time.get_ticks()
            self.animate_dying()

    def animate_dying(self):
        if self.orientation == -1:
            self.image = flip(self.images_dying[self.image_index], True, False)
        else:
            self.image = flip(self.images_dying[self.image_index], False, False)

        if self.image_index == 1:
            self.image_index = 0
        else:
            self.image_index += 1

    def horizontal_movement(self):
        self.rect.x += 3 * self.orientation

    def listen_limits(self):
        if self.rect.x <= 0:
            self.orientation = 1
        elif self.rect.x + self.rect.w >= WIDTH:
            self.orientation = -1

    def listen_jump(self):
        if self.jumping:
            self.rect.y -= self.jump_linspace[0]
            self.jump_linspace = np.delete(self.jump_linspace, 0)

        if len(self.jump_linspace) == 0 and self.jumping:
            self.disable_jump()

        if not self.jumping:
            self.rect.y += 3

    def try_animate(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_animation >= self.animation_cooldown:
            self.last_animation = pygame.time.get_ticks()
            self.animate()

    def animate(self):
        if self.orientation == -1:
            self.image = flip(self.images_flying[self.image_index], True, False)
        else:
            self.image = flip(self.images_flying[self.image_index], False, False)

        if self.image_index == 1:
            self.image_index = 0
        else:
            self.image_index += 1

    def enable_jump(self):
        self.jumping = True

    def disable_jump(self):
        self.jumping = False
        self.jump_linspace = self.create_jump_linspace()
