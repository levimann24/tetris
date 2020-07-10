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
        self.movement_index = 0

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_d:
                    self.shape_group[self.movement_index].move_right = True
                if event.key == pygame.K_a:
                    self.shape_group[self.movement_index].move_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.shape_group[self.movement_index].move_right = False
                if event.key == pygame.K_a:
                    self.shape_group[self.movement_index].move_left = False

    def on_loop(self):
        if self.shape_group[self.movement_index].movement:
            self.shape_group[self.movement_index].move_shape()
        else:
            self.movement_index += 1
            self.create_shape()

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
        if len(self.shape_group) < 1:
            new_shape = block.Block(self)
            self.shape_group.append(new_shape)
        elif len(self.shape_group) < 2:
            p1 = self.shape_group[-1].shape
            new_shape = block.Block(self, p1)
            self.shape_group.append(new_shape)
        else:
            p1 = self.shape_group[-1].shape
            p2 = self.shape_group[-2].shape
            new_shape = block.Block(self, p1, p2)
            self.shape_group.append(new_shape)


if __name__ == "__main__":
    game = Tetris()
    game.on_execute()
