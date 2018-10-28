import pygame 
import random 
from bot import *

class visualizations:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.size = [800, 800]
        startVisualization()


    def startVisualization(self):
        pygame.init()

        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Defense Visualization")

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            
            screen.fill(self.WHITE)

        self.createEnemyTeam()

    def createTeam(self, teamNumber):
        bot_list = []
        hasBall = random.randint(0, 4)
        for i in range(5):
            if i == hasBall and teamNumber == 1:
                bot_list = bot_list + [bot(True, teamNumber)]
            else:
                bot_list = bot_list + [bot(False, teamNumber)]
        return bot_list
