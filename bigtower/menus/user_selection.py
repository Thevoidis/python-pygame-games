import pygame

class Scene() :
    def __init__ (self, game , enlisted_users, next_scene=None) :
        self.game = game
        self.subscene_index = len(game.subscenes)
        self.enlisted_users = enlisted_users
        self.next_scene = next_scene
        self.mainbox_width = self.game.screen_size[0] // 2
        self.mainbox_height = self.game.screen_size[1] // 2
        self.mainbox_color = (10,10,10)
        self.mainbox =  pygame.Rect(
                self.game.screen_size[0] // 4,
                self.game.screen_size[1] // 4,
                self.mainbox_width,
                self.mainbox_height
                )

    def on_next_scene(self) :
        import importlib
        sceneLib = importlib.import_module(str(self.next_scene))
        loadedScene = getattr(sceneLib, "Scene")
        self.game.scene = loadedScene(self)


    def kill(self) :
        self.game.subscenes.pop(self.subscene_index) 

    def default_handle_event(self,event) :
        if event.type == pygame.KEYDOWN :
            if (event.key == pygame.K_ESCAPE):
                self.kill()

    def handle_event(self,event) :
        self.default_handle_event(event)

    def handle_keypress(self) :
        pass

 
    def on_update(self,delta_time) :
        pass


    def on_draw(self) :
        pygame.draw.rect(
                self.game.screen,
            self.mainbox_color,
            self.mainbox,
            )
   


