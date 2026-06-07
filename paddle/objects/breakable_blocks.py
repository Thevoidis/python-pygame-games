import pygame

class Block :
    def __init__(self , game , parent_scene ) :
        import random
        self.parent_scene = parent_scene
        self.game = game
        self.dimensions = [ random.randint(30, self.game.screen_size[0] // 10) , random.randint(30, self.game.screen_size[1] // 10) ]
        self.coords = [ random.randint(20, self.game.screen_size[0] - 20) , random.randint(10,self.game.screen_size[1] - 10*self.parent_scene.paddle.hitbox.height)  ]
        self.color = [ random.randint(0,100) for i in range(3) ]
        self.broken  = False
        self.hitbox =  pygame.Rect(
                self.coords[0], self.coords[1] , self.dimensions[0]  , self.dimensions[1]
                        )
    def update(self) :
        pass



    def draw(self) :
        pygame.draw.rect(self.game.screen,
                         self.color,
                         self.hitbox
                         )

