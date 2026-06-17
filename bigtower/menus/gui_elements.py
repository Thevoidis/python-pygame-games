import arcade


class Button() :
    def __init__(self,
    coords,size,
    selfgcolor=[(20,20,20),(150,150,150)],selbgcolor=[(150,150,150),(20,20,20)],
    sel=False,
    font_name=None,
    font_size=20,
    texture=None, # Texture is a list of the form [ unsel_texture , sel_texture ]
    text=""
    ): #args to Button

        self.bgcolor = selbgcolor
        self.fgcolor = selfgcolor
        self.sel = sel
        self.font_name = font_name
        self.font_size = font_size
        self.coords = coords
        self.size = size
        self.text = text
        self.texture = texture

    
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
        if  self.text :
            if self.font_name :
                arcade.draw_text(
                    self.text,
                    self.coords[0], self.coords[1],
                    self.fgcolor[self.sel],
                    font_size=self.font_size,
                    font_name=self.font_name,
                    anchor_x="center",
                    anchor_y="center"
                    )
            else :
                arcade.draw_text(
                    self.text,
                    self.coords[0], self.coords[1],
                    self.fgcolor[self.sel],
                    anchor_x="center",
                    anchor_y="center"
                    )




    def on_update(self):
        pass
