import pygame


class Paddle:
    VEL = 4
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.WIDTH = width
        self.HEIGHT = height

    def draw(self, win):
        pygame.draw.rect(
            win, (255, 255, 255), (self.x, self.y, self.WIDTH, self.HEIGHT))
        

    def move(self, horizontal=True, up=None, right=None):
        if horizontal:# checks if we move horizontally
            if right:
                self.x += self.VEL
            else:
                self.x -= self.VEL
        else:
            if up:
                self.y -= self.VEL
            else:
                self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
