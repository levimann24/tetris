import pygame
import sys
import settings
import block


class Tetris:
    def __init__(self):
        self.settings = settings.Settings()

        # initialize the screen
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("Pygame Tetris")

        # initialize first shape
        self.shape_group = []
        self.create_shape()

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def on_loop(self):
        for shape in self.shape_group:
            shape.move_shape()

    def on_render(self):
        self.screen.fill(self.settings.bg_color)
        for shape in self.shape_group:
            shape.draw_shape()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def create_shape(self):
        new_shape = block.Block(self)
        self.shape_group.append(new_shape)


if __name__ == "__main__":
    game = Tetris()
    game.on_execute()
