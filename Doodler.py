import pygame

class Doodler(pygame.sprite.Sprite):

    def __init__(self, image, hitbox, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.hitbox = hitbox
        self.rect = hitbox.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.speed = speed
