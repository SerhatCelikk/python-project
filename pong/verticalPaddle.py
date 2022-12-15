import pygame

#4 player paddle class


class VerticalPaddle:
    VEL = 4
    WIDTH = 100
    HEIGHT = 20

    def __init__(self, x, y):
        self.x = self.original_x = x
        self.y = self.original_y = y
        

    def draw(self, win):
        pygame.draw.rect(
            win, (255, 255, 255), (self.x, self.y, self.WIDTH, self.HEIGHT))
            

    def move(self, forward=True):
        if forward:
            self.x -= self.VEL
        else:
            self.x += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y