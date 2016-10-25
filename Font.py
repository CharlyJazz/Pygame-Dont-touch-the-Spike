# coding=utf-8
import pygame

title1 = "Loco"
title2 = "Parajo"
title3 = "Mexicano"

x_title1 = 26+10
x_title2 = 32+35
x_title3 = 46+50

x_score = 220
x_life = 3
Tusj = "FFF_Tusj.ttf"
caveman = "CAVEMAN_.TTF"
towerruins = "towerruins.ttf"
copy = "Developed by Carlos Azuaje | 2016"
caption = 'Loco Parajo Mexicano'
try_again = ['Try Again ?', 'Press a Key for Play']


class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        self.font = pygame.font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)


class Create_life(Text):
    def __init__(self, life):
        self.LifeText = Text(Tusj, 20, "Life : {}".format(str(life)), (0, 0, 0), x_life, -2)


class Create_Score(Text):
    def __init__(self, score):
        self.ScoreText = Text(Tusj, 20, "Score : {}".format(str(score)), (0, 0, 0), x_score, -2)
        self.ScoreEnd = Text(towerruins, 20, "S c o r e  {}".format(str(score)), (0, 0, 0), x_title3-40, 450)


class Create_menu(Text):
    def __init__(self):
        self.title1 = Text(caveman, 30, "{}".format(title1), (100, 160, 221), x_title1, 80)
        self.title2 = Text(caveman, 30, "{}".format(title2), (150, 140, 200), x_title2, 110)
        self.title3 = Text(caveman, 30, "{}".format(title3), (200, 120, 180), x_title3, 140)
        self.copy_right = Text(towerruins, 25, "{}".format(copy), (119, 136, 153), -2, 570)


class Create_TryAgain(Text):
    def __init__(self):
        self.try_again = Text(towerruins, 30, "{}".format(try_again[0]), (153, 0, 0), x_title1+5, 350)
        self.press_key = Text(towerruins, 20, "{}".format(try_again[1]), (204, 0, 0), x_title2-60, 400)
