import user_controls.Player_controls

from pygame.locals import *
import pygame


class App:
    window_width = 800
    window_height = 600
    user_controls = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.player = user_controls.Player_controls.Player()

    def on__init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.window_width,self.window_height),pygame.HWSURFACE)

        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()

            keys = pygame.key.get_pressed()
            if (keys[K_RIGHT]):
                self.player.move_player_right()
            if (keys[K_LEFT]):
                self.player.move_player_left()

            if (keys[K_UP]):
                self.player.move_player_up()

            if (keys[K_DOWN]):
                self.player.move_player_down()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

