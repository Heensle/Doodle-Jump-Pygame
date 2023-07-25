import random_num
import pygame

def x_range (start_range, end_range):
        return random_num.ledge_controlled_x(start_range, end_range)

def relational_y (prev_y):
        return random_num.ledge_relational_y(prev_y)

class Ledge(pygame.sprite.Sprite):
    
    def __init__ (self, image):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = random_num.ledge_rand_x()
        self.y_pos = random_num.ledge_rand_y()
        self.image = image
        self.rect = (self.image.get_rect(topleft = (self.x_pos, self.y_pos)))

    def update(self, num):
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))
        if num == 1: # normal shifting down
            self.y_pos += 1
        elif num == 2: # game_end shifting up
            self.y_pos -= 20

        if self.rect.top > 800:
             self.kill()