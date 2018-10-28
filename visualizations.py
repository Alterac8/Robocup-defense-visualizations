import pygame 
import random 
from bot import *
from predictions import *

class visualizations:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.RED_HAS_BALL = (102, 0, 0)
        self.GRASS_GREEN = (70, 127, 26)
        self.size = [800, 800]
        self.enemy_team = []
        self.ally_team = []
        self.startVisualization()
        self.points = []
        self.rad = {0: (3 * math.pi) / 2, 1: math.pi / 2, 2: math.pi, 3: 2 * math.pi}

    def startVisualization(self):
        pygame.init()

        screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption("Defense Visualization")

        done = False
        debug_print_once = True

        self.ally_team = self.createTeam(0)
        self.enemy_team = self.createTeam(1)
        clock = pygame.time.Clock()
        chance_of_goal = random.randint(0, 100)
        location_of_goal = random.randint(0, 3)
        random_x = random.randint(0, self.size[0] - 200)
        random_y = random.randint(0, self.size[0] - 200)
        point_to_go_chance = random.randint(0, 100)
        has_goal = False

        while not done:
            clock.tick(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.enemy_team = self.createTeam(1)
                        self.ally_team = self.createTeam(0)

                        chance_of_goal = random.randint(0, 100)
                        location_of_goal = random.randint(0, 3)
                        random_x = random.randint(0, self.size[0] - 200)
                        random_y = random.randint(0, self.size[0] - 200)
                        point_to_go_chance = random.randint(0, 100)
                        has_goal = False
                        if not debug_print_once:
                            debug_print_once = True
                            print("\n")
            
            screen.fill(self.GRASS_GREEN)

            if chance_of_goal > 0:
                has_goal = True
                self.addGoal(screen, location_of_goal, random_x, random_y)

            if point_to_go_chance > 0 and has_goal:
                new_angle = math.degrees(math.atan((random_y - self.enemy_team[0].get_y())/(random_x - self.enemy_team[0].get_x())) + self.rad.get(location_of_goal))
                self.enemy_team[0].set_angle(int(new_angle))

            for bot in self.enemy_team:
                if debug_print_once:
                    print(bot)
                    
                if bot.get_hasBall():
                    pygame.draw.circle(screen, self.RED_HAS_BALL, bot.get_coor(), 10)
                else:
                    pygame.draw.circle(screen, self.RED, bot.get_coor(), 10)

            if has_goal and debug_print_once:
                print("Goal pos at ({}, {})".format(random_x, random_y))
            debug_print_once = False
            for bot in self.ally_team:
                pygame.draw.circle(screen, self.BLUE, bot.get_coor(), 10)
            
            self.drawPrediction(screen, self.enemy_team[0])

            pygame.display.flip()

    def createTeam(self, team_number):
        bot_list = []
        for i in range(5):
            if i == 0 and team_number == 1:
                bot_list += [bot(True, team_number)]
            else:
                bot_list += [bot(False, team_number)]
        return bot_list

    def addGoal(self, screen, location, x, y):
        if location == 0:
            pygame.draw.rect(screen, self.WHITE, [x, 0, 200, 80])
        elif location == 1:
            pygame.draw.rect(screen, self.WHITE, [x, self.size[1] - 80, 200, 80])
        elif location == 2:
            pygame.draw.rect(screen, self.WHITE, [0, y, 80, 200])
        elif location == 3:
            pygame.draw.rect(screen, self.WHITE, [self.size[0] - 80, y, 80, 200])

    def drawPrediction(self, screen, bot):
        mk_pred = predictions(bot)
        self.points, outerLeft, outerRight = mk_pred.makePredictions(15)
        pygame.draw.lines(screen, self.BLACK, True, mk_pred.shootingLine(), 2)
        pygame.draw.lines(screen, self.BLACK, True, [bot.get_coor(), outerLeft], 2)
        pygame.draw.lines(screen, self.BLACK, True, [bot.get_coor(), outerRight], 2)

v = visualizations()