import random_num
import pygame

class Ledge(pygame.sprite.Sprite):
    
    def __init__ (self, image):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = random_num.ledge_rand_x()
        self.y_pos = random_num.ledge_rand_y()
        self.image = image
        self.rect = self.image.get_rect()

def x_range (start_range, end_range):
        return random_num.ledge_controlled_x(start_range, end_range)

def relational_y (prev_y):
        return random_num.ledge_relational_y(prev_y)