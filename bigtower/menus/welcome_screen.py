import arcade
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
