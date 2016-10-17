# coding=utf-8
import sys
import random
from Background import Background
from Bird import Bird
from Spike import Spike
from Variables import *
from Font import Create_Score, Create_life, Create_menu


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
        self.Spike_List_x = []
        self.Spike_List_y = []
        self.spikeMain = Spike(self.Spike_x, self.Spike_y, self.Right_or_Left)
        self.spikeList = []
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
        self.life = 3
        self.HandlingLife = Create_life(self.life)
        """Menu"""
        self.HandlingMenu = Create_menu()
        self.ElementMenu = [self.HandlingMenu.title1, self.HandlingMenu.title2, self.HandlingMenu.title3,self.HandlingMenu.copy_right]
        self.mainScreen = True
        self.starGame = False

    def other_turn(self):
        """Esto maneja dos variables importantes, cuando llega a la mitad de
        la pantalla self.collitionActive y self.turn_Active se vuelven False para
        que cuando collisionemos con las paredes se puedan volver True."""
        if self.rectCharacter[0] == WIDTH/2 or (self.rectCharacter[0] >= (WIDTH/2) and self.rectCharacter[0] < (WIDTH/2)+20):
            while self.turn_Active == True:
                print 'Exito muchachos.'
                self.turn_Active = False
            self.collitionActive = False


    def collition(self):
            """"El la primera condicion if evalua la collicion del pajaro con las
            puas, las otras dos con las puas de los estremos inferior y superior"""
            for n in self.Spike_List_y:
                if self.rectCharacter[0] >=  self.Spike_x -10  and self.rectCharacter[0] <= self.Spike_x + 60 and (self.rectCharacter[1] >= n-40 and self.rectCharacter[1] <= n + 60):
                        while self.collitionActive == False:
                            self.score -= 10
                            self.life -= 1
                            self.HandlingLife = Create_life(self.life)
                            self.collitionActive = True

            if self.rectCharacter[1] < 80: #TOP
                while self.collitionActive == False:
                    self.score -= 10
                    self.life -= 1
                    self.exit_game()

            if self.rectCharacter[1] >= HEIGHT - 130 and self.rectCharacter[1] <= HEIGHT: #BOTTOM
                while self.collitionActive == False:
                    self.score -= 10
                    self.life -= 1
                    self.exit_game()

    def rightlimitbool(self):
        self.turn_Active = True
        self.rightlimit = True
        self.spikeList = []
        self.Spike_List_y = []


    def leftlimitbool(self):
        self.turn_Active = True
        self.leftlimit = True
        self.spikeList = []
        self.Spike_List_y = []


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
        """Function for creation of Sprites
           Problem: No se pintan las puas, encontrar el error"""
        max = 450
        print self.Spike_List_y

        spikes = self.level()
        if self.rightlimit == True:
            while self.createRightlimit == False:
                self.Spike_x = 25
                for spike in range(0, int(spikes)):
                    self.Spike_y = random.randint(80, max)
                    self.Right_or_Left = True
                    self.spikeMain = Spike(self.Spike_x, self.Spike_y, self.Right_or_Left)
                    self.spikeList.append(self.spikeMain)
                    self.Spike_List_y.append(self.Spike_y)
                self.createRightlimit = True
                self.createLeftlimit = False

        if self.leftlimit == True:
            while self.createLeftlimit == False:
                self.Spike_x = 270
                for spike in range(0, int(spikes)):
                    self.Spike_y = random.randint(80, max)
                    self.Right_or_Left = False
                    self.spikeMain = Spike(self.Spike_x, self.Spike_y, self.Right_or_Left)
                    self.spikeList.append(self.spikeMain)
                    self.Spike_List_y.append(self.Spike_y)
                self.createLeftlimit = True
                self.createRightlimit = False

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
            self.HandlingLife.LifeText.draw(screen)
            self.other_turn()
            self.collition()

    def draw_spike(self):
        """Problem draw spikes"""
        if not self.collitionActive:
            for spike in self.spikeList:
                spike.update()

    def update(self):
        self.world()
        self.Limit()
        self.createSpikes()
        self.draw_spike()

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def level(self):
        if self.score < 40:
            level = 1
            return level
        elif self.score >= 40 and self.score < 80:
            level = 2
            return level
        elif self.score >= 80 and self.score < 160:
            level = 3
            return level
        elif self.score >= 160:
            level = random.randint(1,4)
            return level


    def menu(self):
        """Menu Principal del Juego en Proceso"""
        if self.mainScreen:
            pygame.display.update()
            screen.blit(self.background.image, self.background.rect)


            for text in self.ElementMenu:
                text.draw(screen)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYUP:
                    self.startGame = True
                    self.mainScreen = False

    def main(self):
        """"Grand Game"""
        while self.run:
            if self.mainScreen:
                pygame.display.set_caption("Presiona una tecla!")
                self.menu()

            elif self.startGame:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        self.exit_game()
                pygame.display.set_caption(caption)
                pygame.display.update()
                self.update()
                self.character.update(screen)
                if self.score < 0 or self.life < 1:
                    self.exit_game()


        pygame.quit()

if __name__ == "__main__":
    main = Main()
    main.main()
