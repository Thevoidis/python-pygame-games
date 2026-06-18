import pygame

from menus.gui_elements import Button

class Scene() :
    def __init__(self,game) :
        self.game = game
        self.background = pygame.image.load("assets/menus/welcom_screen_background.jpg")
        self.on_resize()
        self.mainbox_color = (10,10,10)
        self.mainbox =  pygame.Rect(
                2*(self.game.screen_size[0] // 3),
                0,
                self.mainbox_width,
                self.mainbox_height
                )
        
        self.mainboxitems = [
                {   
                 "name" : "Start Button",
                 "type" : "Button",
                 "text" : "Start New Game"
                 },

                {   
                 "name" : "Load Button",
                 "type" : "Button",
                 "text" : "Load Game"
                 },
            
                {   
                 "name" : "Quit Button",
                 "type" : "Button",
                 "text" : "Quit Game"
                 },
                ]
        self.init_buttons()

    
    def init_buttons(self) :
        top_pad = 0
        button_height = 50
        for item in self.mainboxitems :
            if item["type"] == "Button" :
                item["item"] = Button(self.game,
                                    [self.mainbox.x + 10, self.mainbox.y + 10 + top_pad],
                                    [self.mainbox_width - 20 , button_height],
                                    fgcolor=[(0,0,0),(0,0,0)],
                                    bgcolor=[(100,100,0),(200,200,0)],
                                    text=item["text"]
                                      )

            top_pad += item["item"].size[1] + 10
        self.mainbox.height = top_pad + 10
    def on_draw(self) :
        self.game.screen.blit(
                self.background,
                (0,0)
                )

        pygame.draw.rect(
                self.game.screen,
            self.mainbox_color,
            self.mainbox,
            )
        
        for item in self.mainboxitems :
            item["item"].on_draw()


    def on_resize(self) :
        self.background = pygame.transform.scale(self.background,(self.game.screen_size[0], self.game.screen_size[1]))
        self.mainbox_width = self.game.screen_size[0] // 3
        self.mainbox_height = self.game.screen_size[1] // 2
        self.mainbox =  pygame.Rect(
                5*(self.game.screen_size[0] // 6),
                (self.game.screen_size[1] // 4),
                self.mainbox_width,
                self.mainbox_height
                )

        
    def handle_event(self,event) :
        pass

    def handle_keypress(self) :
        pass

    def on_update(self, delta_time):
        pass
