from paddle import Paddle
from ball import Ball
import pygame
pygame.init()

class Game:
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    
    def __init__(self, win, win_widht, win_height):
        self.win = win
        self.win_widht = win_widht
        self.win_height = win_height
        
        self.left_paddle = Paddle(
            10, self.win_height // 2 - Paddle.HEIGHT // 2, 20, 100)
        self.right_paddle = Paddle(
            self.win_widht - 10 - Paddle.WIDHT, self.win_height // 2 - Paddle.HEIGHT // 2, 20, 100)
        self.top_paddle = Paddle(
            self.win_widht // 2 - Paddle.HEIGHT // 2, 10, 100, 20)
        self.bottom_paddle = Paddle(
            self.win_widht // 2 - Paddle.HEIGHT // 2, self.win_height - 10 - Paddle.WIDHT, 100, 20)
        self.ball = Ball(self.win_widht // 2, self.win_height // 2)
    
    def draw(self):
        self.win.fill(self.BLACK)
        
        for paddle in [self.left_paddle, self.right_paddle, self.top_paddle, self.bottom_paddle]:
            paddle.draw(self.win)
        
        self.ball.draw(self.win)
        pygame.display.update()
    
    def move_paddle(self,keys):
        if keys[pygame.K_w] and self.left_paddle.y - self.left_paddle.VEL >= 0:
            self.left_paddle.move_LR(up=True)
        if keys[pygame.K_s] and self.left_paddle.y + self.left_paddle.VEL + self.left_paddle.HEIGHT <= self.win_height:
            self.left_paddle.move_LR(up=False)
        
        if keys[pygame.K_UP] and self.right_paddle.y - self.right_paddle.VEL >= 0:
            self.right_paddle.move_LR(up=True)
        if keys[pygame.K_DOWN] and self.right_paddle.y + self.right_paddle.VEL + self.right_paddle.HEIGHT <= self.win_height:
            self.right_paddle.move_LR(up=False)
        
        if keys[pygame.K_d] and self.top_paddle.x + self.top_paddle.VEL + self.top_paddle.WIDHT <= self.win_widht:
            self.top_paddle.move_TB(right=True)
        if keys[pygame.K_a] and self.top_paddle.x - self.top_paddle.VEL >= 0:
            self.top_paddle.move_TB(right=False)
            
        if keys[pygame.K_RIGHT] and self.bottom_paddle.x + self.bottom_paddle.VEL + self.bottom_paddle.WIDHT <= self.win_widht:
            self.bottom_paddle.move_TB(right=True)
        if keys[pygame.K_LEFT] and self.bottom_paddle.x - self.bottom_paddle.VEL >= 0:
            self.bottom_paddle.move_TB(right=False)
         
    def handle_collision(self):
        # currently only works for right and left paddles
        # and may have bugs that need to be fixed
        if self.ball.y + self.ball.RADIUS >= self.win_height:
            self.ball.y_vel *= -1
        elif self.ball.y - self.ball.RADIUS <= 0:
            self.ball.y_vel *= -1

        if self.ball.x_vel < 0:
            if self.ball.y >= self.left_paddle.y and self.ball.y <= self.left_paddle.y + self.left_paddle.HEIGHT:
                if self.ball.x - self.ball.RADIUS <= self.left_paddle.x + self.left_paddle.WIDHT:
                    self.ball.x_vel *= -1

                    middle_y = self.left_paddle.y + self.left_paddle.HEIGHT / 2
                    difference_in_y = middle_y - self.ball.y
                    reduction_factor = (self.left_paddle.HEIGHT / 2) / self.ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    self.ball.y_vel = -1 * y_vel

        else:
            if self.ball.y >= self.right_paddle.y and self.ball.y <= self.right_paddle.y + self.right_paddle.HEIGHT:
                if self.ball.x + self.ball.RADIUS >= self.right_paddle.x:
                    self.ball.x_vel *= -1

                    middle_y = self.right_paddle.y + self.right_paddle.HEIGHT / 2
                    difference_in_y = middle_y - self.ball.y
                    reduction_factor = (self.right_paddle.HEIGHT / 2) / self.ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    self.ball.y_vel = -1 * y_vel
