import pygame
import random


class Block:

    def __init__(self, main, p1='nothing', p2='nothing'):
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.settings.b_width
        self.height = self.settings.b_height
        self.border_color = (0, 0, 0)
        self.movement = True
        self.move_right = False
        self.move_left = False

        self.previous2 = [p1, p2]

        self.block_color = {
            'straight': (150, 0, 0),
            'left': (100, 100, 0),
            'right': (0, 150, 0),
            'square': (0, 100, 100),
            't': (0, 0, 150),
            'lz': (100, 0, 100),
            'rz': (100, 100, 100),
        }
        block_pool = ['straight', 'left', 'right', 'square', 't', 'lz', 'rz']
        new_pool = []
        for block in block_pool:
            if block in self.previous2:
                continue
            else:
                new_pool.append(block)
        print(new_pool)
        self.shape = random.choice(new_pool)
        self.color = self.block_color[self.shape]

        # initialize main block for shape
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midtop
        self.y = self.rect.y
        self.x = self.rect.x
        self.border_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.block_map = {
            'straight': [(self.x, self.y-self.height), (self.x, self.y-self.height*2), (self.x, self.y-self.height*3)],
            'left': [(self.x-self.width, self.y), (self.x, self.y-self.height), (self.x, self.y-self.height*2)],
            'right': [(self.x+self.width, self.y), (self.x, self.y-self.height), (self.x, self.y-self.height*2)],
            'square': [(self.x-self.width, self.y), (self.x, self.y-self.height), (self.x-self.width, self.y-self.height)],
            't': [(self.x-self.width, self.y), (self.x, self.y-self.height), (self.x+self.width, self.y)],
            'lz': [(self.x-self.width, self.y), (self.x, self.y-self.height), (self.x+self.width, self.y-self.height)],
            'rz': [(self.x-self.width, self.y-self.height), (self.x, self.y-self.height), (self.x+self.width, self.y)],

        }
        self.component_rects = []
        self.component_borders = []
        for block in self.block_map[self.shape]:
            block_rect = pygame.Rect(
                block[0], block[1], self.width, self.height)
            block_border = pygame.Rect(
                block[0], block[1], self.width, self.height)
            self.component_rects.append(block_rect)
            self.component_borders.append(block_border)

    def delete_part(self):
        pass

    def rotate_shape(self):
        pass

    def move_shape(self):
        if self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.fall_speed
            self.rect.y = self.y
            self.border_rect.y = self.y
            self._move_components()
            if self.move_right:
                self.x += self.settings.b_x_speed
                self.rect.x = self.x
                self.border_rect.x = self.x
                self._move_components_sideways()
            if self.move_left:
                self.x -= self.settings.b_x_speed
                self.rect.x = self.x
                self.border_rect.x = self.x
                self._move_components_sideways()
        else:
            self.movement = False

    def draw_shape(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.border_color, self.border_rect, 1)
        self._draw_components()

    def _draw_components(self):
        for rect in self.component_rects:
            pygame.draw.rect(self.screen, self.color, rect)
        for b_rect in self.component_borders:
            pygame.draw.rect(self.screen, self.border_color, b_rect, 1)

    def _move_components(self):
        for rect in self.component_rects:
            rect.y += self.settings.fall_speed
        for rect in self.component_borders:
            rect.y += self.settings.fall_speed

    def _move_components_sideways(self):
        for rect in self.component_rects:
            if self.move_right:
                rect.x += self.settings.b_x_speed
            if self.move_left:
                rect.x -= self.settings.b_x_speed
        for rect in self.component_borders:
            if self.move_right:
                rect.x += self.settings.b_x_speed
            if self.move_left:
                rect.x -= self.settings.b_x_speed
