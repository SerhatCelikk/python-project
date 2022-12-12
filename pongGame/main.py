from game import Game
import pygame

class PongGame:
    def __init__(self, window, widht, height):
        self.game = Game(window, widht, height)
        self.ball = self.game.ball
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.top_paddle = self.game.top_paddle
        self.bottom_paddle = self.game.bottom_paddle
        
    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(60)
            self.game.draw() 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            keys = pygame.key.get_pressed()
            self.game.move_paddle(keys)
            self.game.ball.move()
            self.game.handle_collision()
        
        pygame.quit()
        

def main():
   widht, height = 900, 600
   win = pygame.display.set_mode((widht,height))# creates a window
   pygame.display.set_caption("PONG")
   pong = PongGame(win, widht, height) # creating a game
   pong.run() 

if __name__ == '__main__':
    main()