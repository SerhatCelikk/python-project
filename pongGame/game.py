from paddle import Paddle
from ball import Ball
import pygame
pygame.init()

class Game:
    FONT = pygame.font.SysFont("comicsans", 32)
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
            self.win_widht - 300 - 10 - Paddle.WIDHT, self.win_height // 2 - Paddle.HEIGHT // 2, 20, 100)
        self.top_paddle = Paddle(
            (self.win_widht- 300) // 2 - Paddle.HEIGHT // 2, 10, 100, 20)
        self.bottom_paddle = Paddle(
            (self.win_widht - 300) // 2 - Paddle.HEIGHT // 2, self.win_height - 10 - Paddle.WIDHT, 100, 20)
        self.ball = Ball(self.win_widht // 2, self.win_height // 2)
    
    def font(self):
        score_title = self.FONT.render("Scorboard:", True, self.WHITE)
        self.win.blit(score_title,(750 - score_title.get_width() // 2, 20))
    
    def _draw_divider(self):
        for i in range (10, self.win_height, self.win_height//20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(
                self.win, self.WHITE, (self.win_widht - 300, i, 10, self.win_height//30))
    
    def draw(self):
        self.win.fill(self.BLACK)
        self._draw_divider()
        self.font()
        
        for paddle in [self.left_paddle, self.right_paddle, self.top_paddle, self.bottom_paddle]:
            paddle.draw(self.win)
        
        self.ball.draw(self.win)
        pygame.display.update()
    
    def move_paddle(self,keys):
        if keys[pygame.K_w] and self.left_paddle.y - self.left_paddle.VEL >= 0:
            self.left_paddle.move(horizontal=False, up=True)
        if keys[pygame.K_s] and self.left_paddle.y + self.left_paddle.VEL + self.left_paddle.HEIGHT <= self.win_height:
            self.left_paddle.move(horizontal=False, up=False)
        
        if keys[pygame.K_UP] and self.right_paddle.y - self.right_paddle.VEL >= 0:
            self.right_paddle.move(horizontal=False, up=True)
        if keys[pygame.K_DOWN] and self.right_paddle.y + self.right_paddle.VEL + self.right_paddle.HEIGHT <= self.win_height:
            self.right_paddle.move(horizontal=False, up=False)
        
        if keys[pygame.K_d] and self.top_paddle.x + self.top_paddle.VEL + self.top_paddle.WIDHT <= self.win_widht - 300:
            self.top_paddle.move(horizontal=True, right=True)
        if keys[pygame.K_a] and self.top_paddle.x - self.top_paddle.VEL >= 0:
            self.top_paddle.move(horizontal=True, right=False)
            
        if keys[pygame.K_RIGHT] and self.bottom_paddle.x + self.bottom_paddle.VEL + self.bottom_paddle.WIDHT <= self.win_widht - 300:
            self.bottom_paddle.move(horizontal=True, right=True)
        if keys[pygame.K_LEFT] and self.bottom_paddle.x - self.bottom_paddle.VEL >= 0:
            self.bottom_paddle.move(horizontal=True, right=False)
    
    def check_overrun(self):# checks for hits against the wall
        if self.ball.x + self.ball.RADIUS >= self.win_widht - 300:# if it hits right
            self.ball.x_vel *= -1
        elif self.ball.x - self.ball.RADIUS <= 0:# if hits left
            self.ball.x_vel *= -1
        elif self.ball.y + self.ball.RADIUS >= self.win_height:# if it hits bottom 
            self.ball.y_vel *= -1
        elif self.ball.y - self.ball.RADIUS <= 0:# if it hits top
            self.ball.y_vel *= -1
            
    def handle_collision(self):
        self.check_overrun()
        
        if self.ball.x_vel < 0:# left 
            if self.ball.y >= self.left_paddle.y and self.ball.y <= self.left_paddle.y + self.left_paddle.HEIGHT:
                if self.ball.x - self.ball.RADIUS <= self.left_paddle.x + self.left_paddle.WIDHT:
                    self.ball.x_vel *= -1

                    middle_y = self.left_paddle.y + self.left_paddle.HEIGHT / 2
                    difference_in_y = middle_y - self.ball.y
                    reduction_factor = (self.left_paddle.HEIGHT / 2) / self.ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    self.ball.y_vel = -1 * y_vel

        elif self.ball.x_vel > 0:# right
            if self.ball.y >= self.right_paddle.y and self.ball.y <= self.right_paddle.y + self.right_paddle.HEIGHT:
                if self.ball.x + self.ball.RADIUS >= self.right_paddle.x:
                    self.ball.x_vel *= -1

                    middle_y = self.right_paddle.y + self.right_paddle.HEIGHT / 2
                    difference_in_y = middle_y - self.ball.y
                    reduction_factor = (self.right_paddle.HEIGHT / 2) / self.ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    self.ball.y_vel = -1 * y_vel
        
        elif self.ball.y_vel < 0 :# top
            if self.ball.x >= self.top_paddle.x and self.ball.x <= self.top_paddle.x + self.top_paddle.WIDHT:
                if self.ball.y - self.ball.RADIUS <= self.top_paddle.y + self.top_paddle.HEIGHT:
                    self.ball.y_vel *= -1
                    
                    middle_x = self.top_paddle.x + self.top_paddle.WIDHT / 2
                    difference_in_x = middle_x - self.ball.x
                    reduction_factor = (self.top_paddle.WIDHT / 2) / self.ball.MAX_VEL
                    x_vel = difference_in_x / reduction_factor
                    self.ball.x_vel *= x_vel
        
        elif self.ball.y_vel > 0:# bottom 
            if self.ball.x >= self.bottom_paddle.x and self.ball.x <= self.bottom_paddle.x + self.bottom_paddle.WIDHT:
                if self.ball.y + self.ball.RADIUS >= self.bottom_paddle.y:
                    self.ball.x_vel *= -1
                    
                    middle_x = self.bottom_paddle.x + self.bottom_paddle.WIDHT / 2
                    difference_in_x = middle_x - self.ball.x
                    reduction_factor = (self.bottom_paddle.WIDHT / 2) / self.ball.MAX_VEL
                    x_vel = difference_in_x / reduction_factor
                    self.ball.x_vel *= x_vel
