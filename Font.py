# coding=utf-8
from Variables import HEIGHT
import pygame

Tusj = "FFF_Tusj.ttf"


class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        self.font = pygame.font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

class Create_text(Text):
    def __init__(self):
        self.ScoreText = Text(Tusj, 20, "Score: ", (0, 0, 0), 250, 0)

class Create_Score(Text):
    def __init__(self, score):
        self.ScoreText = Text(Tusj, 20, "Score: " + str(score), (0, 0, 0), 220, -2)

