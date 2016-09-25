# coding=utf-8
import pygame

title1 = "Loco"
title2 = "Parajo"
title3 = "Mexicano"

x_title1 = 26
x_title2 = 32
x_title3 = 46

x_score = 220
x_life = 20
Tusj = "FFF_Tusj.ttf"
caveman = "CAVEMAN_.TTF"
towerruins = "towerruins.ttf"
copy = "Developed by Carlos Azuaje | 2016"
caption = 'Loco Parajo Mexicano'


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

class Create_menu(Text):
    def __init__(self, ):
        self.title1 = Text(caveman, 20, "{}".format(title1), (100, 160, 221), x_title1, 20)
        self.title2 = Text(caveman, 20, "{}".format(title2), (150, 140, 200), x_title2, 40)
        self.title3 = Text(caveman, 20, "{}".format(title3), (200, 120, 180), x_title3, 60)
        self.intruction = Text(Tusj, 35, "{}".format("Press a key . . ."), (0, 0, 0), 60, 240)
        self.copy_right = Text(towerruins, 25, "{}".format(copy), (119, 136, 153), -2, 570)

