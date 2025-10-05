import random
from collections import namedtuple

import pygame

import Doodler
import ledge

ScaledImage = namedtuple('ScaledImage', ['path', 'width', 'height'])

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

IMAGE_DATA = {
    'menu': ScaledImage("Sprites/loading_screen.png", 480, 800),
    'play_button': ScaledImage("Sprites/play@2x.png", 111, 40),
    'play_button_active': ScaledImage("Sprites/play@2x.png", 144, 52),
    'ledge_image': ScaledImage("Sprites/platform.png", 91, 23),
    'background': ScaledImage("Sprites/doodle_background.png", 480, 800),
    'big_monster1': ScaledImage("Sprites/big_monster3.png", 135, 86),
    'doodle_hitbox': ScaledImage("Sprites/doodle_himself_cropped_hitbox.png", 45, 61),
    'doodler_orig': ScaledImage("Sprites/doodle_himself.png", 68, 61)
}

def main():

    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    images = {
        name: load_scaled_image(details)
        for name, details
        in IMAGE_DATA.items()
    }

    doodle = Doodler.Doodler(images['doodler_orig'], images['doodle_hitbox'], 240, 700, 5.5)
    doodle_prev_bottom = doodle.rect.bottom
    game_end = False
    flipped = False
    platforms = pygame.sprite.Group()
    level = 0
    score = 0

    while True:
        exit = False
        cursor_x, cursor_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if cursor_x >= 36 and cursor_x <= 144 and cursor_y >= 579 and cursor_y <= 618:
                    exit = True

        if exit:
            break

        screen.blit(images['menu'], (0, 0))
        screen.blit(images['big_monster1'], (125, 300))
        if cursor_x >= 36 and cursor_x <= 144 and cursor_y >= 579 and cursor_y <= 618:
            screen.blit(images['play_button_active'], (23, 572))
        else:
            screen.blit(images['play_button'], (35, 580))
        pygame.display.flip()

    prev_y = 700
    for i in range(18):
        platform = ledge.Ledge(images['ledge_image'])
        if i % 2 == 0:
            platform.y_pos = ledge.relational_y(prev_y)
            prev_y = platform.y_pos
        platforms.add(platform)
        platforms.update(0)

    progress = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        doodle.y_pos -= doodle.speed # - because going up decreases y value
        if doodle.speed > 0:
            score += doodle.speed
        doodle.speed -= 0.05 #abritrary value I got by fiddling around-- it just looks right

        if doodle.y_pos >= 400:
            progress = False
        else:
            if progress == False and len(platforms.sprites()) < 40:
                platform = ledge.Ledge(images['ledge_image'])
                platform.y_pos = ledge.relational_y(prev_y)
                prev_y = platform.y_pos
                platforms.add(platform)
            progress = True
            while doodle.y_pos < 400:
                doodle.y_pos += 1
                platforms.update(1)

        if level == 0:
            if random.randint(0, 25) == 25 and len(platforms.sprites()) < 40:
                platform = ledge.Ledge(images['ledge_image'])
                platform.y_pos = ledge.relational_y(prev_y)
                platforms.add(platform)
        elif level == 1:
            if random.randint(0, 50) == 50 and len(platforms.sprites()) < 40:
                platform = ledge.Ledge(images['ledge_image'])
                platform.y_pos = ledge.relational_y(prev_y)
                platforms.add(platform)
        elif level == 2:
            if random.randint(0, 100) == 100 and len(platforms.sprites()) < 40:
                platform = ledge.Ledge(images['ledge_image'])
                platform.y_pos = ledge.relational_y(prev_y)
                platforms.add(platform)
        elif level == 3:
            if random.randint(0, 200) == 200 and len(platforms.sprites()) < 40:
                platform = ledge.Ledge(images['ledge_image'])
                platform.y_pos = ledge.relational_y(prev_y)
                platforms.add(platform)

        if doodle.y_pos > 800:
            game_end = True

        if doodle.y_pos > 400 and game_end:
            doodle.y_pos += doodle.speed * 1.5
            platforms.update(2)

        cursor_x, cursor_y = pygame.mouse.get_pos()

        if cursor_x < 240:
            doodle.image = pygame.transform.flip(images['doodler_orig'], True, False)
            doodle.rect = doodle.hitbox.get_rect(topright = (doodle.rect.right, doodle.rect.top))
            flipped = True
        elif cursor_x > 240:
            doodle.image = images['doodler_orig']
            flipped = False

        if cursor_x < 230 and cursor_x >= 200:
            doodle.x_pos -= 0.5
        elif cursor_x < 200 and cursor_x >= 150:
            doodle.x_pos -= 1
        elif cursor_x < 150 and cursor_x >= 90:
            doodle.x_pos -= 2
        elif cursor_x < 90 and cursor_x >= 30:
            doodle.x_pos -= 3.5
        elif cursor_x < 30 and cursor_x >= 0:
            doodle.x_pos -= 5
        elif cursor_x < 0:
            doodle.x_pos -= 10
        elif cursor_x > 250 and cursor_x <= 280:
            doodle.x_pos += 0.5
        elif cursor_x > 280 and cursor_x <= 320:
            doodle.x_pos += 1
        elif cursor_x > 320 and cursor_x <= 380:
            doodle.x_pos += 2
        elif cursor_x > 380 and cursor_x <= 450:
            doodle.x_pos += 3.5
        elif cursor_x > 450 and cursor_x <= 480:
            doodle.x_pos += 5
        elif cursor_x > 480:
            doodle.x_pos += 10

        if doodle.x_pos < -60:
            doodle.x_pos = 480
        elif doodle.x_pos > 480:
            doodle.x_pos = -60

        if score > 500:
            level = 1
        if score > 2000:
            level = 2
        if score > 5000:
            level = 3

        if flipped:
            doodle.rect = images['doodle_hitbox'].get_rect(topleft = (doodle.x_pos + 23, doodle.y_pos)) # adding an offset for hitbox to align with right corner, NOT left alexa: B)
        else:
            doodle.rect = images['doodle_hitbox'].get_rect(topleft = (doodle.x_pos, doodle.y_pos))

        platforms.update(0)

        for platform in platforms:
            if platform.rect.top >= doodle_prev_bottom and platform.rect.top <= doodle.rect.bottom and pygame.sprite.spritecollide(doodle, platforms, False) and doodle.speed <= 0:
                doodle.speed = 5.5

        screen.blit(images['background'], (0, 0))
        platforms.draw(screen)
        screen.blit(doodle.image, (doodle.x_pos, doodle.y_pos))

        doodle_prev_bottom = doodle.rect.bottom

        pygame.display.flip()

def load_scaled_image(details: ScaledImage):
    return pygame.transform.scale(
        pygame.image.load(details.path),
        (details.width, details.height),
    )

if __name__ == '__main__':
    main()