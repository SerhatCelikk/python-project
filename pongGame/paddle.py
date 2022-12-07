import pygame

class Paddle:
    VEL = 4
    COLOR = (255, 255, 255)#white
    WIDHT = 20
    HEIGHT = 100
    
    def __init__(self, x, y, widht, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.WIDHT = widht
        self.HEIGHT = height
        
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.WIDHT, self.HEIGHT))
        
    
    def move_LR(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
    def move_TB(self, right=True):
        if right:
            self.x += self.VEL
        else:
            self.x -= self.VEL
