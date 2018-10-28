import random

class bot:
    def __init__(self, hasBall, team):
        self.hasBall = hasBall
        self.team = team
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)
        self.angle = random.randint(0, 360)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_angle(self, angle):
        self.angle = angle

    def set_team(self, team):
        self.team = team

    def set_hasBall(self, hasBall):
        self.hasBall = hasBall

    def get_pos(self):
        return (self.x, self.y, self.angle)

    def get_team(self):
        if team == 0:
            return "Ally"
        return "Enemy"

    def get_hasBall(self):
        return self.hasBall