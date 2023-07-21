import pygame

import platform    

def main():

    pygame.init()
    screen = pygame.display.set_mode((480, 800))
    menu = pygame.transform.scale(pygame.image.load("Sprites/loading_screen.png"), (480, 800))
    play_button = pygame.transform.scale(pygame.image.load("Sprites/play@2x.png"), (111, 40))
    play_button_active = pygame.transform.scale(pygame.image.load("Sprites/play@2x.png"), (144, 52))
    platform = pygame.transform.scale(pygame.image.load("Sprites/platform.png"), (91, 23))
    background = pygame.transform.scale(pygame.image.load("Sprites/doodle_background.png"), (480, 800))
    big_monster1 = pygame.transform.scale(pygame.image.load("Sprites/big_monster3.png"), (135, 86))
    doodler_orig = pygame.transform.scale(pygame.image.load("Sprites/doodle_himself.png"), (68, 61))
    doodler = doodler_orig
    doodler_x = 240
    doodler_y = 700
    speed = 5.5

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

        screen.blit(menu, (0, 0))
        screen.blit(big_monster1, (125, 300))
        screen.blit(platform, (23, 572))
        if cursor_x >= 36 and cursor_x <= 144 and cursor_y >= 579 and cursor_y <= 618:
            screen.blit(play_button_active, (23, 572))
        else:
            screen.blit(play_button, (35, 580))
        pygame.display.flip()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            

        if doodler_y >= 700: # temp lower celing to bounce off
            speed = 5.5 # resets speed
        
        doodler_y -= speed # - because going up decreases y value
        speed -= 0.05 #abritrary value I got by fiddling around-- it just looks right
        
        if doodler_y < 400:
            doodler_y = 400


        cursor_x, cursor_y = pygame.mouse.get_pos()

        if cursor_x < 240:
            doodler = pygame.transform.flip(doodler_orig, True, False)
        elif cursor_x > 240:
            doodler = doodler_orig

        if cursor_x < 240 and cursor_x >= 200:
            doodler_x -= 1
        elif cursor_x < 200 and cursor_x >= 150:
            doodler_x -= 2
        elif cursor_x < 150 and cursor_x >= 90:
            doodler_x -= 3
        elif cursor_x < 90 and cursor_x >= 30:
            doodler_x -= 4
        elif cursor_x < 30 and cursor_x >= 0:
            doodler_x -= 5
        elif cursor_x < 0:
            doodler_x -= 10
        elif cursor_x > 240 and cursor_x <= 280:
            doodler_x += 1
        elif cursor_x > 280 and cursor_x <= 320:
            doodler_x += 2
        elif cursor_x > 320 and cursor_x <= 380:
            doodler_x += 3
        elif cursor_x > 380 and cursor_x <= 450:
            doodler_x += 4
        elif cursor_x > 450 and cursor_x <= 480:
            doodler_x += 5
        elif cursor_x > 480:
            doodler_x += 10

        if doodler_x < 0:
            doodler_x = 480
        elif doodler_x > 480:
            doodler_x = 0

        screen.blit(background, (0, 0))
        screen.blit(platform, (23, 572))
        screen.blit(doodler, (doodler_x, doodler_y))

        pygame.display.flip()


    


if __name__ == '__main__':
    main()