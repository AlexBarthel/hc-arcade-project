import pygame

# Initialize pygame
pygame.init()
# Configure pygame display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width = screen.get_width()
height = screen.get_height()

clock = pygame.time.Clock()
state = 1

# Preload menu icons
icons = {
    "sm-btn": pygame.image.load("img/storymode.png"),
    "sm-btn-alt": pygame.transform.scale_by(pygame.image.load("img/storymode-alt.png"), 1.1),
    "fp-btn": pygame.image.load("img/freeplay.png"),
    "fp-btn-alt": pygame.transform.scale_by(pygame.image.load("img/freeplay-alt.png"), 1.1),
    "op-btn": pygame.image.load("img/options.png"),
    "op-btn-alt": pygame.transform.scale_by(pygame.image.load("img/options-alt.png"), 1.1)
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
    buttons = [
        ("sm-btn", "sm-btn-alt", height / 3 - height / 6),
        ("fp-btn", "fp-btn-alt", height / 3 * 2 - height / 6),
        ("op-btn", "op-btn-alt", height / 3 * 3 - height / 6),
    ]
    # Loop over every button by index and check if its selected.
    # If selected, then swap to the alternate button art, otherwise
    # stick to the original file.
    for index, (btn, btn_alt, pos_y) in enumerate(buttons):
        key = btn_alt if selection == index else btn
        screen.blit(icons[key], icons[key].get_rect(center=(width / 2, pos_y)))

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
                stopsound()

    # Set background color
    screen.fill("black")

    if menu_index == -1: draw_main_menu()
    if menu_index == 0: draw_story_mode()
    if menu_index == 1: draw_freeplay()
    if menu_index == 2: draw_options()
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
