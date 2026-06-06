import pygame
from gui_utils.gui_elements import Button

class Scene :
    def __init__(self,parent_scene) :
        self.parent_scene = parent_scene
        self.mainrect = pygame.Rect(0,0,
                        self.parent_scene.game.screen_size[0] // 2,
                        self.parent_scene.game.screen_size[1] // 2
                                    )
        self.mainrect.center = (self.parent_scene.game.screen_size[0] // 2,
                        self.parent_scene.game.screen_size[1] // 2)
        self.enabled  = False

        self.diff_text = self.parent_scene.game.title_font.render(
                "Choose Difficulty :",
                True,
                self.parent_scene.game.sel_color
                )
        # Buttons

        self.indian_mode_button = Button(self.parent_scene.game,
                            (self.mainrect.x + 10, self.mainrect.y + 10),
                            (self.mainrect.width - 20, 100),"Indian",font=self.parent_scene.game.title_font)

        self.asian_mode_button = Button(self.parent_scene.game,
                            (self.mainrect.x + 10, self.mainrect.y + 115),
                            (self.mainrect.width - 20, 100),"Asian",font=self.parent_scene.game.title_font)

        self.hard_mode_button = Button(self.parent_scene.game,
                            (self.mainrect.x + 10, self.mainrect.y + 220),
                            (self.mainrect.width - 20, 100),"Hard",font=self.parent_scene.game.title_font)

        self.normal_mode_button = Button(self.parent_scene.game,
                            (self.mainrect.x + 10, self.mainrect.y + 325),
                            (self.mainrect.width - 20, 100),"Normal",sel=True,font=self.parent_scene.game.title_font)

        self.easy_mode_button = Button(self.parent_scene.game,
                            (self.mainrect.x + 10, self.mainrect.y + 430),
                            (self.mainrect.width - 20, 100),"Easy",font=self.parent_scene.game.title_font)

        self.difficulty_mode_buttons = [
                self.indian_mode_button,
                self.asian_mode_button,
                self.hard_mode_button,
                self.normal_mode_button,
                self.easy_mode_button
                ]

    def update(self) :
        pass

    def handle_event(self,event):
        if event.type == pygame.KEYDOWN :
            if (event.key == pygame.K_ESCAPE) and (self.parent_scene.difficulty_chooser.enabled) :
                self.parent_scene.difficulty_chooser.enabled = False
                self.parent_scene.scene_paused = False

            if event.key == pygame.K_RETURN :
                for i in range(len(self.difficulty_mode_buttons)) :
                    if (self.difficulty_mode_buttons[i].sel == True) :
                        self.parent_scene.game.difficulty_level = self.difficulty_mode_buttons[i].text or None
                        self.parent_scene.difficulty_chooser.enabled = False
                        self.parent_scene.scene_paused = False
                 

            if event.key == pygame.K_UP :
                for i in range(len(self.difficulty_mode_buttons)) :
                    if (self.difficulty_mode_buttons[i].sel == True) :
                        self.difficulty_mode_buttons[i].sel = False
                        self.difficulty_mode_buttons[ (i-1) % len(self.difficulty_mode_buttons)].sel = True
                        break
    
            if event.key == pygame.K_DOWN :
                for i in range(len(self.difficulty_mode_buttons)) :
                    if (self.difficulty_mode_buttons[i].sel == True) :
                        self.difficulty_mode_buttons[i].sel = False
                        self.difficulty_mode_buttons[ (i+1) % len(self.difficulty_mode_buttons)].sel = True
                        break

    def draw_difficulty_mode_buttons(self) :
        for button in self.difficulty_mode_buttons :
            button.draw()


    def handle_keypress(self) :
        pass

    def draw(self) :
        self.parent_scene.game.screen.blit(self.diff_text,
                                           (self.mainrect.x,self.mainrect.y - 100))
        pygame.draw.rect(self.parent_scene.game.screen,
                        (100,100,100),
                         (self.mainrect.x , self.mainrect.y , self.mainrect.width, self.mainrect.height),
                         5
                         )
        self.draw_difficulty_mode_buttons()
        
