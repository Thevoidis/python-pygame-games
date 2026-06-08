import pygame
import random

class Buff :
    def __init__(self,game,parent_scene) :
        self.game = game
        self.radius = 10
        self.hitbox =  pygame.Rect(0,0,
                        2*self.radius,
                        2*self.radius,
                        )
        self.parent_scene = parent_scene
        self.hitbox.center = (random.randint(0, self.game.screen_size[0]) , 0) 
        self.buff = random.choice(["Fireball","Extraball"])
        if self.buff == "Extraball" :
            self.color = (0,200,0)
        elif self.buff == "Fireball" :
            self.color = (200,0,0)




        self.delta_t = self.game.clock.tick(60) / 1000.0  # seconds


    def handle_keypress(self) :
        pass



    def update(self) :
        self.hitbox.y += 50

        

    
    def draw(self) :
        pygame.draw.circle(self.game.screen,
                           self.color,
                           self.hitbox.center,
                           self.radius)


