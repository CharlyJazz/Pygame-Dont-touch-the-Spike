# coding=utf-8
import pygame

""""General Variables"""

side1 = 50
side2 = 25
HEIGHT = 500+2*side1
WIDTH = 300+2*side2
caption = 'Loco Parajo Mexicano'
size = [WIDTH, HEIGHT]
files = ['b.png', 'd.png', 'o.png', 'p.png', 'jump.mp3', 'm.mp3']
background_game, spike, gameover, bird, jump, music = files
screen = pygame.display.set_mode(size)
game_on = False
game_over = False


#600H
#350W