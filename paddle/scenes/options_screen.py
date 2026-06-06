import pygame

from gui_utils.gui_elements import Button
class Scene :
    def __init__(self, parent_scene ,game):
        self.game = game
        self.parent_scene = parent_scene
        self.welcomeTextRaw = "     What now ?  "
        self.welcome_text = self.game.title_font.render(
                self.welcomeTextRaw,
                True,
                (100,150,50)
                )
        self.selected_main_option = "New Game"
        self.title_rect = pygame.Rect(self.game.screen_size[0]//2 , self.game.screen_size[1]//2,400,50)
        
        # buttons
        self.newgame_button = Button(self.game,
                            (self.title_rect.x + 10, self.title_rect.y + 50),
                            (self.title_rect.width - 20, self.title_rect.height),"New Game", sel= True)

        self.loadgame_button = Button(self.game,
                            (self.title_rect.x + 10, self.title_rect.y + 110),
                            (self.title_rect.width - 20, self.title_rect.height),"Load Game")

        self.savegame_button = Button(self.game,
                            (self.title_rect.x + 10, self.title_rect.y + 170),
                            (self.title_rect.width - 20, self.title_rect.height),"Save Game")
        self.difficulty_button = Button(self.game,
                            (self.title_rect.x + 10, self.title_rect.y + 230),
                            (self.title_rect.width - 20, self.title_rect.height),"Choose Difficulty")

        self.quitgame_button = Button(self.game,
                            (self.title_rect.x + 10 , self.title_rect.y + 290),
                            (self.title_rect.width - 20 , self.title_rect.height),"Quit Game")

        self.menubuttons = [self.newgame_button , self.loadgame_button , self.savegame_button ,self.difficulty_button ,self.quitgame_button ]
    def update(self) :
        pass

    def handle_event(self,event) :
        if event.type == pygame.KEYDOWN :
            if (self.quitgame_button.sel == True) and (event.key == pygame.K_RETURN):
                self.game.running = False
    

            elif (self.newgame_button.sel == True) and (event.key == pygame.K_RETURN):
                del self.game.scene
                from scenes.scene_1 import Scene
                self.game.scene = Scene(self.game)
                self.parent_scene = self.game.scene
                self.parent_scene.scene_paused = False

            elif (self.difficulty_button.sel == True) and (event.key == pygame.K_RETURN):
                self.parent_scene.difficulty_chooser.enabled = True
                self.parent_scene.options_screen_enabled = False

            elif (self.loadgame_button.sel == True) and (event.key == pygame.K_RETURN):
                self.game.load_save()
                self.parent_scene.scene_paused = False
                self.parent_scene.options_screen_enabled = False

            elif (self.savegame_button.sel == True) and (event.key == pygame.K_RETURN):
                self.game.update_save()
                self.parent_scene.scene_paused = False
                self.parent_scene.options_screen_enabled = False
            


            if event.key == pygame.K_ESCAPE :
                self.parent_scene.options_screen_enabled = False
                self.parent_scene.scene_paused = False

            if event.key == pygame.K_UP :
                for i in range(len(self.menubuttons)) :
                    if (self.menubuttons[i].sel == True) :
                        self.menubuttons[i].sel = False
                        self.menubuttons[ (i-1) % len(self.menubuttons)].sel = True
                        break
    
            if event.key == pygame.K_DOWN :
                for i in range(len(self.menubuttons)) :
                    if (self.menubuttons[i].sel == True) :
                        self.menubuttons[i].sel = False
                        self.menubuttons[ (i+1) % len(self.menubuttons)].sel = True
                        break

    def handle_keypress(self) :
        pass
    
    def draw_menuoptions(self) :
        for button in self.menubuttons :
            button.draw()

    def draw(self) :
        self.game.screen.blit(self.welcome_text,
                              self.title_rect
        )

        # Border rectangle
        pygame.draw.rect(self.game.screen,
                         self.game.sel_color,
                         ( self.title_rect.x , self.title_rect.y - 10, 
                             self.title_rect.width , (len(self.menubuttons) + 1)*60),
                         5)
        self.draw_menuoptions()
        

