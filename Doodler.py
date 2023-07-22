import pygame

class Doodler(pygame.sprite.Sprite):

    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect
        self.x_pos = x
        self.y_pos = y
        self.speed = speed