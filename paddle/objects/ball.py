import pygame
import random

class Ball :
    def __init__(self,game) :
        self.game = game
        self.radius = 10
        self.hitbox =  pygame.Rect(0,0,
                        2*self.radius,
                        2*self.radius,
                        )
        self.hitbox.center = (random.randint(0, self.game.screen_size[0]) , 0) 
        self.color = (200,0,0)
        self.vel = [random.randint(-20,20), random.randint(1,20)]

    def handle_keypress(self) :
        pass

    def update(self) :
        if (self.hitbox.x > 0) and self.hitbox.x < (self.game.screen_size[0] - self.hitbox.width)  :
            self.hitbox.x += self.vel[0]
        self.hitbox.y += self.vel[1]
        

    
    def draw(self) :
        pygame.draw.circle(self.game.screen,
                           self.color,
                           self.hitbox.center,
                           self.radius)


