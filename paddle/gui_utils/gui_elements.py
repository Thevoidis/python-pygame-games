import pygame

class Button :
    def __init__ (self, game, coords, size, text ,unselfgcolor=(0,0,0), unselbgcolor=(0,100,0) , selfgcolor=(0,0,0), selbgcolor=(0,200,0) , sel=False , font=False) :
        self.unselbgcolor = unselbgcolor
        self.selbgcolor = selbgcolor
        self.unselfgcolor = unselfgcolor
        self.selfgcolor = selfgcolor
        self.coords = coords
        self.size = size
        self.text = text
        self.game = game
        self.sel = sel
        if font :
            self.font = font
        else :
            self.font = self.game.default_font


    def draw(self) :
        if self.sel :
            self.bgcolor = self.selbgcolor
            self.fgcolor = self.selfgcolor
        else :
            self.bgcolor = self.unselbgcolor
            self.fgcolor = self.unselfgcolor

        pygame.draw.rect(self.game.screen,
                         self.bgcolor,
                         (self.coords[0],
                         self.coords[1],
                         self.size[0],
                         self.size[1] )
                         )

        self.rendered_text = self.font.render(
        self.text,
        True,
        self.fgcolor 
        )
        text_rect = self.rendered_text.get_rect(center=(
        self.coords[0] + self.size[0] // 2,
        self.coords[1] + self.size[1] // 2
    ))
        self.game.screen.blit(self.rendered_text,text_rect)


