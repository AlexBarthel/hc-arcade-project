# FRIDAY NIGHT LIBERATIN'

import pygame

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
state = 1
width = screen.get_width()
height = screen.get_height()

# define icons
icons = {
    "sm-btn": pygame.image.load("img/storymode.png"),
    "sm-btn-alt": pygame.transform.scale_by(pygame.image.load("img/storymode-alt.png"), 1.1),
    "fp-btn": pygame.image.load("img/freeplay.png"),
    "fp-btn-alt": pygame.transform.scale_by(pygame.image.load("img/freeplay-alt.png"), 1.1),
    "op-btn": pygame.image.load("img/options.png"),
    "op-btn-alt": pygame.transform.scale_by(pygame.image.load("img/options-alt.png"), 1.1)
}

def playsound(filename, loop):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1 if loop else 1)

def stopsound():
    pygame.mixer.music.stop()

# menu variables
menu_index = -1
selection = 0

def draw_main_menu():
    if selection == 0:
        screen.blit(icons["sm-btn-alt"], icons["sm-btn-alt"].get_rect(center=(width/2, height/3 - height/6)))
    else:
        screen.blit(icons["sm-btn"], icons["sm-btn"].get_rect(center=(width/2, height/3 - height/6)))
    
    if selection == 1:
        screen.blit(icons["fp-btn-alt"], icons["fp-btn-alt"].get_rect(center=(width/2, height/3*2 - height/6)))
    else:
        screen.blit(icons["fp-btn"], icons["fp-btn"].get_rect(center=(width/2, height/3*2 - height/6)))

    if selection == 2:
        screen.blit(icons["op-btn-alt"], icons["op-btn-alt"].get_rect(center=(width/2, height/3*3 - height/6)))
    else:
        screen.blit(icons["op-btn"], icons["op-btn"].get_rect(center=(width/2, height/3*3 - height/6)))

# play menu music
playsound("audio/menu-music.wav", True)

while state:
    # poll for events
    for e in pygame.event.get():
        # menu-0 key events
        if e.type == pygame.KEYDOWN and menu_index == -1:
            if e.key == pygame.K_UP:
                selection += -1 if selection != 0 else 2
            if e.key == pygame.K_DOWN:
                selection += 1 if selection != 2 else -2
            if e.key == pygame.K_RETURN:
                menu_index = selection
                stopsound()

    # set background
    screen.fill("black")

    if menu_index == -1: draw_main_menu()
    
    # render the screen
    pygame.display.flip()

    # limit FPS
    clock.tick(60)

pygame.quit()