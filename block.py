import pygame
import random


class Block:

    def __init__(self, main):
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.settings.b_width
        self.height = self.settings.b_height

        self.block_map = {
            'straight': (150, 0, 0),
            'left': (100, 100, 0),
            'right': (0, 150, 0),
            'square': (0, 100, 100),
            't': (0, 0, 150),
            'lz': (100, 0, 100),
            'rz': (100, 100, 100),
        }
        block_pool = ['straight', 'left', 'right', 'square', 't', 'lz', 'rz']
        self.shape = random.choice(block_pool)
        self.color = self.block_map[self.shape]

        # initialize main block for shape
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midtop
        self.y = self.rect.y
        self.x = self.rect.x

    def delete_part(self):
        pass

    def rotate_shape(self):
        pass

    def move_shape(self):
        self.y += self.settings.fall_speed
        self.rect.y = self.y

    def draw_shape(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
