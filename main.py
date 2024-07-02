import pygame

# Initialize pygame
pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)
# Configure pygame display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width = screen.get_width()
height = screen.get_height()

clock = pygame.time.Clock()
state = 1

# Preload menu icons
icons = {
    # "sm-btn": pygame.image.load("img/storymode.png"),
    # "sm-btn-alt": pygame.transform.scale_by(pygame.image.load("img/storymode-alt.png"), 1.1),
    # "fp-btn": pygame.image.load("img/freeplay.png"),
    # "fp-btn-alt": pygame.transform.scale_by(pygame.image.load("img/freeplay-alt.png"), 1.1),
    # "op-btn": pygame.image.load("img/options.png"),
    # "op-btn-alt": pygame.transform.scale_by(pygame.image.load("img/options-alt.png"), 1.1)
}

# Preload backgrounds
backgrounds = {
    "WEEK 1": pygame.image.load("img/Week 1.jpg"),
    "WEEK 2": pygame.image.load("img/Week 2.jpg"),
    "WEEK 3": pygame.image.load("img/Week 3.jpg"),
}

# Preload fonts
fonts = {
    "FS Sinclair Medium": pygame.font.Font("font/FS Sinclair Medium.otf"),
    "Swiss 721 Extended Bold": pygame.font.Font("font/Swiss 721 Extended Bold.otf", 48),
}


def playsound(filename, loop):
    # Use pygame's built-in mixer to play audio files
    # Steps: initialize -> load -> play
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1 if loop else 1)


def stopsound():
    # Stop all playing audio
    pygame.mixer.music.stop()


# Menu variables for UI
menu_index = -1
selection = 0
fade_in_value = 255


def draw_main_menu():
    # Store button locations on screen
    btns = [
        ("STORY MODE", height / 3 - height / 6),
        ("FREEPLAY", height / 3 * 2 - height / 6),
        ("OPTIONS", height / 3 * 3 - height / 6),
    ]

    # Render the menu buttons
    for index, (value, y) in enumerate(btns):
        text_surface = fonts["Swiss 721 Extended Bold"].render(
            value, 1, (255, 255, 255)
        )
        if index == selection:
            text_surface = pygame.transform.scale_by(text_surface, 1.1)
        screen.blit(
            text_surface,
            (width / 2 - text_surface.get_rect().centerx, y),
        )


def draw_story_mode():
    # Store button locations on screen
    btns = [
        ("WEEK 1", height / 3 - height / 6),
        ("WEEK 2", height / 3 * 2 - height / 6),
        ("WEEK 3", height / 3 * 3 - height / 6),
    ]

    # Get the selected button
    btn_id = btns[selection][0]

    # Draw week-specific backgrounds
    screen.blit(backgrounds[btn_id], backgrounds[btn_id].get_rect())

    # Render the menu buttons
    for index, (value, y) in enumerate(btns):
        text_surface = fonts["Swiss 721 Extended Bold"].render(
            value, 1, (255, 255, 255)
        )
        offset = 0
        if index == selection:
            # Scale the selected option by 110%
            text_surface = pygame.transform.scale_by(text_surface, 1.1)
            # Offset to the right
            offset = width / 24

        screen.blit(
            text_surface,
            (width / 6 - text_surface.get_rect().centerx + offset, y),
        )


# Play menu music on load
playsound("audio/menu-music.wav", True)

while state:
    # Listen for mouse/keyboard events
    for e in pygame.event.get():
        # Main menu events
        if e.type == pygame.KEYDOWN and menu_index == -1:
            if e.key == pygame.K_UP:
                selection += -1 if selection != 0 else 2
            if e.key == pygame.K_DOWN:
                selection += 1 if selection != 2 else -2
            if e.key == pygame.K_RETURN:
                menu_index = selection
                selection = 0
        if e.type == pygame.KEYDOWN and menu_index == 0:
            if e.key == pygame.K_UP:
                selection += -1 if selection != 0 else 2
            if e.key == pygame.K_DOWN:
                selection += 1 if selection != 2 else -2
            if e.key == pygame.K_RETURN:
                # TODO: Play selected song
                stopsound()

    # Set background color
    screen.fill("black")

    if menu_index == -1:
        draw_main_menu()
    if menu_index == 0:
        draw_story_mode()
    if menu_index == 1:
        draw_freeplay()
    if menu_index == 2:
        draw_options()
    # if menu_index == 3: draw_level(level_id)

    # Fade in on window load
    if fade_in_value > 0:
        fade_in_value -= 5
        fade_surface = pygame.Surface((width, height))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_in_value)
        screen.blit(fade_surface, (0, 0))

    # Render the screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

# Stop pygame to avoid any issues
pygame.quit()
