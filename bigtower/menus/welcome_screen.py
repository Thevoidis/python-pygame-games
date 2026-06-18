import arcade

from menus.gui_elements import Button

class Scene() :
    def __init__(self,game) :
        self.game = game
        self.mainbox_width = self.game.screen_size[0] // 3
        self.mainbox_height = self.game.screen_size[1] // 2
        self.background = arcade.load_texture("assets/menus/welcom_screen_background.jpg")
        self.mainbox_color = (10,10,10)
        self.mainbox =  arcade.XYWH(
                5*(self.game.screen_size[0] // 6),
                3*(self.game.screen_size[1] // 4),
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
                item["item"] = Button([self.mainbox.x,self.mainbox.y + (self.mainbox_height // 2) - 30 - top_pad],
                                      [self.mainbox_width - 10 , button_height],
                                      fgcolor=[(0,0,0),(0,0,0)],
                                      bgcolor=[(100,100,0),(200,200,0)],
                                      text=item["text"]
                                      )

            top_pad += item["item"].size[1] + 10
    def on_draw(self) :
        arcade.draw_texture_rect(
                self.background,
                arcade.LBWH(
                    0,
                    0,
                    self.game.screen_size[0],
                    self.game.screen_size[1]
                    )
                )

        arcade.draw_rect_outline(
            self.mainbox,
            self.mainbox_color,
            border_width=5,
            tilt_angle=0)
        
        for item in self.mainboxitems :
            item["item"].on_draw()


    def on_resize(self) :
        self.mainbox_width = 100
        self.mainbox_height = 100
        self.mainbox =  arcade.XYWH(
                self.game.screen_size[0] // 2,
                self.game.screen_size[1] // 2,
                self.mainbox_width,
                self.mainbox_height
                )

        

    def on_key_press(self, key, modifiers):
        pass
    
    def on_key_release(self, key, modifiers):
        pass

    def on_update(self, delta_time):
        pass
