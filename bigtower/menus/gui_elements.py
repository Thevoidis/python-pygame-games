import arcade


class Button() :
    def __init__(self,
    coords,size,
    fgcolor=[(20,20,20),(150,150,150)],bgcolor=[(150,150,150),(20,20,20)],
    sel=False,
    font_name="Arial",
    font_size=20,
    texture=None, # Texture is a list of the form [ unsel_texture , sel_texture ]
    text=""
    ): #args to Button

        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.sel = sel
        self.font_name = font_name
        self.font_size = font_size
        self.coords = coords
        self.size = size
        self.text = text
        self.texture = texture
        self.text_obj = arcade.Text(
            text,
            coords[0],
            coords[1],
            (0, 0, 0),
            font_size=5,
            anchor_x="center",
            anchor_y="center",
        )
    
    def on_draw(self):

        if self.texture :
                arcade.draw_texture_rect(
                    self.texture[self.sel],
                    arcade.XYWH(
                        self.coords[0], self.coords[1],
                        self.size[0], self.size[1]
                        )
                    )
        else :
                arcade.draw_rect_filled(
                    arcade.XYWH(
                        self.coords[0], self.coords[1],
                        self.size[0], self.size[1]
                        ),
                    self.bgcolor[self.sel]
                        )
        if  self.text and self.font_name :
            self.text_obj.color = self.fgcolor[self.sel]
            self.text_obj.draw()

        elif (not self.font_name) :
            print("No fonts")



    def on_update(self):
        pass
