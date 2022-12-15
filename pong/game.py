from .paddle import Paddle
from .verticalPaddle import VerticalPaddle
from .ball import Ball
import pygame
import random
pygame.init()

#4 player game class


class GameInformation:
    def __init__(self, left_hits, right_hits, left_score, right_score, top_hits, bottom_hits, top_score, bottom_score):
        self.left_hits = left_hits
        self.right_hits = right_hits
        self.top_hits = top_hits
        self.bottom_hits = bottom_hits
        self.left_score = left_score
        self.right_score = right_score
        self.top_score = top_score
        self.bottom_score = bottom_score



class Game:
    """
    To use this class simply initialize and instance and call the .loop() method
    inside of a pygame event loop (i.e while loop). Inside of your event loop
    you can call the .draw() and .move_paddle() methods according to your use case.
    Use the information returned from .loop() to determine when to end the game by calling
    .reset().
    """
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.left_paddle = Paddle(
            10, self.window_height // 2 - Paddle.HEIGHT // 2)
        self.right_paddle = Paddle(
            self.window_width - 10 - Paddle.WIDTH, self.window_height // 2 - Paddle.HEIGHT//2)
        self.top_paddle = VerticalPaddle(
            self.window_width // 2 - VerticalPaddle.HEIGHT // 2, 10)
        self.bottom_paddle = VerticalPaddle(
            self.window_width // 2 - VerticalPaddle.HEIGHT // 2, self.window_height - 10 - VerticalPaddle.WIDTH)
        self.ball = Ball(self.window_width // 2, self.window_height // 2)
        

        self.left_score = 0
        self.right_score = 0
        self.top_score = 0
        self.bottom_score = 0
        self.left_hits = 0
        self.right_hits = 0
        self.top_hits = 0
        self.bottom_hits = 0
        self.window = window

    def _draw_score(self):
        left_score_text = self.SCORE_FONT.render(
            f"{self.left_score}", 1, self.WHITE)
        right_score_text = self.SCORE_FONT.render(
            f"{self.right_score}", 1, self.WHITE)
        top_score_text = self.SCORE_FONT.render(
            f"{self.top_score}", 1, self.WHITE)
        bottom_score_text = self.SCORE_FONT.render(
            f"{self.bottom_score}", 1, self.WHITE)
        self.window.blit(left_score_text, (self.window_width //
                                           4 - left_score_text.get_width()//2, 20))
        self.window.blit(right_score_text, (self.window_width * (3/4) -
                                            right_score_text.get_width()//2, 20))
        self.window.blit(top_score_text, (self.window_width //
                                            2 - top_score_text.get_width()//2, 20))
        self.window.blit(bottom_score_text, (self.window_width //
                                            2 - bottom_score_text.get_width()//2, self.window_height - 20))

    def _draw_hits(self):
        hits_text = self.SCORE_FONT.render(
            f"{self.left_hits + self.right_hits}", 1, self.RED)
        self.window.blit(hits_text, (self.window_width //
                                     2 - hits_text.get_width()//2, 10))
        

    def _draw_divider(self):
        for i in range(10, self.window_height, self.window_height//20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(
                self.window, self.WHITE, (self.window_width//2 - 5, i, 10, self.window_height//20))
        for i in range(10, self.window_width, self.window_width//20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(
                self.window, self.WHITE, (i, self.window_height//2 - 5, self.window_width//20, 10))

    def _handle_collision(self):
        ball = self.ball
        left_paddle = self.left_paddle
        right_paddle = self.right_paddle
        top_paddle = self.top_paddle
        bottom_paddle = self.bottom_paddle

        if ball.y + ball.RADIUS >= self.window_height:
            ball.y_vel *= -1
        elif ball.y - ball.RADIUS <= 0:
            ball.y_vel *= -1

        if ball.x_vel < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + Paddle.HEIGHT:
                if ball.x - ball.RADIUS <= left_paddle.x + Paddle.WIDTH:
                    ball.x_vel *= -1

                    middle_y = left_paddle.y + Paddle.HEIGHT / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (Paddle.HEIGHT / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel
                    self.left_hits += 1
            if ball.y >= top_paddle.y and ball.y <= top_paddle.y + VerticalPaddle.HEIGHT:
                if ball.x - ball.RADIUS <= top_paddle.x + VerticalPaddle.WIDTH:
                    ball.x_vel *= -1

                    middle_y = top_paddle.y + VerticalPaddle.HEIGHT / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (VerticalPaddle.HEIGHT / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel
                    self.left_hits += 1

        else:
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + Paddle.HEIGHT:
                if ball.x + ball.RADIUS >= right_paddle.x:
                    ball.x_vel *= -1

                    middle_y = right_paddle.y + Paddle.HEIGHT / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (Paddle.HEIGHT / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel
                    self.right_hits += 1
            if ball.y >= bottom_paddle.y and ball.y <= bottom_paddle.y + VerticalPaddle.HEIGHT:
                if ball.x + ball.RADIUS >= bottom_paddle.x:
                    ball.x_vel *= -1

                    middle_y = bottom_paddle.y + VerticalPaddle.HEIGHT / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (VerticalPaddle.HEIGHT / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel
                    self.right_hits += 1

    def draw(self, draw_score=True, draw_hits=False):
        self.window.fill(self.BLACK)

        self._draw_divider()

        if draw_score:
            self._draw_score()

        if draw_hits:
            self._draw_hits()

        for paddle in [self.left_paddle, self.right_paddle]:
            paddle.draw(self.window)
        for paddle in [self.top_paddle, self.bottom_paddle]:
            paddle.draw(self.window)

        self.ball.draw(self.window)

    def move_paddle(self, left=True, up=True):
        """
        Move the left or right paddle.

        :returns: boolean indicating if paddle movement is valid. 
                  Movement is invalid if it causes paddle to go 
                  off the screen
        """
        if left:
            if up and self.left_paddle.y - Paddle.VEL < 0:
                return False
            if not up and self.left_paddle.y + Paddle.HEIGHT > self.window_height:
                return False
            self.left_paddle.move(up)
            
        else:
            if up and self.right_paddle.y - Paddle.VEL < 0:
                return False
            if not up and self.right_paddle.y + Paddle.HEIGHT > self.window_height:
                return False
            self.right_paddle.move(up)
        if up:
            if up and self.top_paddle.y - VerticalPaddle.VEL < 0:
                return False
            if not up and self.top_paddle.y + VerticalPaddle.HEIGHT > self.window_height:
                return False
            self.top_paddle.move(up)
        else:
            if up and self.bottom_paddle.y - VerticalPaddle.VEL < 0:
                return False
            if not up and self.bottom_paddle.y + VerticalPaddle.HEIGHT > self.window_height:
                return False
            self.bottom_paddle.move(up)

        return True

    def loop(self):
        """
        Executes a single game loop.

        :returns: GameInformation instance stating score 
                  and hits of each paddle.
        """
        self.ball.move()
        self._handle_collision()

        if self.ball.x < 0:
            self.ball.reset()
            self.right_score += 1
        elif self.ball.x > self.window_width:
            self.ball.reset()
            self.left_score += 1
        if self.ball.y < 0:
            self.ball.reset()
            self.bottom_score += 1
        elif self.ball.y > self.window_height:
            self.ball.reset()
            self.top_score += 1

        game_info = GameInformation(
            self.left_hits, self.right_hits, self.left_score, self.right_score, self.top_hits, self.bottom_hits, self.top_score, self.bottom_score)

        return game_info

    def reset(self):
        """Resets the entire game."""
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0
        self.top_score = 0
        self.bottom_score = 0
        self.left_hits = 0
        self.right_hits = 0
        self.top_hits = 0
        self.bottom_hits = 0
