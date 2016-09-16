# coding=utf-8
import random
from Background import Background
from Bird import Bird
from Spike import Spike
from Variables import *
from Font import Create_Score


pygame.init()

class Main(object):
    def __init__(self):
        """Class Main"""
        """Basic atributes"""
        self.run = True
        self.clock = pygame.time.Clock()
        """Color and Background"""
        self.background = Background(background_game, [0, -20])
        self.fill_color = (100, 100, 100)
        self.color_margin = (238, 232, 170)
        """Types of Spikes"""
        self.spikeBOTTOM = pygame.image.load(spike)
        self.spikeTOP = pygame.transform.flip(self.spikeBOTTOM, True, True)
        """Object BIRD Instance"""
        self.character = Bird(WIDTH/2, HEIGHT/2, [2, 0])
        """Object SPIKES Instance"""
        self.Right_or_Left = True  #Saber si el Spike debe ir hacia la derecha o izquierda
        self.createSpikesBool = True
        self.hide = -60
        self.Spike_x = self.hide
        self.Spike_y = self.hide
        self.spikeMain = Spike(self.Spike_x, self.Spike_y, self.Right_or_Left)
        """Rect Sprite"""
        self.rectCharacter = self.character.get_rect()
        self.rectSpike = self.spikeMain.get_rect()
        """Limit of Bird"""
        self.rightlimit = False
        self.leftlimit = False
        self.bottomlimit = False
        self.toplimit = False
        self.createRightlimit = False
        self.createLeftlimit = False
        self.collitionActive = False
        self.turn_Active = True
        """Handling Font"""
        self.score = 0
        self.HandlingScore = Create_Score(self.score)

    def debug_true(self, x, y, z, w, zUp, wUp):
        print x, '\t', y, '\t', z, '\t', w, '\t', zUp, '\t', wUp

    def other_turn(self):
                if self.rectCharacter[0] == WIDTH/2 or (self.rectCharacter[0] >= (WIDTH/2) and self.rectCharacter[0] < (WIDTH/2)+20):
                    while self.turn_Active == True:
                        print 'Exito muchachos.'
                        self.turn_Active = False
                    self.collitionActive = False

    def collition(self):
            if self.rectCharacter[0] >=  self.Spike_x and self.rectCharacter[0] <= self.Spike_x + 60 and (self.rectCharacter[1] >= self.Spike_y and self.rectCharacter[1] <= self.Spike_y + 60): #Si estan a la misma altura, y toca el parajo la pared.
                    self.debug_true(self.rectCharacter[0], self.rectCharacter[1], self.Spike_x, self.Spike_y, self.Spike_x + 60, self.Spike_y+60)
                    while self.collitionActive == False:
                        self.score -= 10
                        self.collitionActive = True


    def rightlimitbool(self):
        self.turn_Active = True
        self.rightlimit = True

    def leftlimitbool(self):
        self.turn_Active = True
        self.leftlimit = True

    def bottomlimitbool(self):
        self.bottomlimit = True

    def toplimitbool(self):
        self.toplimit = True

    def Limit(self):
        """Este metodo implementara todas las condiciones y dinamicas para cada interaccion"""
        self.positionTuple = self.character.get_position()
        self.x, self.y = self.positionTuple

        if self.x in [269, 270, 271, 272, 273, 274, 275, 276]:
            while self.rightlimit == False:
                #print 'TEST RIGHT!!!'
                self.rightlimitbool()
                if self.collitionActive == False:
                    self.score += 10
                self.HandlingScore = Create_Score(self.score)
                self.leftlimit = False

        if self.x in [23, 24, 25, 26, 27, 28, 29]:
            while self.leftlimit == False:
                #print 'TEST LEFT!!!'
                self.leftlimitbool()
                if self.collitionActive == False:
                    self.score += 10
                self.HandlingScore = Create_Score(self.score)
                self.rightlimit = False

        if self.y < 26:
            while self.toplimit == False:
                #print 'TEST TOP!!!'
                self.toplimitbool()
                self.bottomlimit = False

        if self.y > 510:
            while self.bottomlimit == False:
                #print 'TEST BOTTOM!!!'
                self.bottomlimitbool()
                self.toplimit = False


    def createSpikes(self):
        """Function for creation of Sprites"""
        max = 450
        if self.rightlimit == True:
            while self.createRightlimit == False:
                self.Spike_x = 25
                self.Spike_y = random.randint(80, max)
                self.Right_or_Left = True
                self.createRightlimit = True
                self.spikeMain = Spike(self.Spike_x, self.Spike_y, self.Right_or_Left)
                self.createLeftlimit = False
                #print 'Righ limit>', '[', str(self.rightlimit), ' ', str(self.leftlimit), "]", '<Left limit'


        if self.leftlimit == True:
            while self.createLeftlimit == False:
                self.Spike_x = 270
                self.Spike_y = random.randint(80, max)
                self.Right_or_Left = False
                self.createLeftlimit = True
                self.createRightlimit = False
                self.spikeMain = Spike(self.Spike_x, self.Spike_y, self.Right_or_Left)
                #print 'Righ limit Create>', '[', str(self.createRightlimit), ' ', str(self.createLeftlimit), "]", '<Left limit Create'

    def world(self):
        if self.run:
            screen.blit(self.background.image, self.background.rect)
            pygame.draw.line(screen, self.color_margin,  ([side2 / 2, 0]), ([side2 / 2, HEIGHT]), side2)
            pygame.draw.line(screen, self.color_margin, [WIDTH - side2 / 2, 0], [WIDTH - side2 / 2, HEIGHT], side2)
            pygame.draw.line(screen, self.color_margin, [0, 0], [WIDTH, 0], side1 - 9)
            pygame.draw.line(screen, self.color_margin, [0, HEIGHT], [WIDTH, HEIGHT], side1 - 9)
            for i in range(0, 5):
                screen.blit(self.spikeBOTTOM, [22+i*62, HEIGHT-75])
                screen.blit(self.spikeTOP, [22+i*62, 22])
            """Handling Text"""
            self.HandlingScore.ScoreText.draw(screen)
            self.other_turn()
            self.collition()



    def update(self):
        self.world()
        self.Limit()
        self.createSpikes()


    def main(self):
        """"Grand Game"""
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            pygame.display.set_caption(caption)
            pygame.display.update()
            self.update()
            self.character.update(screen)
            self.spikeMain.update()

        pygame.quit()

if __name__ == "__main__":
    main = Main()
    main.main()
